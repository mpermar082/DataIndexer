# test_dataindexer.py
"""
Tests for DataIndexer module.
"""

import unittest
from dataindexer import DataIndexer

class TestDataIndexer(unittest.TestCase):
    """Test cases for DataIndexer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataIndexer()
        self.assertIsInstance(instance, DataIndexer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataIndexer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
