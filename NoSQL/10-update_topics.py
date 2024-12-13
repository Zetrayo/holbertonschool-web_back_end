#!/usr/bin/env python3


"""
This module contains a function to update the 'topics' field of a school document in a MongoDB collection.
The function updates the topics of the school based on the name of the school.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a school document in the collection based on the school's name.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
    name (str): The name of the school whose topics need to be updated.
    topics (list): A list of strings representing the new topics to be assigned to the school.

    Returns:
    None: This function does not return a value. It modifies the document in the collection.
    """
    mongo_collection.update_many(
        {"name": name},  # Find the school by its name
        {"$set": {"topics": topics}}  # Set the new topics
    )
