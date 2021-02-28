# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(group_name="Test 1", header="test 1 text 1", footer="test 1 text 2"))


def test_add_empty_group(app):
    app.group.create(Group(group_name="", header="", footer=""))

'''Примечания:
  virtualenv venv - создание виртуального окружения
  source venv/bin/activate - запуск виртуального окружения virtualenv
  deactivate - отключение виртуального окружения
  установлены pip, selenium, pytest, geckodriver перемещен в /usr/local/bin'''
