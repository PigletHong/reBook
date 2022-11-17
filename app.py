from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
from kyoboCrawler import send_bestseller, send_newbooks, send_kyoboBook
import datetime
import config

app = Flask(__name__)

client = MongoClient(config.mongodb_url)
db = client.dbsparta


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


@app.route('/join')
def join():
    return render_template('join.html')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@app.route('/detail')
def detail():
    return render_template('detail.html')

# ============================================
# api call
# ============================================


@app.route('/api/review', methods=["POST"])
def create_review():
    # id_receive = request.form['id_give']
    url_receive = request.form['url_give']
    content_receive = request.form['content_give']
    tag_receive = request.form['tag_give']

    bookInfo = send_kyoboBook(url_receive)
    # 현재 시간 포멧 2022-11-17
    pubDate = datetime.datetime.now().strftime("%Y-%m-%d")

    doc = {
        'url': url_receive,
        'content': content_receive,
        'tag': tag_receive,
        'bookInfo': bookInfo,
        'pubDate': pubDate,
    }

    db.review.insert_one(doc)

    return jsonify({'msg': '리뷰작성 완료!'})


if __name__ == '__main__':
    app.run()
