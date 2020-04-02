from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('project2.html')

@app.route('/orders', methods =['POST'])
def write_orders():
   name_receive = request.form['name_give']
   count_receive = request.form['count_give']
   add_receive = request.form['add_give']
   call_receive = request.form['call_give']

   order = {
      'name': name_receive,
      'count': count_receive,
      'add': add_receive,
      'call': call_receive
   }

   db.orders.insert_one(order)

   return jsonify({'result': 'success', 'msg': '주문이 성공적으로 시행되었습니다.'})


@app.route('/orders')
def read_orders():

   orders = list(db.orders.find({}, {'_id': 0}))

   return jsonify({'result': 'success', 'msg': '주문을 조회하였습니다.', 'orders': orders})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)