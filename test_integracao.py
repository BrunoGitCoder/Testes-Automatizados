from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login, search_movie, register_movie

def test_movie_register(browser, admin_account, movie_data):
    login(browser, admin_account)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'btmenu'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'menu-admin-show'))
    )
    browser.find_element(By.ID, 'movie-register').click()
    register_movie(browser, movie_data)
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'movie-register-success'))
    )
    search_movie(browser, movie_data['title'])
    WebDriverWait(browser, 5).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'movie-list'))
    )
    movie = browser.find_element(By.CLASS_NAME, 'card-title')
    assert movie_data['title'] in movie.text

def test_movie_delete(browser, admin_account, movie_data):
    login(browser, admin_account)
    search_movie(browser, movie_data['title'])
    WebDriverWait(browser, 5).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'movie-list'))
    )
    movie = browser.find_element(By.CLASS_NAME, 'card-title')
    movie.click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn-crud'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'btn-show-delete-confirm'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn-confirm'))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'movie-register-success'))
    )
    search_movie(browser, movie_data['title'])
    warning_not_found = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'search-null'))
    )
    assert 'nenhum filme' in warning_not_found.text.lower()
