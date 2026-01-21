"""
Unit tests for control loop functionality
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from compiler.experiment_gen import BioCompiler


class TestControlLoop(unittest.TestCase):
    
    def setUp(self):
        self.compiler = BioCompiler()
    
    def test_control_loop_in_protocol(self):
        """Test that control loop generates homeostatic maintenance phase"""
        subroutine = self.compiler.find_subroutine(organ="eye", species="Xenopus laevis")
        protocol = self.compiler.generate_protocol(subroutine)
        
        self.assertIn("PHASE 4: HOMEOSTATIC MAINTENANCE", protocol)
        self.assertIn("CLOSED-LOOP intervention", protocol)
        self.assertIn("Monitoring Schedule", protocol)
        self.assertIn("Feedback Decision Tree", protocol)
        self.assertIn("STOP CONDITIONS", protocol)
    
    def test_spatial_risk_warning(self):
        """Test that spatial mismatch triggers warning"""
        # Planaria uses systemic delivery on global network (should NOT warn)
        subroutine = self.compiler.find_subroutine(organ="head", species="Girardia dorotocephala")
        protocol = self.compiler.generate_protocol(subroutine)
        
        # This should NOT have a warning since bath application is appropriate for planaria
        self.assertNotIn("WARNING: GLOBAL REMODELING RISK", protocol)
    
    def test_monitoring_checkpoints_generated(self):
        """Test that monitoring timeline is generated"""
        subroutine = self.compiler.find_subroutine(organ="tail", species="Xenopus laevis")
        protocol = self.compiler.generate_protocol(subroutine)
        
        self.assertIn("T+0h:", protocol)
        self.assertIn("Baseline measurement", protocol)
        self.assertIn("Verify Vmem", protocol)


if __name__ == '__main__':
    unittest.main()
