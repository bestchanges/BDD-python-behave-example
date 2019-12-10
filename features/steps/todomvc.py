import json
from typing import List, Optional

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def find_tasks(browser: WebDriver) -> List[WebElement]:
    elements = browser.find_elements_by_xpath(f'//ul[@class="todo-list"]/*')
    return elements


def find_task_by_name(browser: WebDriver, task_name) -> Optional[WebElement]:
    """
    find tag label with the task text in it
    :return: outer li tag
    """
    found_li = browser.find_element_by_xpath(f'//label[text()="{task_name}"]/../..')
    return found_li


def get_complete_control_for_task_li(task_li):
    return task_li.find_element_by_xpath(f'//label[text()="{task_li.text}"]/preceding-sibling::input')


def get_task_completed(task_li: WebElement):
    return task_li.get_attribute('class')


@step("list of tasks is empty")
def step_impl(context):
    tasks = find_tasks(context.browser)
    assert len(tasks) == 0


@step("user add task '{task_name}'")
@step("пользователь добавляет задачу '{task_name}'")
def add_task(context, task_name):
    browser: WebDriver = context.browser
    input = browser.find_element_by_xpath("//input[@class='new-todo']")
    input.send_keys(task_name)
    input.send_keys(Keys.RETURN)


@step("there is todo-item '{task_name}' in the list")
@step("в списке есть задача '{task_name}'")
def step_impl(context, task_name):
    task = find_task_by_name(context.browser, task_name)
    assert task


@step("пользователь открывает страницу {url}")
@step("user opens webpage {url}")
def step_impl(context, url):
    browser: WebDriver = context.browser
    browser.get(url)


@step("there are no todo-item '{task_name}' in the list")
@step("в списке нет задачи '{task_name}'")
def step_impl(context, task_name):
    try:
        task = find_task_by_name(context.browser, task_name)
    except NoSuchElementException:
        return
    raise Exception()


@step("нажимает на чекбокс для задачи '{task_name}'")
@when("click checkbox for task '{task_name}'")
def complete_task(context, task_name):
    task = find_task_by_name(context.browser, task_name)
    checkbox = get_complete_control_for_task_li(task)
    checkbox.click()


@step("task '{task_name}' {state}")
@step("задача '{task_name}' {state}")
def step_impl(context, task_name, state):
    task = find_task_by_name(context.browser, task_name)
    if state in ['is completed', 'выполнена']:
        assert task.get_attribute('class') == 'completed'
    elif state in ['is not completed', 'не выполнена']:
        assert task.get_attribute('class') != 'completed'
    else:
        assert False, f"Unknown state: {state}"


@step("there are todo-items in the list")
def step_impl(context):
    for row in context.table:
        task_name = row['taskname']
        add_task(context, task_name)
        if row['completed'].lower() == 'true':
            complete_task(context, task_name)


@step("there are todo-items loaded from json")
def step_impl(context):
    text = context.text
    assert text
    json_data = json.loads(text)
    for row in json_data:
        task_name = row['taskname']
        add_task(context, task_name)
        if row['completed']:
            complete_task(context, task_name)
