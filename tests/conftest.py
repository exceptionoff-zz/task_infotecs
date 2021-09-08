import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def web_browser(chrome_options):
    # Запускаем браузер
    browser = webdriver.Chrome('chromedriver\\chromedriver.exe',
                               options=chrome_options)
    yield browser
    browser.quit()

@pytest.fixture
def chrome_options():
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument("no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=800,600")
    options.add_argument("incognito")
    return options

@pytest.fixture
def connected():
    from urllib import request
    try:
        request.urlopen('http://www.yandex.ru')
        return True
    except:
        return False

