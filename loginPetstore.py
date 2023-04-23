import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):

    tetelek = ["navigation__home", "navigation__pets", "navigation__store", "navigation__logout"]

    szovegek = ["Home", "Pets", "Store", "Logout"]

    def adatBevitel(self, oldalelem, bevitel):
        self.oldalelem = oldalelem
        self.bevitel = bevitel
        wait = WebDriverWait(self.meghajto, 10)
        wait.until(EC.element_to_be_clickable((By.ID, oldalelem)))
        self.meghajto.find_element(By.ID, oldalelem).send_keys(bevitel)

    def lathatosagEllenorzes(self, tetelek, szovegek):
        self.tetelek = tetelek
        self.szovegek = szovegek
        for tetel in self.tetelek:
            wait = WebDriverWait(self.meghajto, 10)
            wait.until(EC.element_to_be_clickable((By.ID, tetel)))
        for szoveg in self.szovegek:
            self.assertIn(szoveg, self.meghajto.page_source)

    def setUp(self):
        self.meghajto = webdriver.Chrome()

    def test_something(self):
        meghajto = self.meghajto
        meghajto.maximize_window()
        meghajto.get("https://training.testifi.io/login")
        self.adatBevitel("mat-input-0", "demo.user")
        self.adatBevitel("mat-input-1", "Test!123")
        self.meghajto.find_element(By.ID, "login__submit").click()
        self.lathatosagEllenorzes(self.tetelek, self.szovegek)

    def tearDown(self):
        self.meghajto.close()


if __name__ == '__main__':
    unittest.main()
