# Example Python Code to Insert a Document 
# Edited by Daniel Zawicki 5 Apr 2026

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): # Added username and password parameters, passed through by user
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        # USER = 'aacuser'    removed hard-coded username, commented for reference
        # PASS = '1234'       removed hard-coded password, commented for reference
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    
    ################## CRUD Methods ##################
    ##### Create #####
    # Insert a document into MongoDB
    def create(self, data):
        if data is not None and isinstance(data, dict):  # validate data as dict
            try:
                self.collection.insert_one(data)   # attempt to insert
                return True                              # True if successful
            except Exception as e:
                print(f"Insert failed: {e}")             # Exception if failed
                return False                             # False if failed
        else:                                            # if data is None or not dict
            print("Insert failed: data is empty or not a dictionary.")
            return False    # False if data is None or is not dict

    ##### Read #####
    # Query documents from MongoDB
    def read(self, query):
        if query is not None and isinstance(query, dict): # validate data as dict
            try: 
                cursor = self.collection.find(query)      # cursor points to respective data
                return list(cursor)                       # Return listed data
            except Exception as e:
                print(f"Query failed: {e}")               # Exception if failed
                return []                                 # Return empty list if failed
        else:                                             # if query is None or not dict
            print("Query failed: query is empty or not a dictionary.")
            return []  # Return empty list if failed
        
    ##### Update #####
    # Update documents in MongoDB
    def update(self, query, new_values):
        if (query is not None and isinstance(query, dict) and            # validate data as dict
            new_values is not None and isinstance(new_values, dict)):    # validate new data as dict
            try:
                result = self.collection.update_one(query, {"$set": new_values})  # modifies query with new values
                return result.modified_count    # returns number of modified documents
            except Exception as e:              
                print(f"Update failed: {e}")    # Exception if failed
                return 0                        # Return zero if failed
        else:
            print("Update failed: query or new_values is empty or not a dictionary.")  
            return 0    # return zero if data is None or is not dict
    
    ##### Delete #####
    # Delete documents in MongoDB
    def delete(self, query):
        if query is not None and isinstance(query, dict):  # validate data as dict
            try:
                result = self.collection.delete_one(query) # delete query
                return result.deleted_count                # return number of deleted documents
            except Exception as e:
                print(f"Delete failed: {e}")               # exception if failed
                return 0                                   # return zero if failed
        else:
            print("Delete failed: query is emtpy or not a dictionary.")    
            return 0    # return zero if data is None or is not dict