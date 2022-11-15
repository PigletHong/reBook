from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
import config
app = Flask(__name__)

client = MongoClient(config.mongodb_url)
db = client.dbsparta


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


if __name__ == '__main__':
    app.run()
