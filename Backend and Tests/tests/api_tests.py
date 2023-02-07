import pytest
import requests

response = requests.get('http://127.0.0.1:8080/pricing/?address=Wroclaw,rynek&rooms=7&area=80')


def test_status_code_good_request():
    assert 200 == response.status_code


def test_response_format_good_request():
    assert 'application/json' == response.headers.get('content-type')


def test_response_data_good_request():
    resp = response.json()
    assert dict == type(resp)
    assert 'price' in resp.keys()
    assert float == type(resp.get('price'))

bad_response = requests.get('http://127.0.0.1:8080/pricing/?address=Wroclaw,rynek&rooms=7')


def test_status_code_bad_request():
    assert 400 == bad_response.status_code


def test_response_data_bad_request():
    resp = bad_response.json()
    assert dict == type(resp)
    assert 'message' in resp.keys()
    assert "Missing parameter" == resp.get('message')

