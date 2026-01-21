"""
Unit tests for the BioCompiler module
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from compiler.experiment_gen import BioCompiler


class TestBioCompiler(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.compiler = BioCompiler()
    
    def test_compiler_initialization(self):
        """Test that compiler initializes with database"""
        self.assertIsNotNone(self.compiler.library)
        self.assertIsInstance(self.compiler.library, list)
    
    def test_find_eye_subroutine(self):
        """Test finding the eye induction subroutine"""
        result = self.compiler.find_subroutine(organ="eye", species="Xenopus laevis")
        self.assertIsNotNone(result)
        self.assertEqual(result['target_morphology']['organ'], 'eye')
        self.assertEqual(result['target_morphology']['species'], 'Xenopus laevis')
    
    def test_find_tail_subroutine(self):
        """Test finding the tail regeneration subroutine"""
        result = self.compiler.find_subroutine(organ="tail", species="Xenopus laevis")
        self.assertIsNotNone(result)
        self.assertEqual(result['target_morphology']['organ'], 'tail')
        self.assertEqual(result['target_morphology']['action'], 'regenerate')
    
    def test_find_nonexistent_subroutine(self):
        """Test that nonexistent subroutines return None"""
        result = self.compiler.find_subroutine(organ="nonexistent", species="Fake Species")
        self.assertIsNone(result)
    
    def test_generate_protocol(self):
        """Test protocol generation"""
        subroutine = self.compiler.find_subroutine(organ="eye", species="Xenopus laevis")
        protocol = self.compiler.generate_protocol(subroutine)
        
        self.assertIsNotNone(protocol)
        self.assertIsInstance(protocol, str)
        self.assertIn("BIOELECTRIC COMPILER PROTOCOL", protocol)
        self.assertIn("PHASE 0: DEVELOPMENTAL CONTEXT", protocol) # Check for new phase
        self.assertIn("TARGET STATE DEFINITION", protocol)
        self.assertIn("HARDWARE SELECTION", protocol)
        self.assertIn("Ratiometric Voltage Imaging", protocol) # Check for updated verification advice
    
    def test_case_insensitive_search(self):
        """Test that search is case-insensitive"""
        result1 = self.compiler.find_subroutine(organ="EYE", species="xenopus laevis")
        result2 = self.compiler.find_subroutine(organ="eye", species="Xenopus laevis")
        
        self.assertEqual(result1['id'], result2['id'])


if __name__ == '__main__':
    unittest.main()
