import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.company import Company


class TestDataMethods(unittest.TestCase):
    def test_find_by_name(self):
        result = Company.find_by_name('assistix')
        self.assertEqual([result["company"], result["employees"][0]], ["ASSISTIX",{'index': 123, 'name': 'Riggs Daniel'}] ,'Should be None.')
    
if __name__ == '__main__':
    unittest.main()