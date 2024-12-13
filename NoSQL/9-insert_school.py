#!/usr/bin/env python3


"""
This module contains a function to insert a new document into a MongoDB collection using kwargs.
The function returns the _id of the newly inserted document.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified MongoDB collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
    **kwargs: The fields and values to insert into the new document.

    Returns:
    ObjectId: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)  # Insert the document and get the result
    return result.inserted_id  # Return the _id of the newly inserted document
