Этот проект содержит в себе 3 теста:

_tests/test_internet_connection.py_
(тест на интернет соединение)
_tests/yandex_search/test_link_search.py::test_link_checking_Yandex_search_first_page_
(тест на нахождение определенной ссылки в результатах выдачи 1 страницы по определенному запросу)
_tests/yandex_search/test_link_search.py::test_link_checking_Yandex_search_all_pages_
(тест на нахождение определенной ссылки во всех результатах выдачи по определенному запросу)

Тест _tests/yandex_search/test_link_search.py::test_link_checking_Yandex_search_first_page_ на
тестовых данных, удовлетворяет Заданию.

В файле _tests/conftest.py_ содержаться фикстуры:
_web_browser_ - запускает браузер, и закрывает его после теста.
_chrome_options_ - перед запуском браузера задает его опции
_connected_ - возвращает True, если есть интернет соединение, инааче - False

В файле requirements.txt содержаться все заисимости данного проекта.