# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from python_training.fixture.application import Application


@pytest.fixture    # инициализация фикстуры
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(middle_name="Middle name", first_name="First name", last_name="Last name", nickname="Nickname", img_path="/data/photo.jpg", title="Title", company="Company",
                         address="address address", home_phone="+79031234567", mobile_phone="+79031234568", work_phone="+79031234569", fax_phone="+79031234510",
                         email_1="test@gmail.com", email_2="test2@gmail.com", email_3="test3@gmail.com", homepage="test.com", bday="1", bmonth="February",
                         byear="1990", aday="3", amonth="April", ayear="2000", group_name="Test 1", address_2="address address 2", home="home", notes="notes"))
    app.session.logout()
