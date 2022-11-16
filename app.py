from flask import Flask, render_template, request, jsonify
import config
import hashlib
import jwt
import datetime
from bestseller import send_bestseller
from newbooks import send_newbooks

SECRET_KEY = 'HONG'

app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient(config.mongodb_url)
db = client.rebook


@app.route('/')
def newbooks():
    data = send_newbooks()
    print(data)
    return render_template('newbooks.html', data=data)

@app.route('/bestseller')
def bestseller():
    data = send_bestseller()
    print(data)
    return render_template('bestseller.html', data=data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']


    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})

    if result is not None:

        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=120)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/join')
def join():
    return render_template('join.html')


@app.route('/api/join', methods=['POST'])
def api_join():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.user.insert_one({'id': id_receive, 'pw': pw_hash, 'name': name_receive})

    return jsonify({'result': 'success'})

@app.route('/api/name', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)

        userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success', 'name': userinfo['name']})
    except jwt.ExpiredSignatureError:

        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@app.route('/detail')
def detail():
    return render_template('detail.html')


if __name__ == '__main__':
    app.run()
