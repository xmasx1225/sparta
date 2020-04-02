from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/reviews', methods =['POST'])
def write_reviews():
   title_receive = request.form['title_give']
   author_receive = request.form['author_give']
   review_receive = request.form['review_give']

   review = {
      'title': title_receive,
      'author': author_receive,
      'review': review_receive
   }

   db.reviews.insert_one(review)

   return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/reviews')
def read_reviews():

   reviews = list(db.reviews.find({}, {'_id': 0}))

   return jsonify({'result': 'success', 'msg': '리뷰를 조회하였습니다.', 'reviews':reviews})

if __name__ == '__main__':
