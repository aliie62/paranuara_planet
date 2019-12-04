import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from data import _get_collection,save_documents,get_documents, get_one_document


class TestDataMethods(unittest.TestCase):
    def test_connection(self):
        self.assertEqual(_get_collection('vegetable').name,'vegetable','Should be "vegetable".')
    
    def test_get_documents(self):
        self.assertEqual(len(get_documents('vegetable')), 243,'Should be "243".')
    
    def test_get_one_document(self):
        self.assertEqual(get_one_document('vegetable',{"index":1})['index'],1,'Should be "1".')

    def test_save(self):
        save_documents('vegetable',[{"index":244,"name":"test_veggie"}])
        self.assertEqual(get_documents('vegetable',{"index":244})[0]['name'],'test_veggie','Should be "test_veggie".')

if __name__ == '__main__':
    unittest.main()