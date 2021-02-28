# -*- coding: utf-8 -*-

def test_delete_first_contacts(app):
    app.contact.delete(number=3)    # число контактов для удаления
