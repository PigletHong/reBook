# =========================================================================
# linux 버전
# =========================================================================
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from pyvirtualdisplay import Display
# from bs4 import BeautifulSoup
# import config

# def getDynamicPage(url):
#     # linux 환경 가상 display 실행
#     display = Display(visible=0, size=(1920, 1080))
#     display.start()

#     caps = DesiredCapabilities().CHROME
#     caps["pageLoadStrategy"] = "none"  # Pageload Strategy 설정 변경
#     chrome_options = webdriver.ChromeOptions()  # 크롬 드라이버 실행
#     chrome_options.add_argument("headless")  # 크롬 드라이버 창 감추기
#     # driver = webdriver.Chrome(service=Service(
#     #     ChromeDriverManager().install()), options=chrome_options)  # 크롬 드라이버 자동 업데이트
#     driver = webdriver.Chrome(
#         config.chrome_driver_path, options=chrome_options)  # 크롬 드라이버 업데이트 없이 실행
#     driver.get(url)
#     # previous = driver.execute_script("return document.body.scrollHeight")
#     # interval = 1  # 인터벌 설정
#     return driver

# =========================================================================
# windows 버전
# =========================================================================
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup


def getDynamicPage(url):
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


def send_kyoboBook(url):
    driver = getDynamicPage(url)
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
    desc = soup.select_one('div.info_text.fw_bold').getText()
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
