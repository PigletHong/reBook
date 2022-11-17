# =========================================================================
# linux 버전
# =========================================================================
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from pyvirtualdisplay import Display
# from bs4 import BeautifulSoup
# import config


# def get_driver(url):
#     # linux 환경 가상 display 실행
#     display = Display(visible=0, size=(1920, 1080))
#     display.start()
#     caps = DesiredCapabilities().CHROME
#     caps["pageLoadStrategy"] = "none"  # Pageload Strategy 설정 변경
#     chrome_options = webdriver.ChromeOptions()  # 크롬 드라이버 실행
#     chrome_options.add_argument("headless")  # 크롬 드라이버 창 감추기
#     driver = webdriver.Chrome(
#         config.chrome_driver_path, options=chrome_options)  # 크롬 드라이버 업데이트 없이 실행
#     driver.get(url)
#     return driver

# =========================================================================
# windows 버전
# =========================================================================
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup


def get_driver(url):
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"  # Pageload Strategy 설정 변경
    chrome_options = webdriver.ChromeOptions()  # 크롬 드라이버 실행
    chrome_options.add_argument("headless")  # 크롬 드라이버 창 감추기
    driver = webdriver.Chrome(options=chrome_options)  # 크롬 드라이버 업데이트 없이 실행
    driver.get(url)

    return driver

# =========================================================================
# 공용 함수
# =========================================================================


def get_kyoboBook(url):
    driver = get_driver(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    title = soup.select_one(
        'div.auto_overflow_contents > div > h1 > span').getText()
    price = soup.select_one(
        'div.prod_price_box > div > span.price > span').getText()
    img = soup.select_one('div.portrait_img_box.portrait > img')['src']
    author = soup.select_one(
        'div.prod_author_box.auto_overflow_wrap > div.auto_overflow_contents > div > div > a').getText()
    publisher = soup.select_one(
        'div.prod_info_text.publish_date > a').getText()
    pubDate = soup.select_one('div.prod_info_text.publish_date').getText()
    # pubDate 가공
    pubDate = pubDate.replace(" ", "").replace(
        "\n", "").split("·")[1].replace("출시", "")
    desc = soup.select_one('div.info_text').getText()
    # longDesc = soup.select_one( 'div.intro_bottom > div:nth-of-type(2)').getText()  # 긴 책 설명
    return {
        'title': title,
        'price': price,
        'img': img,
        'author': author,
        'publisher': publisher,
        'pubDate': pubDate,
        'desc': desc,
    }


def send_kyoboBook(url):
    kyoboBook = get_kyoboBook(url)
    return kyoboBook

# lazy loading img 처리 필요 / db 저장 필요


def get_newbooks(url):
    driver = get_driver(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all("li", attrs={"class": "prod_item"})
    extract = []
    try:
        for idx, item in enumerate(items):
            # 20개 아이템만 크롤링
            if idx >= 20:
                break
            img = item.find("img")["src"]
            url = item.find("a", attrs={"class": "prod_info"})['href']
            title = item.find("span", attrs={"class": "prod_name"}).text
            author = item.find("span", attrs={"class": "prod_author"}).text
            price = item.find("span", attrs={"class": "val"}).text
            desc = item.find("p", attrs={"class": "prod_introduction"}).text
            star = item.find(
                "span", attrs={"class": "review_klover_text font_size_xxs"}).text
            doc = {
                'title': title,
                'price': price,
                'author': author,
                'img': img,
                'desc': desc,
                'star': star,
                'url': url,
            }
            extract.append(doc)
    except Exception:
        pass
    print('신상품 크롤링 완료!')
    return extract


def send_newbooks():
    url = "https://product.kyobobook.co.kr/new/"  # 기존 신상품 페이지 사용
    newbook = get_newbooks(url)
    return newbook

# lazy loading img 처리 필요 / db 저장 필요


def get_bestseller(url):
    driver = get_driver(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all("li", attrs={"class": "prod_item"})
    extract = []
    try:
        for idx, item in enumerate(items):
            img = item.find("img")["src"]
            url = item.find("a", attrs={"class": "prod_info"})['href']
            title = item.find("span", attrs={"class": "prod_name"}).text
            author = item.find("span", attrs={"class": "prod_author"}).text
            price = item.find("span", attrs={"class": "val"}).text
            desc = item.find("p", attrs={"class": "prod_introduction"}).text
            star = item.find(
                "span", attrs={"class": "review_klover_text font_size_xxs"}).text
            doc = {
                'rank': idx+1,
                'title': title,
                'price': price,
                'author': author,
                'img': img,
                'desc': desc,
                'star': star,
                'url': url,
            }
            extract.append(doc)
    except Exception:
        pass
    print('베스트셀러 크롤링 완료!')
    return extract


def send_bestseller():
    # 일간에서 주간 베스트셀러로 URL로 변경
    url = "https://product.kyobobook.co.kr/bestseller/total?period=002"  # 종합주간베스트
    bestseller = get_bestseller(url)
    return bestseller
