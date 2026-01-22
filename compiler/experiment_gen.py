import json
import os
from typing import List, Dict, Optional
from datetime import datetime

class BioCompiler:
    def __init__(self, database_path=None):
        if database_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            database_path = os.path.join(base_dir, 'database', 'database_seed.json')
        
        self.library = self._load_library(database_path)

    def _load_library(self, path: str) -> List[Dict]:
        """Loads the bioelectric subroutines from the database file."""
        if not os.path.exists(path):
            print(f"[!] Warning: Database not found at {path}.")
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
            if target['organ'].lower() == organ.lower() and \
               target['species'].lower() == species.lower():
                return sub
        return None

    def _analyze_spatial_risks(self, spatial_domain: str, delivery_method: Dict) -> Optional[str]:
        """Check for mismatches between target domain and delivery method."""
        local_domains = ['ventral_ectoderm', 'amputation_stump', 'regeneration_bud', 'blastema']
        
        is_local_target = any(domain in spatial_domain.lower() for domain in local_domains)
        is_systemic_delivery = delivery_method.get('spatial_restriction') == 'systemic'
        
        if is_local_target and is_systemic_delivery:
            return (
                "WARNING: GLOBAL REMODELING RISK DETECTED\n"
                f"   Target domain '{spatial_domain}' requires LOCAL intervention,\n"
                f"   but delivery method '{delivery_method['type']}' is SYSTEMIC.\n"
                "   Risk: Entire bioelectric network may be affected.\n"
                "   Recommendation: Consider microinjection or bead implantation."
            )
        return None

    def _generate_monitoring_schedule(self, control_loop: Dict, state: Dict) -> List[str]:
        """Generate time-based monitoring checkpoints."""
        protocol = []
        protocol.append("Monitoring Schedule:")
        protocol.append(f"  Frequency: {control_loop['monitoring_frequency']}")
        protocol.append(f"  Duration:  {state['duration_hours']}h (minimum) to {control_loop['termination_criteria']['max_duration_hours']}h (maximum)")
        protocol.append("")
        protocol.append("Recommended Measurement Timeline:")
        
        max_hours = control_loop['termination_criteria']['max_duration_hours']
        
        if max_hours <= 48:
            checkpoints = [0, 4, 8, 12, 24, 36, 48]
        elif max_hours <= 72:
            checkpoints = [0, 6, 12, 24, 36, 48, 60, 72]
        else:
            checkpoints = [0, 8, 24, 48, 72, 96, 120, 168]
        
        checkpoints = [t for t in checkpoints if t <= max_hours]
        
        for t in checkpoints:
            if t == 0:
                protocol.append(f"  T+{t}h:  Baseline measurement (immediately post-intervention)")
            else:
                protocol.append(f"  T+{t}h:  Verify Vmem remains in target range")
        
        return protocol

    def _generate_feedback_logic(self, control_loop: Dict, state: Dict) -> List[str]:
        """Generate decision tree for homeostatic feedback."""
        protocol = []
        protocol.append("Feedback Decision Tree:")
        protocol.append("")
        
        feedback = control_loop['feedback_mechanism']
        target_range = state['target_vmem_range']
        min_v, max_v = sorted(target_range)
        
        protocol.append("At each measurement checkpoint:")
        protocol.append("")
        protocol.append(f"  IF Vmem > {feedback.get('if_vmem_drifts_above', max_v)}mV (Upper Drift):")
        protocol.append(f"     -> TRIGGER: Tissue is drifting toward depolarization")
        protocol.append(f"     -> ACTION:  {feedback.get('corrective_action', 'Monitor closely')}")
        protocol.append("")
        protocol.append(f"  ELSE IF Vmem < {feedback.get('if_vmem_drifts_below', min_v)}mV (Lower Drift):")
        protocol.append(f"     -> TRIGGER: Tissue is drifting toward excessive hyperpolarization")
        protocol.append(f"     -> ACTION:  {feedback.get('corrective_action', 'Allow stabilization')}")
        protocol.append("")
        protocol.append(f"  ELSE (Vmem within [{min_v}, {max_v}]mV):")
        protocol.append(f"     -> STATUS:  Target state MAINTAINED")
        protocol.append(f"     -> ACTION:  Continue monitoring at scheduled intervals")
        
        return protocol

    def _generate_termination_criteria(self, control_loop: Dict) -> List[str]:
        """Generate stop conditions for the intervention."""
        protocol = []
        criteria = control_loop['termination_criteria']
        
        protocol.append("STOP CONDITIONS (Any of the following):")
        protocol.append("")
        
        if criteria.get('anatomical_marker'):
            protocol.append(f"  1. ANATOMICAL: {criteria['anatomical_marker']}")
        
        if criteria.get('bioelectric_marker'):
            protocol.append(f"  2. BIOELECTRIC: {criteria['bioelectric_marker']}")
        
        protocol.append(f"  3. SAFETY CUTOFF: {criteria['max_duration_hours']} hours elapsed")
        protocol.append(f"     (Maximum intervention duration to prevent overgrowth/tumors)")
        
        return protocol

    def _generate_genetic_verification(self, biomarkers: List[Dict]) -> List[str]:
        """Generate secondary verification steps using genetic markers."""
        protocol = []
        protocol.append("SECONDARY VERIFICATION (Genetic Markers):")
        protocol.append("Confirm bioelectric state has successfully triggered transcriptional machinery:")
        protocol.append("")
        
        for marker in biomarkers:
            protocol.append(f"  > Gene:      {marker['gene']}")
            protocol.append(f"    Expected:  {marker['expected_expression'].upper()}")
            protocol.append(f"    Timing:    {marker['check_time']}")
            protocol.append(f"    Location:  {marker['location']}")
            protocol.append("")
            
        return protocol

    def generate_protocol(self, subroutine: Dict) -> str:
        """Translates the Bioelectric State into a Homeostatic Control Protocol."""
        target = subroutine['target_morphology']
        state = subroutine['bioelectric_state']
        drivers = subroutine['hardware_drivers']
        dev_context = subroutine.get('developmental_context', {})
        control_loop = subroutine.get('control_loop', {})
        delivery = subroutine.get('delivery_method', {})
        biomarkers = subroutine.get('downstream_biomarkers', [])
        
        protocol = []
        protocol.append("=" * 70)
        protocol.append(f"BIOELECTRIC COMPILER PROTOCOL v0.4 (Genetic Interface)")
        protocol.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        protocol.append(f"TARGET: {target['action'].upper()} {target['organ'].upper()} in {target['species']}")
        protocol.append("=" * 70)
        
        if dev_context:
            protocol.append("")
            protocol.append("[PHASE 0: DEVELOPMENTAL CONTEXT]")
            protocol.append(f"Intervention Window:")
            protocol.append(f"  > Start Stage:    {dev_context.get('stage_start', 'Unknown')}")
            protocol.append(f"  > End Stage:      {dev_context.get('stage_end', 'Unknown')}")
            protocol.append(f"  > System:         {dev_context.get('reference_system', 'Unknown')}")

        protocol.append("")
        protocol.append("[PHASE 1: TARGET STATE DEFINITION]")
        protocol.append(f"To achieve {target['organ']} morphogenesis, tissue must enter:")
        protocol.append(f"  > Spatial Domain: {state['spatial_domain']}")
        protocol.append(f"  > Target Vmem:    {state['target_vmem_range']} mV")
        protocol.append(f"  > Duration:       {state['duration_hours']}h (minimum)")
        protocol.append(f"  > Profile:        {state.get('temporal_profile', 'constant').upper()} signal")
        protocol.append(f"  > Notes:          {state.get('notes', 'N/A')}")

        protocol.append("")
        protocol.append("[PHASE 2: HARDWARE SELECTION]")
        protocol.append("Select ONE of the following drivers:")
        
        for i, driver in enumerate(drivers, 1):
            protocol.append(f"")
            protocol.append(f"  OPTION {i}: {driver['name']} ({driver['type']})")
            protocol.append(f"    - Mechanism: {driver['mechanism_of_action']}")
            protocol.append(f"    - Dosage:    {driver.get('dosage', 'See references')}")
        
        if 'metadata' in subroutine and 'references' in subroutine['metadata']:
            protocol.append(f"")
            protocol.append(f"  References: {', '.join(subroutine['metadata']['references'])}")

        if delivery:
            protocol.append("")
            protocol.append("[PHASE 3: DELIVERY & SPATIAL CONSTRAINTS]")
            protocol.append(f"Method:       {delivery.get('type', 'Unknown')}")
            protocol.append(f"Restriction:  {delivery.get('spatial_restriction', 'Unknown')}")
            protocol.append(f"Timing:       {delivery.get('timing', 'See context')}")
            if delivery.get('notes'):
                protocol.append(f"Notes:        {delivery['notes']}")
            
            spatial_warning = self._analyze_spatial_risks(state['spatial_domain'], delivery)
            if spatial_warning:
                protocol.append("")
                protocol.append(spatial_warning)

        if control_loop:
            protocol.append("")
            protocol.append("[PHASE 4: HOMEOSTATIC MAINTENANCE]")
            protocol.append("This is a CLOSED-LOOP intervention. The tissue will attempt to")
            protocol.append("restore its original setpoint. Active monitoring and feedback are required.")
            protocol.append("")
            
            schedule = self._generate_monitoring_schedule(control_loop, state)
            for line in schedule:
                protocol.append(line)
            
            protocol.append("")
            
            feedback = self._generate_feedback_logic(control_loop, state)
            for line in feedback:
                protocol.append(line)
            
            protocol.append("")
            
            termination = self._generate_termination_criteria(control_loop)
            for line in termination:
                protocol.append(line)

        protocol.append("")
        protocol.append("[PHASE 5: SAFETY & VERIFICATION]")
        protocol.append("(!) VERIFICATION METHOD:")
        protocol.append("    - Use Ratiometric Voltage Imaging (CC2-DMPE / DiBAC4) at each checkpoint")
        protocol.append("    - Calculate Ratio = I_donor / I_acceptor")
        
        if biomarkers:
            protocol.append("")
            genetic_verification = self._generate_genetic_verification(biomarkers)
            for line in genetic_verification:
                protocol.append(line)
        
        protocol.append("")
        protocol.append("=" * 70)
        
        return "\n".join(protocol)

if __name__ == "__main__":
    compiler = BioCompiler()
    result_subroutine = compiler.find_subroutine(organ="eye", species="Xenopus laevis")
    
    if result_subroutine:
        lab_protocol = compiler.generate_protocol(result_subroutine)
        print(lab_protocol)
    else:
        print("[!] Error: No known bioelectric subroutine for this morphology.")
