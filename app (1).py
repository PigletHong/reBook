from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
import config

app = Flask(__name__)

client = MongoClient(config.mongodb_url)

db = client.sparta


@app.route('/')
def newbooks():
    return render_template('newbooks.html')


@app.route('/bestseller')
def bestseller():
    return render_template('bestseller.html')


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


@app.route('/api/comment', methods=['POST'])
def cmt_write():
    return jsonify()

@app.route('/api/comment', methods=['GET'])
def cmt_get():
    return jsonify()

@app.route('/api/comment', methods=['POST'])
def review_update():






    if __name__ == '__main__':
        app.run()
