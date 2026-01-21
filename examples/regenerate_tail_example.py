"""
Example: Regenerate Tail in Xenopus laevis

This example demonstrates how to use MorphoLang to generate a protocol
for rescuing tail regeneration in a refractory period context.
"""

import sys
import os

# Add parent directory to path to import morpholang modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from compiler.experiment_gen import BioCompiler

def main():
    print("=" * 60)
    print("MorphoLang Example: Tail Regeneration")
    print("=" * 60)
    print()
    
    # Initialize the bioelectric compiler
    compiler = BioCompiler()
    
    # Search for the tail regeneration subroutine
    print("Searching for 'tail' regeneration subroutine in 'Xenopus laevis'...")
    print()
    
    subroutine = compiler.find_subroutine(organ="tail", species="Xenopus laevis")
    
    if subroutine:
        # Generate the experimental protocol
        protocol = compiler.generate_protocol(subroutine)
        print(protocol)
    else:
        print("[!] Error: No bioelectric subroutine found for this morphology.")

if __name__ == "__main__":
    main()
