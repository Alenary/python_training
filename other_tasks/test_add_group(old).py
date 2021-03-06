# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):    #  функция инициализации
        self.wd = webdriver.Firefox()    #  запуск драйвера
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        wd = self.wd    #  извлечение ссылки на объект
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Test 1")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("test 1 text 1")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("test 1 text 2")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    def tearDown(self):    #  функция зачистки
        self.wd.quit()

if __name__ == "__main__":    #  указание на фреймворк для запуска
    unittest.main()

'''Примечания:
  virtualenv venv - создание виртуального окружения
  source venv/bin/activate - запуск виртуального окружения virtualenv
  deactivate - отключение виртуального окружения
  установлены pip, selenium, pytest, geckodriver перемещен в /usr/local/bin'''
