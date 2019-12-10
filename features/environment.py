# Take from: https://github.com/StephenDavidson/python-bdd-behave/blob/master/features/environment.py
import time

from behave import fixture, use_fixture

from selenium.webdriver import Firefox


@fixture
def browser_firefox(context):
    print("Browser init")
    browser = Firefox()
    browser.implicitly_wait(1)

    context.browser = browser

    yield context.browser

    print("Browser cleanup")
    time.sleep(2)
    context.browser.quit()


def before_feature(context, arg):
    # use the same browser instance for all scenarios in the feature
    # if you want to run fresh browser session on each scenario put it in before_scenario()
    use_fixture(browser_firefox, context)
