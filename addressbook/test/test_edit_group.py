# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group_partially(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test 1", header="test 1 text 1", footer="test 1 text 2"))
    app.group.edit_first_group(Group(group_name="name upd 2"))

def test_edit_first_group_all_fields(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test 1", header="test 1 text 1", footer="test 1 text 2"))
    app.group.edit_first_group(Group(group_name="name upd", header="new text", footer="text upd"))
