#!/usr/bin/env python3


"""
This module contains a function to find all schools that have a specific topic in their 'topics' field.
The function returns a list of schools that contain the given topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the specified topic in their 'topics' field.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
    topic (str): The topic to search for in the 'topics' field.

    Returns:
    list: A list of school documents that contain the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))  # Query schools where 'topics' contains the given topic
