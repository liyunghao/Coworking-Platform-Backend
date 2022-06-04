import pytest
from requests import get, post

# 權限狀態的轉移
#
# not login
# normal user
# admin user
#
# ```graphviz
# digraph finite_state_machine {
#     fontname = "Helvetica,Arial,sans-serif"
#    	node [fontname = "Helvetica,Arial,sans-serif"]
#    	edge [fontname = "Helvetica,Arial,sans-serif"]
#    	rankdir = LR
#     node [shape= circle]
#     "not login" -> "normal user" [label= "userExist && correctCredential"]
#     "normal user" -> "admin user" [label = "isAdmin"]
#     "admin user" -> "normal user" [label = "revokeAdmin"]
#     "normal user" -> "not login" [label = "tokenExpire"]
#     "admin user" -> "not login" [label = "tokenExpire"]
# }
# ```
#
# #### For `userExist && correctCredential`
#
# PC, CC:
#
# TC1: T, T
# TC2: F, F
#
# CACC:
#
# TC1(+TC3): T, T
# TC2: F, T
# TC4: T, F
#
# #### For `tokenExpire`, `isAdmin`, `revokeAdmin`
#
# PC, CC, CACC
#
# TC1: T
# TC2: F
#

URL = 'http://localhost:5000'

@pytest.mark.parametrize('testcase, ans', [
    # PC, CC
    ({'username': 'validUser', 'password': 'validUserCredential'}, 200),
    ({'username': 'invalidUser', 'password': 'inValidUserCredential'}, 400),

    # CACC
    ({'username': 'validUser', 'password': 'ValidUserCredential'}, 200),
    ({'username': 'invalidUser', 'password': 'ValidUserCredential'}, 400),
    ({'username': 'validUser', 'password': 'inValidUserCredential'}, 400),
])
def test_predicate_uE_cP(testcase, ans):
    resp = post(f'{URL}/login', json=testcase)
    assert resp.status_code == ans


@pytest.mark.parametrize('testcase, token, ans', [
    # PC, CC, CACC
    ({'account': 'validAccount'}, "notExpiredToken", 200),
    ({'account': 'validAccount'}, "ExpiredToken", 200),
])
def test_predicate_uE_cP(testcase, token, ans):
    resp = get(f'{URL}/user', json=testcase)
    assert resp.status_code == ans
