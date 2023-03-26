import pymongo

client = pymongo.MongoClient("mongodb+srv://sachintest:Sachintest1!@cluster0.2vr4s.mongodb.net/?retryWrites=true&w=majority")
db = client.test

dblist = client.list_database_names()
if "test" in dblist:
    print("The database exists.")
else:
    print("The database does not exists, please check")
    collection = db.tst