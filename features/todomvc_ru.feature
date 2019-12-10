# language: ru
Функционал: будучи ленивым я хочу тестировать сайт todomvc.com автоматически

  Предыстория:
    Допустим пользователь открывает страницу http://todomvc.com/examples/react/

  Сценарий: создать новую задачу и убедиться что она добавлена
    Дано в списке нет задачи 'Моя первая задача'
    Когда пользователь добавляет задачу 'Моя первая задача'
    Тогда в списке есть задача 'Моя первая задача'
    К тому же задача 'Моя первая задача' не выполнена

  Сценарий: создать новую задачу и пометить её как выполненную
    Дано пользователь добавляет задачу 'К выполнению'

    Когда нажимает на чекбокс для задачи 'К выполнению'
    Тогда задача 'К выполнению' выполнена