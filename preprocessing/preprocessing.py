import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import re
from data import get_documents, get_one_document, save_documents
import json
from bson.son import SON

def check_foods(people):
    """This function is to chexk if there is any new food that we do not have it
    in neither vegetable nor fruit collections in the database.
    """
    #Initialise a set to store all foods
    foods = set()  
    for person in people:
        foods.update(set(person['favouriteFood']))
    foods_tuned = [food.lower().strip() for food in foods]
    
    #Check if there is any food not found in the database
    new_foods = []
    for food in foods_tuned:
        if not (get_one_document('vegetable',{"name":food}) or get_one_document('fruit',{"name":food})):
            new_foods.append(food)
    if len(new_foods) > 0:
        with open('new_foods.txt','w') as f:
            f.writelines('\n'.join(new_foods))
        return False
    else:
        return True

def process_people(people):
    for person in people:
            #Define username for each person based their email address
            username = re.findall("(.+)@.+",person["email"])[0]
            person["username"] = username

            #Split up favourite food list to vegetables and fruits and droping favouriteFood key
            vegetables = []
            fruits = []
            favourite_foods = person["favouriteFood"]
            for food in favourite_foods:
                veggie_db = get_one_document('vegetable',{"name":food})
                if veggie_db:
                    vegetables.append(SON([("index",veggie_db["index"])]))
                else:
                    fruit_db = get_one_document('fruit',{"name":food})
                    fruits.append(SON([("index",fruit_db["index"])]))
            person["vegetables"] = vegetables
            person["fruits"] = fruits
            person.pop("favouriteFood")
            #Format friends item using SON
            friends = [SON([("index", friend['index'])]) for friend in person['friends']]
            person['friends'] = friends
    result = save_documents('people',people)
    return result

def process_companies(companies):
    pass

if __name__ == "__main__":
    pass
    #Loads json files
    with open('files/people.json','r') as f:
        people = json.load(f)
    if not check_foods(people):
        print("New food(s) has been found.")
        print("Please check <new_foods.txt> file in the project folder for more information.")
        print("You should update <vegetable> or <fruit> collection in the database using <update_foods.py> script.")
        print("You can find this script in the <preprocessing> folder under project folder.")
    else:
        process_people(people)
        print("People data imported to the database.",'\n')
        with open('files/companies.json','r') as f:
            companies = json.load(f)
        save_documents('company',companies)
        print("Companies data imported to the database.")
        
 