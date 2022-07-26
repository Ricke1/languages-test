from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default=None,
                     help="Choose languages")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(user_language)
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser_name = request.config.getoption("browser_name")
    browser = None
    if user_language == "es":
        print("\nstart chrome browser for test with es language..")
        browser = webdriver.Chrome(options=options)
    elif user_language == "fr":
        print("\nstart chrome browser for test with fr language..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()