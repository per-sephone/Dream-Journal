"""
Database init, can be updated to support other databases.
Currently supports sqlite3
"""

from .model_datastore import model

appmodel = model()

def get_model():
    return appmodel