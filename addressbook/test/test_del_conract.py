# -*- coding: utf-8 -*-

def test_delete_first_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete(number=3)    # число контактов для удаления
    app.session.logout()