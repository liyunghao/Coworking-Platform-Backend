import pytest

from requests import get, post, put, delete

# E2E testing
# Input space partitioning

# `/create`: userid(C1: is admin or not), 其餘 Variable(C2: Is valid or Not)
# `/read`: postId(C3: post exist or not)
# `/update`: userid(C1: is admin or not, C4: is author or not), postId(C3: post exist or not)
# `/delete`: userid(C1: is admin or not, C4: is author or not), postId(C3: post exist or not)

# Criteria: Base Choice Coverage(BCC)

# testcase
URL = "http://localhost:5000"


# `/create`(C1, C2):
# - (Basic) true, true
# - false, true
# - ture, false
# - false, false


@pytest.mark.parametrize('testcase, ans', [
    ({'content': 'Valid Message'}, 200),
    ({'content': 'Invalid Message'}, 400)
])
def test_create (testcase, ans):
    """
    Test Cases: create route
    """
    resp = post(f'{URL}/bulletin', json=testcase)

    assert resp.status_code == ans

# `/read`(C3):
# - (Basic) true
# - false
@pytest.mark.parametrize('id_, ans', [
    (1, 200),
    (-1, 400)
])
def test_read (id_, ans):
    """
    Test Cases: read route
    """
    resp = get(f'{URL}/bulletin/{id_}')

    assert resp.status_code == ans

#  `/update`(C1, C2, C3, C4):
#  - (Basic) true, true, true, true
#  - false, true, true, true
#  - true, false, true, true
#  - true, true, false, true
#  - true, true, true, false
@pytest.mark.parametrize('message, id_, ans', [
    ({'content': 'Valid Message'}, 1, 200),
    ({'content': 'Valid Message'}, -1, 400),
    ({'content': 'Invalid Message'}, -1, 400)
])
def test_update (message, id_, ans):
    """
    Test Cases: update route
    """
    resp = put(f'{URL}/bulletin/{id_}', json=message)

    assert resp.status_code == ans


# `/delete`(C1, C3, C4):
# - (Basic) true, true, true
# - false, true, true
# - true, false, true
# - true, true, false
@pytest.mark.parametrize('id_, ans', [
    ( 1, 200),
    ( -1, 400)
])
def test_delete(id_, ans):
    """
    Test Cases: delete route
    """
    resp = delete(f'{URL}/bulletin/{id_}')

    assert resp.status_code == ans

