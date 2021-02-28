# -*- coding: utf-8 -*-

from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middle_name="Middle name", first_name="First name", last_name="Last name", nickname="Nickname", img_path="data/photo.jpg", title="Title", company="Company",
                         address="address address", home_phone="+79031234567", mobile_phone="+79031234568", work_phone="+79031234569", fax_phone="+79031234510",
                         email_1="test@gmail.com", email_2="test2@gmail.com", email_3="test3@gmail.com", homepage="test.com", bday="1", bmonth="February",
                         byear="1990", aday="3", amonth="April", ayear="2000", group_name="Test 1", address_2="address address 2", home="home", notes="notes"))
    app.contact.edit(Contact(middle_name=" upd", first_name=" upd", last_name=" upd", nickname=" upd", img_path="data/photo2.jpg", title=" upd", company=" upd",
                         address=" upd", home_phone="+79031234560", mobile_phone="+79031234560", work_phone="+79031234560", fax_phone="+79031234511",
                         email_1="test_upd@gmail.com", email_2="test2_upd@gmail.com", email_3="test3_upd@gmail.com", homepage="test-new.com", bday="6", bmonth="May",
                         byear="1991", aday="4", amonth="May", ayear="2001", group_name="Test 1", address_2="address address new", home="home new", notes="notes new"))
