#!/usr/bin/env python3
"""a Python function that lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    list all mongo  collection.
    """

    return [list_doc for list_doc in mongo_collection.find()]
