# -*- coding: utf-8 -*-

def test_change_contact_group(app):
    app.contact.change_group(number=2)    # число контактов для добавления в другую группу
