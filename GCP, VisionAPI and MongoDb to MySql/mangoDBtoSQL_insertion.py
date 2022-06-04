import pymongo
import MySQLdb
import mysql.connector as c
print ("pymongo version:", pymongo.version)

# import the MongoClient class
from pymongo import MongoClient

# build a new client instance for MongoDB passing
# the string domain and integer port to the host parameters
mongo_client = MongoClient('localhost', 27017)
#storing the mangoclient host information tp host_info varible
host_info = mongo_client['HOST']
#printing the containt of host_info
print ("\nhost:", host_info) 
#making reference pointing to LibraryDB(database in MongoDB)
db_mongo=mongo_client.LibraryDB
#making a refernce pointing to mongoDB book collection
collection=db_mongo.Book
#making a connection between python and mysql
db_sql=c.connect(host="localhost",user="root",passwd="root",database="Librarydb",auth_plugin='mysql_native_password')
#checkinfg connection is established or not
if db_sql.is_connected():
     print("Successfully connected")
else:
     print("Not connected") 
# making a cursor for mysql
cursor_mysql = db_sql.cursor()
#loop
while True:
    mongo_cursor = db_mongo.Book.watch()
    mongo_document = next(mongo_cursor)
    mongo_docs = [mongo_document['fullDocument']]
    
    for data in mongo_docs:
        cursor_mysql.execute("INSERT INTO Book (ISBN, Accession_No, Title, Author, Publisher, Edition, Yr, category, Total_no_pages, Price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)""",(data['ISBN'], data['Accession_No'], data['Title'], data['Author'], data['Publisher'], data['Edition'], data['Year_of_publication'], data['Category'], data['Total_no_pages'], data['Price']))
    
    db_sql.commit()