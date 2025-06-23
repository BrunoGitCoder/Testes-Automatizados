from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(browser, user):
    user_input = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.NAME, 'user'))
    )
    user_input.clear()
    user_input.send_keys(user['user'])
    pass_input = browser.find_element(By.NAME, 'password')
    pass_input.clear()
    pass_input.send_keys(user['pass'])
    browser.find_element(By.CLASS_NAME, 'btn-login').click()

def search_movie(browser, movie):
    if not 'search' in browser.current_url:
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'header-btn-search'))
        ).click()
    search_input = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.NAME, 'search-text'))
    )
    search_input.clear()
    search_input.send_keys(movie)
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

def register_movie(browser, movie_data):
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, 'movie-register-form'))
    )
    browser.find_element(By.NAME, "title" ).send_keys(movie_data["title"])
    browser.find_element(By.NAME, "description" ).send_keys(movie_data["description"])
    browser.find_element(By.NAME, "category" ).send_keys(movie_data["category"])
    browser.find_element(By.NAME, "poster" ).send_keys(movie_data["poster"])
    browser.find_element(By.CLASS_NAME, "btn-save-movie").click()