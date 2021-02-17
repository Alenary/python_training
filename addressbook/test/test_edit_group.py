# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(group_name=" upd", header="new text", footer=" upd"))
    app.session.logout()
