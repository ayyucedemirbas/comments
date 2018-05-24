import pymongo
import sys
from pymongo import MongoClient


def main():
   
    connection = MongoClient("your_mongodb_URI") 
    
    db = connection.hepsiburada #your db name instead of 'hepsiburada'
    people = db.hepsiburada     #your db name instead of 'hepsiburada'
    f = open('/home/ayyuce/Desktop/ex.txt')  # open a file
    text = f.readline() 
    while text:
        
        content={"file_name": "/home/ayyuce/Desktop/ex.txt", "contents" : text }

            
        people.insert(content)
        text = f.readline()
   
    
    

if __name__ == '__main__':
    main()
