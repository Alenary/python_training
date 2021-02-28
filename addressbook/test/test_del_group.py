# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test 1", header="test 1 text 1", footer="test 1 text 2"))
    app.group.delete_first_group()
