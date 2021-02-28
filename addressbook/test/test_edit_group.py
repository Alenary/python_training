# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group_partially(app):
    app.group.edit_first_group(Group(group_name="name upd 2"))

def test_edit_first_group_all_fields(app):
    app.group.edit_first_group(Group(group_name="name upd", header="new text", footer="text upd"))
