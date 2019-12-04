import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import List
from data import save_documents

def update_foods(collectionName:str,docs:List):
    """This functions adds new food to the given collection name.
    Parameters:
               *collectionName: it could be either <vegetable> or <fruit>
               *docs: it is a list of new foods. It should be in this format:
                        [{"index":index_number1, "name": food_name1},
                        {"index":index_number2, "name": food_name2},
                        ...]
    """

if __name__ == "__main__":
    """Parameters:
        *collectionName: it could be either <vegetable> or <fruit>
        *docs: it is a list of new foods. It should be in this format:
                    [{"index":index_number1, "name": food_name1},
                    {"index":index_number2, "name": food_name2},
                    ...]
    """
    #Set collection name and foods list according to new findings
    result = save_documents('vegetable',[{"index":285, "name":"new_food"}])
    print(result)