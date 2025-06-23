from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login

def test_ui_redirect_buttons(browser, admin_account):
    login(browser, admin_account)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'btmenu'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'menu-admin-show'))
    )
    current_url = browser.current_url
    browser.find_element(By.ID, 'movie-register').click()
    WebDriverWait(browser, 5).until(
        EC.url_changes(current_url)
    )
    assert 'register' in browser.current_url.lower()

    current_url = browser.current_url
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'header-btn-search'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.url_changes(current_url)
    )
    assert 'search' in browser.current_url.lower()

    current_url = browser.current_url
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'header-btn-home'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.url_changes(current_url)
    )
    assert 'home' in browser.current_url.lower()
