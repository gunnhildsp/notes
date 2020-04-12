import os

import pytest


def read_config():
    password = os.environ["DB_PASSWORD"]
    user = os.environ["DB_USER"]
    return {
        "password": password, 
        "user": user,
    }

def test_read_config(monkeypatch):
    monkeypatch.setenv("DB_PASSWORD", "password123")
    monkeypatch.setenv("DB_USER", "username")
    conf = read_config()
    assert set(conf.keys()) == {"password", "user"}
    assert conf["password"] == "password123"
    assert conf["user"] == "username"


@pytest.fixture()
def monkeypatch_config(monkeypatch):
    monkeypatch.setenv("DB_PASSWORD", "password123")
    monkeypatch.setenv("DB_USER", "username")

    
def test_read_config_using_fixture(monkeypatch_config):
    conf = read_config()
    assert set(conf.keys()) == {"password", "user"}
    assert conf["password"] == "password123"
    assert conf["user"] == "username"