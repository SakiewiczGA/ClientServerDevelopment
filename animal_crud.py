import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:37448' % (username, password))
        self.database = self.client['AAC']
        

# Insert document
    def create(self, data):
                
        self.data = data      
       
        if self.data is not None:   
            self.database.animals.insert_one(self.data)
            return True  
                
        else:                
            return False

# Find documents
    def read(self, data):
        self.data = data
        if self.data is not None:
            return self.database.animals.find(data, {"_id":False})

        else:
            print("Nothing to Read")
            return False
           
        
            
# Update documents
    def update(self, data, newData):
        self.data = data
        self.newData = newData    
        if data is not None:
            return self.database.animals.update_many(self.data, {'$set' : self.newData}) 
        else:
            print("Nothing entered to change")
            return False  
                                                        
 

 #Delete documents
    def delete(self, data):
        self.data = data
        if self.data is not None:
        
            return self.database.animals.delete_many(self.data)
            print ("Records deleted")
            
        else:
            print("Nothing entered to delete")
            return False
                
        
        