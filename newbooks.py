from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

url = "https://product.kyobobook.co.kr/new/"

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none" #Pageload Strategy 설정 변경
chrome_options = webdriver.ChromeOptions() #크롬 드라이버 실행
chrome_options.add_argument("headless") #크롬 드라이버 창 감추기
driver = webdriver.Chrome(options=chrome_options) #크롬 드라이버 업데이트 없이 실행
driver.get(url)


def crawling_newbooks():
    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all("li", attrs={"class": "prod_item"})
    extract = []
    count = 0

    try :
        for item in items:
            if count < 20:

                img = item.find("img")["src"]
                # print(img)

                title = item.find("span", attrs={"class": "prod_name"}).text
                # print(title)

                author = item.find("span", attrs={"class": "prod_author"}).text
                # print(author)

                price = item.find("span", attrs={"class": "val"}).text
                # print(price)

                desc = item.find("p", attrs={"class": "prod_introduction"}).text
                # print(desc)

                star = item.find("span", attrs={"class": "review_klover_text font_size_xxs"}).text
                # print("*")


                doc = {'title': title,
                       'price': price,
                       'author': author,
                       'img': img,
                       'desc': desc,
                       'star': star}

                extract.append(doc)

                count = count + 1




    except Exception:
        pass

    return extract


def send_newbooks():
    extract = crawling_newbooks()
    return extract