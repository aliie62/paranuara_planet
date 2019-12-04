"""I could use aggregate method for MongoDB to do a cleaner join. However, for the sake of simplicity
 and speed of delivery, I used a basic method.
"""
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data import get_one_document, save_documents, get_documents

class Person(object):
    
    @staticmethod
    def find_by_username(username:str):
        person = get_one_document('people',{'username':username})
        if person:
            fruit_ids = [item['index'] for item in person["fruits"]]
            vegetable_ids = [item['index'] for item in person['vegetables']]
            fruit_docs = get_documents('fruit',{'index':{'$in':fruit_ids}})
            fruits = [fruit['name'] for fruit in fruit_docs]
            vegetable_docs = get_documents('vegetable',{'index':{'$in':vegetable_ids}})
            vegetables = [vegetable['name'] for vegetable in vegetable_docs]
            person['fruits'] = fruits
            person['vegetables'] = vegetables
            return {"username":person["username"],"age":person["age"],"fruits":person["fruits"],"vegetables":person["vegetables"]}
        else:
            return person

    @staticmethod
    def find_by_username2(username:str):
        person = get_one_document('people',{'username':username})
        if person:
            fruit_ids = [item['index'] for item in person["fruits"]]
            vegetable_ids = [item['index'] for item in person['vegetables']]
            fruit_docs = get_documents('fruit',{'index':{'$in':fruit_ids}})
            fruits = [fruit['name'] for fruit in fruit_docs]
            vegetable_docs = get_documents('vegetable',{'index':{'$in':vegetable_ids}})
            vegetables = [vegetable['name'] for vegetable in vegetable_docs]
            person['fruits'] = fruits
            person['vegetables'] = vegetables
            return {"username":person["username"],"age":person["age"],"fruits":person["fruits"],"vegetables":person["vegetables"]}
        else:
            return person
    
    @staticmethod
    def find_two(username1:str, username2:str):
        person1 = get_one_document('people',{'username':username1})
        person2 = get_one_document('people',{'username':username2})
        if person1 and person2:
            friend_ids = [friend['index'] for friend in person1["friends"]]
            friend_ids2 = [friend['index'] for friend in person2["friends"]]
            friend_ids.extend(friend_ids2)
            freinds_id = list(set(friend_ids))
            friends_docs = get_documents('people',{'$and':[{'index':{'$in':freinds_id}}, {'eyeColor':'brown'}, {"has_died":False}]})
            friends = [friend['name'] for friend in friends_docs]
            return {
                "person_1":{"name":person1['name'], "age":person1['age'], "address":person1['address'], "phone":person1['phone']},
                "person_2":{"name":person2['name'], "age":person2['age'], "address":person2['address'], "phone":person2['phone']},
                "friends": friends
                }
        else:
            return None