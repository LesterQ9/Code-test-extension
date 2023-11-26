import pytest
import allure

@allure.feature("success")
def test_success():
    """this test succeeds"""
    assert True

@allure.feature("fails")
def test_failure():
    """this test fails"""
    assert False

def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')

def test_broken():
    raise Exception('oops')
