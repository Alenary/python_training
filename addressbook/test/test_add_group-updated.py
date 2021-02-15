# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture    # инициализация фикстуры
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="Test 1", header="test 1 text 1", footer="test 1 text 2"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="", header="", footer=""))
    app.session.logout()


'''Примечания:
  virtualenv venv - создание виртуального окружения
  source venv/bin/activate - запуск виртуального окружения virtualenv
  deactivate - отключение виртуального окружения
  установлены pip, selenium, pytest, geckodriver перемещен в /usr/local/bin'''
