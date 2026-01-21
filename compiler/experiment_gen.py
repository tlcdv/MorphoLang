import json
import os
from typing import List, Dict, Optional
from datetime import datetime

class BioCompiler:
    def __init__(self, database_path=None):
        if database_path is None:
            # Resolve path relative to this script
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            database_path = os.path.join(base_dir, 'database', 'database_seed.json')
        
        self.library = self._load_library(database_path)

    def _load_library(self, path: str) -> List[Dict]:
        """Loads the bioelectric subroutines from the database file."""
        if not os.path.exists(path):
            print(f"[!] Warning: Database not found at {path}. implementation will be empty.")
            return []
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"[!] Error: Failed to decode JSON from {path}.")
            return []

    def find_subroutine(self, organ: str, species: str) -> Optional[Dict]:
        """Scans the library for a matching high-level command."""
        print(f"[*] Compiling request: Build '{organ}' in '{species}'...")
        for sub in self.library:
            target = sub['target_morphology']
            # Flexible matching
            if target['organ'].lower() == organ.lower() and \
               target['species'].lower() == species.lower():
                return sub
        return None

    def generate_protocol(self, subroutine: Dict) -> str:
        """Translates the Bioelectric State into a Lab Protocol."""
        target = subroutine['target_morphology']
        state = subroutine['bioelectric_state']
        drivers = subroutine['hardware_drivers']
        dev_context = subroutine.get('developmental_context', {})
        
        # Header
        protocol = []
        protocol.append(f"BIOELECTRIC COMPILER PROTOCOL v1.1")
        protocol.append(f"generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        protocol.append(f"TARGET: {target['action'].upper()} {target['organ'].upper()} in {target['species']}")
        protocol.append("-" * 50)
        
        # Phase 0: Developmental Context (NEW)
        if dev_context:
            protocol.append(f"\n[PHASE 0: DEVELOPMENTAL CONTEXT]")
            protocol.append(f"Intervention Window:")
            protocol.append(f"  > Start Stage:    {dev_context.get('stage_start', 'Unknown')}")
            protocol.append(f"  > End Stage:      {dev_context.get('stage_end', 'Unknown')}")
            protocol.append(f"  > System:         {dev_context.get('reference_system', 'Unknown')}")

        # The "Software" Logic (Physiological Goal)
        protocol.append(f"\n[PHASE 1: TARGET STATE DEFINITION]")
        protocol.append(f"To achieve {target['organ']} morphogenesis, the tissue must enter the following state:")
        protocol.append(f"  > Spatial Domain: {state['spatial_domain']}")
        protocol.append(f"  > Target Vmem:    {state['target_vmem_range']} mV")
        protocol.append(f"  > Duration:       {state['duration_hours']} hours")
        protocol.append(f"  > Logic Note:     {state.get('notes', '')}")

        # The "Hardware" Execution (Machine Code)
        protocol.append(f"\n[PHASE 2: HARDWARE SELECTION]")
        protocol.append(f"Select ONE of the following drivers to instantiate the state:")
        
        for i, driver in enumerate(drivers, 1):
            protocol.append(f"\n  OPTION {i}: {driver['name']} ({driver['type']})")
            protocol.append(f"    - Mechanism: {driver['mechanism_of_action']}")
            protocol.append(f"    - Dosage:    {driver.get('dosage', 'See paper')}")
        
        if 'metadata' in subroutine and 'references' in subroutine['metadata']:
             protocol.append(f"\n  Sources: {', '.join(subroutine['metadata']['references'])}")

        # Warnings based on text safety guidelines
        protocol.append(f"\n[PHASE 3: SAFETY & VERIFICATION]")
        protocol.append(f"(!) WARNING: High voltage/current can cause irreversible damage.")
        protocol.append(f"(!) VERIFY:  Use Ratiometric Voltage Imaging (CC2-DMPE / DiBAC4(3)) to confirm Vmem change.")
        
        return "\n".join(protocol)

# --- EXECUTION EXAMPLE ---
if __name__ == "__main__":
    compiler = BioCompiler()
    
    # User Request: "I want to build an eye in a frog."
    # Note: The seed data has "Xenopus laevis" and "eye"
    result_subroutine = compiler.find_subroutine(organ="eye", species="Xenopus laevis")
    
    if result_subroutine:
        lab_protocol = compiler.generate_protocol(result_subroutine)
        print(lab_protocol)
    else:
        print("[!] Error: No known bioelectric subroutine for this morphology.")
