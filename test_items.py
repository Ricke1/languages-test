import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pytest
import selenium
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form")

