#!/usr/bin/env python3


"""
This module contains a function to list all documents in a given MongoDB collection.
It returns all documents as a list or an empty list if no documents are found.
"""


def list_all(mongo_collection):
    """
    Lists all documents in the specified MongoDB collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection object.

    Returns:
    list: A list of all documents in the collection. Returns an empty list if no documents.
    """
    return list(mongo_collection.find())  # Convert the cursor to a list
