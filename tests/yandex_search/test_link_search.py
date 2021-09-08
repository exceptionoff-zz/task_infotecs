import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_data = [
    ('ViPNet Coordinator HW5000',
     'https://infotecs.ru/upload/iblock/db0/ViPNet_Coordinator_HW_5000_web_'
     'july_2018.pdf')
    ]

@pytest.mark.parametrize('search_query, desired_link', test_data)
def test_link_checking_Yandex_search_first_page(search_query, desired_link,
                                                web_browser):
    '''Тест проверка наличия ссылки на первой странице выдачи. '''
    # успешность теста
    success = None

    # Время ожидания появления элемента на странице
    wait_time = 5

    search_line_xpath = '//*[@id="text"]'
    btn_search_xpath = '//form/div/button'

    try:

        # Переходим на страницу
        web_browser.get('http://www.yandex.ru')

        # Строка поиска на 'http://www.yandex.ru'
        search_line = WebDriverWait(web_browser, wait_time).until(
            EC.presence_of_element_located((By.XPATH,
                                            search_line_xpath)))
        # Кнопка поиска на 'http://www.yandex.ru'
        btn_to_find = WebDriverWait(web_browser, wait_time).until(
            EC.presence_of_element_located((By.XPATH,
                                            btn_search_xpath)))

        # Вводим поисковый запрос
        search_line.send_keys(search_query)
        # Кликаем по кнопке
        btn_to_find.click()

        # Веб элементы со ссылками на результаты запроса:
        web_elements = WebDriverWait(web_browser, wait_time).until(
            EC.presence_of_all_elements_located((By.XPATH,
                                                 '//li/div/h2/a')))

        # Свойства 'href' у всех результатов запроса на тек.странице:
        href_s = [w_e.get_attribute('href') for w_e in web_elements]

        success = desired_link in href_s
        # Если искомая ссылка найдена, то открываем её в новой вкладке:
        if success:
            web_browser.execute_script(f"window.open('{desired_link}');")
    except TimeoutException as err:
        success = False
    except:
        success = False
    finally:
        assert success

@pytest.mark.parametrize('search_query, desired_link', test_data)
def test_link_checking_Yandex_search_all_pages(search_query, desired_link,
                                               web_browser):
    '''Тест поиск ссылки на всех страницах выдачи. '''
    # успешность теста
    success = None

    # Время ожидания появления элемента на странице
    wait_time = 5

    search_line_xpath = '//*[@id="text"]'
    btn_search_xpath = '//form/div/button'

    # Переходим на страницу
    web_browser.get('http://www.yandex.ru')

    # Строка поиска на 'http://www.yandex.ru'
    search_line = WebDriverWait(web_browser, wait_time).until(
        EC.presence_of_element_located((By.XPATH,
                                            search_line_xpath)))
    # Кнопка поиска на 'http://www.yandex.ru'
    btn_to_find = WebDriverWait(web_browser, wait_time).until(
        EC.presence_of_element_located((By.XPATH,
                                            btn_search_xpath)))

    # Вводим поисковый запрос
    search_line.send_keys(search_query)
    # Кликаем по кнопке
    btn_to_find.click()

    link_next_page_text = 'дальше'
    while True:
        try:
            # Веб элементы со ссылками на результаты запроса:
            web_elements = WebDriverWait(web_browser, wait_time).until(
                EC.presence_of_all_elements_located((By.XPATH,                                                         '//li/div/h2/a')))

            # Свойства 'href' у всех результатов запроса на тек.странице:
            href_s = [w_e.get_attribute('href') for w_e in web_elements]


            link_next_page = WebDriverWait(web_browser, wait_time).until(
                EC.presence_of_element_located((By.LINK_TEXT, link_next_page_text))
                )
            link_next_page.click()

            success = desired_link in href_s
            # Если искомая ссылка найдена, то открываем её в новой вкладке:
            if success:
                web_browser.execute_script(f"window.open('{desired_link}');")
                break

        except TimeoutException:
            success = False
            break
        except:
            success = False
            break

    assert success






