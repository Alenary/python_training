# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture    # инициализация фикстуры
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="Test 1", header="test 1 text 1", footer="test 1 text 2"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="", header="", footer=""))
    app.logout()


'''Примечания:
  virtualenv venv - создание виртуального окружения
  source venv/bin/activate - запуск виртуального окружения virtualenv
  deactivate - отключение виртуального окружения
  установлены pip, selenium, pytest, geckodriver перемещен в /usr/local/bin'''
