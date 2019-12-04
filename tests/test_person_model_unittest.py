import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.person import Person


class TestDataMethods(unittest.TestCase):
    def test_find_by_username1(self):
        self.assertEqual(Person.find_by_username('ali'), None ,'Should be None.')
    
    def test_find_by_username2(self):
        person = Person.find_by_username('noreenhuffman')
        self.assertEqual(person, {"username":"noreenhuffman","age":22,"fruits":['banana'],"vegetables":["beetroot","celery","cucumber"]} ,'Should be the same.')
    
    def test_find_two(self):
        username1 = 'deckermckenzie'
        username2 = 'bonniebass'
        self.assertEqual(Person.find_two(username1,username2),
                        {
                "person_1":{"name":"Decker Mckenzie", "age": 60, "address":"492 Stockton Street, Lawrence, Guam, 4854", "phone":"+1 (893) 587-3311"},
                "person_2":{"name":"Bonnie Bass", "age":54, "address":"455 Dictum Court, Nadine, Mississippi, 6499", "phone":"+1 (823) 428-3710"},
                "friends": ["Decker Mckenzie"]
                },
                'Should be the same.')


if __name__ == '__main__':
    unittest.main()