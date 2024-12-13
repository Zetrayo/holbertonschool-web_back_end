#!/usr/bin/env python3


"""
This script provides statistics about Nginx logs stored in a MongoDB collection.
It displays the total number of logs, counts for each HTTP method, and the number of status checks.
"""


from pymongo import MongoClient

def main():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    # Count the total number of logs in the collection
    total_logs = collection.count_documents({})

    # Print the total number of logs
    print(f"{total_logs} logs")

    # List of HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    # Print the methods and the number of occurrences
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Count the number of logs where method=GET and path=/status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    main()
