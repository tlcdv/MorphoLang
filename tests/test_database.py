"""
Unit tests for database validation
"""

import unittest
import json
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestDatabaseIntegrity(unittest.TestCase):
    
    def setUp(self):
        """Load the database"""
        self.database_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'database',
            'database_seed.json'
        )
        
        with open(self.database_path, 'r') as f:
            self.database = json.load(f)
    
    def test_database_is_list(self):
        """Test that database is a list"""
        self.assertIsInstance(self.database, list)
    
    def test_database_not_empty(self):
        """Test that database contains entries"""
        self.assertGreater(len(self.database), 0)
    
    def test_all_entries_have_required_fields(self):
        """Test that all entries have required fields"""
        required_fields = ['id', 'metadata', 'target_morphology', 
                          'bioelectric_state', 'hardware_drivers']
        
        for entry in self.database:
            for field in required_fields:
                self.assertIn(field, entry, 
                            f"Entry {entry.get('id', 'unknown')} missing field: {field}")
    
    def test_unique_ids(self):
        """Test that all subroutine IDs are unique"""
        ids = [entry['id'] for entry in self.database]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate IDs found in database")
    
    def test_vmem_ranges_are_valid(self):
        """Test that Vmem ranges are properly formatted"""
        for entry in self.database:
            vmem_range = entry['bioelectric_state']['target_vmem_range']
            
            # Should be a list
            self.assertIsInstance(vmem_range, list, 
                                f"Entry {entry['id']}: Vmem range should be a list")
            
            # Should have 2 elements (if not special case like [0,0])
            self.assertEqual(len(vmem_range), 2, 
                           f"Entry {entry['id']}: Vmem range should have 2 values")
            
            # Both should be numbers
            for val in vmem_range:
                self.assertIsInstance(val, (int, float), 
                                    f"Entry {entry['id']}: Vmem values should be numbers")
    
    def test_hardware_drivers_not_empty(self):
        """Test that each entry has at least one hardware driver"""
        for entry in self.database:
            self.assertGreater(len(entry['hardware_drivers']), 0,
                             f"Entry {entry['id']}: Must have at least one hardware driver")


if __name__ == '__main__':
    unittest.main()
