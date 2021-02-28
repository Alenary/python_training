import time


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        time.sleep(1)   # возможно использование wd.find_element_by_name("user") для устранения перекрытия тестов при множественном запуске

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in(): # залогинен
            if self.is_logged_in_as(username):  # совпадение имени
                return
            else:
                self.logout()
        self.login(username, password)

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

