import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()