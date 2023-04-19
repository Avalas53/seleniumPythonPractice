import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.meghajto = webdriver.Chrome()

    def test_something(self):
        meghajto = self.meghajto
        meghajto.maximize_window()
        meghajto.get("https://training.testifi.io/pets")
        time.sleep(2)
        petgomb = meghajto.find_element(By.ID, "menu")
        petgomb.click()
        time.sleep(1)
        addview = meghajto.find_element(By.ID, "menu__add-view")
        addview.click()
        time.sleep(1)
        cardview = meghajto.find_element(By.ID, "view-menu__card")
        cardview.click()
        time.sleep(1)

    def tearDown(self):
        self.meghajto.close()


if __name__ == '__main__':
    unittest.main()
