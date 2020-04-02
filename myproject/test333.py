from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

all_users = list(db.users.find())

same_ages = list(db.users.find({'age': 21}))

person = db.users.find_one({'name': 'bobby'})

print(person)
