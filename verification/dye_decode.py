import cv2
import numpy as np
import json
import sys
import os

class BioStateValidator:
    def __init__(self, calibration_slope=-0.5, calibration_intercept=-20):
        """
        Initialize with calibration data for the specific voltage dye (e.g., DiBAC4(3) or CC2-DMPE).
        Formula: Vmem = (Fluorescence_Intensity * slope) + intercept
        
        Note: Real calibration requires a standard curve using clamped cells.
        """
        self.slope = calibration_slope
        self.intercept = calibration_intercept

    def load_subroutine(self, json_path):
        """Loads the Target Bioelectric State from our MorphoLang Schema."""
        with open(json_path, 'r') as f:
            data = json.load(f)
        return data['bioelectric_state']

    def analyze_image(self, image_path):
        """
        Reads a fluorescence microscopy image and converts it to a Voltage Map.
        """
        # Load image (Grayscale for intensity analysis)
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if img is None:
            print(f"[!] Error: Could not load image at {image_path}")
            return None

        # Pre-processing: Denoising (The text notes bioelectric signals are slow/steady, not noisy spikes)
        img_blur = cv2.GaussianBlur(img, (5, 5), 0)

        # Convert Pixel Intensity (0-255) to Membrane Potential (mV)
        # Higher fluorescence often means Depolarization (less negative) or Hyperpolarization
        # depending on the specific dye type (anionic vs cationic). 
        # Here we assume brighter = depolarized (typical for some anionic dyes).
        vmem_map = (img_blur * self.slope) + self.intercept
        
        return vmem_map

    def verify_state(self, vmem_map, target_state):
        """
        Compares the observed Vmem against the Target Range defined in the schema.
        """
        target_range = target_state['target_vmem_range'] # e.g., [-30, -50]
        spatial_domain = target_state['spatial_domain']
        
        # In a full version, we would use segmentation (AI) to find the 'spatial_domain' (e.g., "Eye Field").
        # Here, we analyze the Region of Interest (ROI) with the highest signal change.
        
        if vmem_map is None:
             return False, "FAILURE: No Vmem map data."

        avg_observed_vmem = np.mean(vmem_map)
        
        print(f"[*] Analyzing Domain: {spatial_domain}...")
        print(f"[*] Target Range:     {target_range} mV")
        print(f"[*] Observed Avg:     {avg_observed_vmem:.2f} mV")
        
        # Verification Logic
        # Note: Range is often [Min, Max] (e.g., [-50, -30])
        # Ensure we handle list sorting correctly
        min_v, max_v = sorted(target_range)
        
        if min_v <= avg_observed_vmem <= max_v:
            return True, "SUCCESS: Tissue has entered the Target Bioelectric State."
        else:
            diff = min_v - avg_observed_vmem
            # Correct diff calculation logic
            if avg_observed_vmem < min_v:
                 diff = min_v - avg_observed_vmem
            elif avg_observed_vmem > max_v:
                 diff = avg_observed_vmem - max_v
            else:
                 diff = 0
            
            return False, f"FAILURE: State Mismatch. Deviation: {diff:.2f} mV"

# --- EXECUTION MOCKUP ---
if __name__ == "__main__":
    validator = BioStateValidator()
    
    # 1. Load the Target State (The "Standard Format" we defined earlier)
    # We pretend we are checking the "Eye Induction" subroutine
    target_state = {
        "target_vmem_range": [-30, -50],
        "spatial_domain": "ventral_ectoderm"
    }
    
    # 2. Analyze a Mock Image (In real usage, this is your microscope file)
    # Creating a dummy image where pixels are effectively "-40mV"
    # Inverse calibration: Intensity = (Vmem - intercept) / slope
    # Vmem = -40
    # -40 = (I * -0.5) + -20
    # -20 = I * -0.5
    # I = 40
    target_intensity = int((-40 - (-20)) / -0.5)
    
    # Generate a dummy image file for testing
    mock_image_data = np.full((100, 100), target_intensity, dtype=np.uint8)
    cv2.imwrite('microscope_capture.png', mock_image_data)
    
    # 3. Run Verification
    vmem_map = validator.analyze_image('microscope_capture.png')
    success, message = validator.verify_state(vmem_map, target_state)
    
    print(message)
    
    # Clean up
    if os.path.exists('microscope_capture.png'):
        os.remove('microscope_capture.png')
