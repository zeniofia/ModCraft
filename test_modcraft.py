# test_modcraft.py
"""
Tests for ModCraft module.
"""

import unittest
from modcraft import ModCraft

class TestModCraft(unittest.TestCase):
    """Test cases for ModCraft class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModCraft()
        self.assertIsInstance(instance, ModCraft)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModCraft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
