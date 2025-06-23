import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login, search_movie

@pytest.mark.parametrize('account, expected', 
                         [('invalid_account', False), 
                          ('user_account', True)])
def test_login(browser,request, account, expected, warning_login):
    conta = request.getfixturevalue(account)
    get_home_url = browser.current_url
    login(browser, conta)
    if expected:
        WebDriverWait(browser, 5).until(EC.url_changes(get_home_url))
        assert 'home' in browser.current_url.lower()
    else:
        warning = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'aviso'))
        )
        assert any( mensage in warning.text for mensage in warning_login)

def test_search_movie(browser, user_account, search_list):
    login(browser, user_account)
    for search in search_list:
        search_movie(browser, search)
        WebDriverWait(browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'movie-list'))
        )
        movies = browser.find_elements(By.CLASS_NAME, 'card-title')
        assert any(search.lower() in movie.text.lower() for movie in movies)

@pytest.mark.parametrize('account, expected',
                        [('user_account', False),
                        ('admin_account', True)])
def test_show_admin_menu(browser, request, account, expected):
    account = request.getfixturevalue(account)
    login(browser, account)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'btmenu'))
    ).click()
    admin_menu = browser.find_elements(By.ID, 'movie-register')
    assert bool(admin_menu) == expected