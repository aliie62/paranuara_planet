from pymongo import MongoClient
from typing import List, Dict
import os

def _get_collection(collectionName:str):
    conn = MongoClient(os.environ.get('Mongo_URI'))
    db = conn[os.environ.get('Mongo_Database')]
    return db[collectionName]


def save_documents(collectionName: str,docs: List[Dict]):
    """This function saves a list of documents in the given collection name.
    Parameters:
               *collectionName
               *docs: List of documents to be saved. i.e. [{doc1}, {doc2}, ...]
    """
    collection = _get_collection(collectionName)
    result = collection.insert_many(docs).inserted_ids
    return {'inserted_ids': result}

def get_documents(collectionName: str,query:Dict={}) -> List[Dict]:
    """This function retrieves a list of documents from the given collection name by applying the query.
    Parameters:
               *collectionName
               *query: This parameter is optional. However, if it is provided, it should be in dictionary format
    """
    collection = _get_collection(collectionName)
    result = list(collection.find(query))
    return result

def get_one_document(collectionName: str,query:Dict={}) ->Dict:
    """This function retrieves a document from the given collection name by applying the query.
    Parameters:
               *collectionName
               *query: This parameter is optional. However, if it is provided, it should be in dictionary format
    """
    collection = _get_collection(collectionName)
    return collection.find_one(query)