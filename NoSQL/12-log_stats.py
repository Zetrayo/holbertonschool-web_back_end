#!/usr/bin/env python3


"""
This script provides statistics about Nginx logs stored in MongoDB.
"""


from pymongo import MongoClient


def get_nginx_stats():
    """
    Fetches statistics from the 'nginx' collection in the 'logs' database.
    """

    # Connect to MongoDB client
    client = MongoClient()

    # Access the 'logs' database and 'nginx' collection
    db = client.logs
    collection = db.nginx

    # Get total number of documents (logs)
    total_logs = collection.count_documents({})

    # Define the HTTP methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}

    # Count the documents for each HTTP method
    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})

    # Count the number of GET requests with path = /status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})

    # Output results in the required format
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    get_nginx_stats()
