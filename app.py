from pymongo import MongoClient
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
import config
from bestseller import send_bestseller
from newbooks import send_newbooks

app = Flask(__name__)
from pymongo import MongoClient

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


if __name__ == '__main__':
    app.run()
