# -*- coding: utf-8 -*-

from model.contact import Contact

def test_edit_first_contact(app):
    app.contact.edit(Contact(middle_name=" upd", first_name=" upd", last_name=" upd", nickname=" upd", img_path="data/photo2.jpg", title=" upd", company=" upd",
                         address=" upd", home_phone="+79031234560", mobile_phone="+79031234560", work_phone="+79031234560", fax_phone="+79031234511",
                         email_1="test_upd@gmail.com", email_2="test2_upd@gmail.com", email_3="test3_upd@gmail.com", homepage="test-new.com", bday="6", bmonth="May",
                         byear="1991", aday="4", amonth="May", ayear="2001", group_name="Test 1", address_2="address address new", home="home new", notes="notes new"))
