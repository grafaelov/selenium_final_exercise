import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language",
                    action="store",
                    default="en",
                    help="Choose language")
    parser.addoption('--browser_name',
                    action='store',
                    default="chrome",
                    help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nStart Chrome browser.")
        options = Options()
        # Класс.Метод указывающий выбранный в парамете язык.
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nStart Firefox browser.")
        fp = webdriver.FirefoxProfile()
        # Класс.Метод указывающий выбранный в парамете язык.
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuit browser.")
    browser.quit()

@pytest.fixture(scope="session")
def language(pytestconfig):
    return pytestconfig.getoption("language")
