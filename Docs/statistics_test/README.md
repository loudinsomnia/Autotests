# Запуск тестирования
Прежде чем запускать тесты необходимо установить  
***Selenium Webdriver***\
[Скачать вебдрайвер можно здесь](https://chromedriver.chromium.org/downloads) и указать его в переменной PATH внутри файла statistics_report.py<br>
Так же необходимо установить все зависимости из 
***requirment.txt.***

Для установки зависимости из файла необходимо в командной строке написать\
`pip install -r requirment.txt`\
Данный тест предназначен, для проверка отображения страниц статистик

для запуска тестов необходимо в терминале написать \
`pytest -s -v statistics_test.py`

для вывода при тестировании только short summary \
`pytest -s -v --tb=no statistics_test.py`

для тестирования предусмотрены параметры запуска, порт тестового стенда, время ожидания прогрузки CRM системы

для выбора конкретного порта в командной строке указывает дополнительный параметр  
`--port=Необходимый порт`  
по дефолту пустой

для выбора конкретного хоста в командной строке указывает дополнительный параметр  
`--host=URL тестируемого объекта`  
по дефолту crm.fm-tst.com URL

для выбора конкретного времени ожидания в командной строке указывает дополнительный параметр  
`--time=Время ожидания`  
по дефолту 60 секунд

Можно указать оба параметра вместе, при этом команда для запуска тестирования будет выглядить так:  
`pytest -s -v statistics_test.py --port=Порт тестового стенда --time=Время ожидания прогрузки CRM`

Для быстрого и короткого описания ошибок  
`pytest -q statistics_report.py`

Вывод ошибок при тестировании, происходит после выполнения всех тестов