import pytest, os
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Edge()
    driver.get("http://localhost/crud_web_app/index.php")
    yield driver
    driver.quit()

@pytest.fixture
def admin_account():
    return {'user': 'admin', 'pass': 'admin'}

@pytest.fixture
def user_account():
    return {'user': 'user', 'pass': '123'}

@pytest.fixture
def invalid_account():
    return {'user': 'invalid', 'pass': 'account'}

@pytest.fixture
def warning_login():
    return ['não existe','inválida']

@pytest.fixture
def search_list():
    return ['the', 'ring', 'it']

@pytest.fixture
def movie_data():
    return {
        'title': 'Snow White and the Huntsman',
        'description': 'A fearless princess teams up with the huntsman to confront the Evil.',
        'category': 'Fantasia',
        'poster': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'poster', 'snow_white_small.png')
    }
