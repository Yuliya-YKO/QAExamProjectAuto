import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()