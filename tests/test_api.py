import requests
import json
import pytest

base_url = "https://practice.expandtesting.com/notes/api/users"


def test_positive_registration():
    url = f"{base_url}/register"
    data = {
        "name": "Yuliya",
        "email": "yko.kot7@gmail.com",
        "password": "123456789"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201
    assert response.json()['success'] is True


def test_duplicate_registration():
    url = f"{base_url}/register"
    data = {
        "name": "Yuliya",
        "email": "yko.kot7@gmail.com",
        "password": "123456789"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 409
    assert response.json()['success'] is False


def test_invalid_email_registration():
    url = f"{base_url}/register"
    data = {
        "name": "tttt1",
        "email": "invalid-email",
        "password": "rrrrfggf"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400
    assert response.json()['success'] is False


def test_short_name_registration():
    url = f"{base_url}/register"
    data = {
        "name": "t",
        "email": "yyy11@fj.com",
        "password": "rrrrfggf"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400
    assert response.json()['success'] is False


def test_invalid_password_registration():
    url = f"{base_url}/register"
    data = {
        "name": "tttt1",
        "email": "yyy7uy11@fj.com",
        "password": "short"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400
    assert response.json()['success'] is False


def test_login_success():
    login_url = f"{base_url}/login"
    login_data = {
        "email": "yko.kot7@gmail.com",
        "password": "123456789"
    }
    response = requests.post(login_url, json=login_data)
    assert response.status_code == 200
    assert response.json()['success'] is True


def test_invalid_login():
    url = f"{base_url}/login"
    data = {
        "email": "invalid-email",
        "password": "123456789"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400
    assert response.json()['success'] is False


def test_nonexistent_user_login():
    url = f"{base_url}/login"
    data = {
        "email": "fffff@ghg.com",
        "password": "123456789"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 401
    assert response.json()['success'] is False

