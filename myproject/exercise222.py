from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

mv = db.movies.find_one({'title': '어벤져스: 엔드게임'})
star = mv['star']

same_star_movie = db.movies.update_many({'star': star}, {'$set': {'star': 0}})

##for mv in same_star_movie:
# title = mv['title']
# print(title)
# db.movies.update_one({'title': title}, {'$set': {'star': 0}}

