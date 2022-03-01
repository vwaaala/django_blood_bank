import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance
    """
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    yield browser
    browser.close()