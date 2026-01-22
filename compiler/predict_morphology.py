import json
import os
from typing import List, Dict, Optional, Tuple

class BioDecoder:
    def __init__(self, database_path=None):
        """Initialize the decoder with the bioelectric database."""
        if database_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            database_path = os.path.join(base_dir, 'database', 'database_seed.json')
        
        self.library = self._load_library(database_path)

    def _load_library(self, path: str) -> List[Dict]:
        """Loads the bioelectric subroutines."""
        if not os.path.exists(path):
            print(f"[!] Warning: Database not found at {path}.")
            return []
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"[!] Error: Failed to decode JSON from {path}.")
            return []

    def predict(self, vmem: float, spatial_domain: str, species: str = None) -> List[Dict]:
        """
        Inverse Lookup: Predicts morphological outcome based on observed bioelectric state.
        
        Args:
            vmem (float): Observed membrane potential in mV (e.g., -40.0).
            spatial_domain (str): Tissue location (e.g., 'ventral_ectoderm').
            species (str, optional): Filter by species.
            
        Returns:
            List[Dict]: List of matching subroutines/predictions.
        """
        matches = []
        
        print(f"[*] Analyzing bioelectric pattern: {vmem} mV in '{spatial_domain}'...")
        
        for sub in self.library:
            # Check Species (if provided)
            target = sub['target_morphology']
            if species and target['species'].lower() != species.lower():
                continue
                
            # Check Spatial Domain (fuzzy match)
            state = sub['bioelectric_state']
            if spatial_domain.lower() not in state['spatial_domain'].lower() and \
               state['spatial_domain'].lower() not in spatial_domain.lower():
                continue
                
            # Check Voltage Range
            min_v, max_v = sorted(state['target_vmem_range'])
            if min_v <= vmem <= max_v:
                matches.append(sub)
                
        return matches

    def generate_report(self, matches: List[Dict]) -> str:
        """Generates a readable prediction report."""
        if not matches:
            return "No matching morphological outcomes found for this pattern."
            
        report = []
        report.append("=" * 60)
        report.append("BIOELECTRIC PATTERN DECODER REPORT")
        report.append(f"Matches Found: {len(matches)}")
        report.append("=" * 60)
        
        for i, match in enumerate(matches, 1):
            target = match['target_morphology']
            state = match['bioelectric_state']
            
            report.append(f"\nPREDICTION #{i}: {target['action'].upper()} {target['organ'].upper()}")
            report.append(f"  Species:    {target['species']}")
            report.append(f"  Mechanism:  {state['notes']}")
            report.append(f"  Confidence: High (Voltage matches target range {state['target_vmem_range']} mV)")
            
            if 'downstream_biomarkers' in match:
                markers = [m['gene'] for m in match['downstream_biomarkers']]
                report.append(f"  Verifiers:  Check for expression of {', '.join(markers)}")
                
        report.append("-" * 60)
        return "\n".join(report)

if __name__ == "__main__":
    # Example Usage
    decoder = BioDecoder()
    
    # User sees -40mV in frog gut
    predictions = decoder.predict(vmem=-40.0, spatial_domain="ventral_ectoderm", species="Xenopus laevis")
    
    print(decoder.generate_report(predictions))
