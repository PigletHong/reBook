from pymongo import MongoClient
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
import config
from bestseller import send_bestseller
from newbooks import send_newbooks
from bookInfo import send_kyoboBook

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


@app.route('/api/review')
def create_review():
    url = request.form['url']
    content = request.form['content']
    tag = request.form['tag']

    bookInfo = send_kyoboBook(url)

    doc = {
        'url': url,
        'content': content,
        'tag': tag,
        'bookInfo': bookInfo,
    }

    db.review.insert_one(doc)

    return jsonify({'msg': '리뷰작성 완료!'})


if __name__ == '__main__':
    app.run()
