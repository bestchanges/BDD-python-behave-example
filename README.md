Last run status: [![Last test Status](https://travis-ci.com/bestchanges/BDD-python-behave-example.svg?branch=master)](https://travis-ci.com/bestchanges/BDD-python-behave-example)

# BDD Python Behave Selenium Example
Пример реализации концепции Behavior Driven Development на Python во фреймворке Behave. 

Для демонстрации на [Python fwdays'19 online conference](https://fwdays.com/en/event/python-fwdays-online-conference)

## Вводная
Задача техники BDD состоит в том, чтобы наладить успешную коммуникацию между заказчиками, бизнес-аналитиками, программистами и тестерами на протяжении жизни всего проекта.

Для этого создан язык на котором в простой текстовой форме описывается ожидаемое поведение приложения, а затем через BDD фреймворк текст транслируется в программный код, который уже можно использовать для тестирования программного продукта.

Там, где применяется BDD требования к ПО превращаются в живой код, а тесты вместо языка программирования пишутся на простом человеческом языке.

В этом докладе на примере автоматизации тестирования веб-сайта будет показана работа фреймворка Behave для языка Python. 


# How to install

```bash
$ pip install pipenv --user
$ pipenv sync
``` 

# How to run
```bash
$ pipenv run behave 
$ pipenv run behave --tags="@wip"
$ pipenv run behave --tags="~@core"
$ HEADLESS=1 pipenv run behave
```


