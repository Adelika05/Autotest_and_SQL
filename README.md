# Autotest_and_SQL
# Проект для тестирования API  Yandex САМОКАТ
Этот проект содержит тесты на создание клиентом заказа и получение данных о казаке по номеру трека.
Проверяется:
  1. Выполнить запрос на создание заказа.
  2. Сохранить номер трека заказа.
  3. Выполнить запрос на получения заказа по треку заказа.
  4. Проверить, что код ответа равен 200


## Запуск тестов

Для запуска тестов необходимо установить:

библиотеку pytest: **_pip install pytest_**

Пакет requests: **_pip install requests_**

Запустить тесты можно командой: **_pytest_**


## Содержимое проекта

* _configuration.py_ - файл с базовым URL для запросов
* _data.py_ - файл с данными для запросов
* _sender_stand_request.py_ - файл с функцией для отправки запросов
* _create_kit_name_kit_test.py_ - файл с тестами для создания набора
* _README.md_ - файл с описанием проекта и инструкцией для запуска тестов
* _.gitignore_ - файл со списком файлов и каталогов, которые не должны попадать в репозиторий
