import pytest

from requests import get, post, put, delete

URL = 'http://localhost:5000'

@pytest.mark.parametrize('testcase, ans', [
    ({'username': 'account', 'nickname': 'validNickname'}, 200),
    ({'username': 'account', 'nickname': 'InvalidNickname'}, 400),
    ({'username': 'existedAccount', 'nickname': 'validNickname'}, 400),
    ({'username': 'existedAccount', 'nickname': 'InvalidNickname'}, 400),
])
def test_register(testcase, ans):
    resp = post(f'{URL}/users', json=testcase)
    assert resp.status_code == ans

@pytest.mark.parametrize('testcase, id_, ans', [
    ({'nickname': 'validNickname'}, 1,200),
    ({'nickname': 'InvalidNickname'}, 1,400),
    ({'nickname': 'validNickname'}, -1,400),
    ({'nickname': 'InvalidNickname'}, -1,400),
])
def test_update_user_info(testcase, id_, ans):
    resp = put(f'{URL}/users/id_', json=testcase)    
    assert resp.status_code == ans

# def test_read_all_user_info(testcase):
#    resp = get(f'{URL}/users', json=testcase)    
#    assert resp.status_code == ans

@pytest.mark.parametrize('id_, ans', [
    (1,200),
    (-1,400),
])
def test_read_one_user_info(id_, ans):
    resp = get(f'{URL}/users/{id_}')    
    assert resp.status_code == ans

@pytest.mark.parametrize('testcase, ans', [
    ({'username': 'account', 'password': 'correctPassword'}, 400),
    ({'username': 'account', 'password': 'incorrectPassword'}, 400),
    ({'username': 'existedAccount', 'password': 'correctPassword'}, 200),
    ({'username': 'existedAccount', 'password': 'incorrectPassword'}, 400),
])
def test_login(testcase, ans):
    resp = post(f'{URL}/login', json=testcase)    
    assert resp.status_code == ans

