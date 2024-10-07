import json
import pytest
from src.main import app
from src.DAL_Controller import database

TEST_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/ask_gpt_test'


@pytest.fixture
def test_client():
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='function', autouse=True)
def Before_each():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/ask_gpt_test'
    with app.app_context():
        database.create_all()  # create tables for each test
    yield


@pytest.fixture(scope='function', autouse=True)
def teardown_database():
    yield
    with app.app_context():
        database.drop_all()  # drop all tables after each test

def test_ask_success(test_client):
    response = test_client.post('/ask', json={'question': 'how are you?'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'question' in data
    assert 'answer' in data

def test_ask_fail(test_client):
    response = test_client.post('/ask', json={'no_question': 'nothing'})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert  'No question provided' in data['error']

def test_ask_fail_2(test_client):
    response = test_client.post('/ask', json={'question': ''})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert  'No question provided' in data['error']
