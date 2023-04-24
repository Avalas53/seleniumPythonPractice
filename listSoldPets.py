import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exco


class MyTestCase(unittest.TestCase):
    tetelek1 = ["menu", "menu__search", "attribute__select", "select__status"]
    tetelek2 = ["status__select", "select__sold"]

    def waitAndClick(self, oldalelem):
        self.oldalelem = oldalelem
        wait = WebDriverWait(self.meghajto, 7)
        wait.until(exco.element_to_be_clickable((By.ID, oldalelem)))
        self.meghajto.find_element(By.ID, oldalelem).click()

    def waitAndClickByXpath(self, noidelem):
        self.noidelem = noidelem
        wait = WebDriverWait(self.meghajto, 10)
        wait.until(exco.element_to_be_clickable((By.XPATH, noidelem)))
        self.meghajto.find_element(By.XPATH, noidelem).click()

    def setUp(self):
        self.meghajto = webdriver.Chrome()

    def test_something(self):
        meghajto = self.meghajto
        meghajto.maximize_window()
        meghajto.get("https://training.testifi.io/pets")
        for tetel in self.tetelek1:
            self.waitAndClick(tetel)
        self.waitAndClickByXpath("//*[@id='cdk-step-content-0-0']/form/div/button/span")
        for tetel in self.tetelek2:
            self.waitAndClick(tetel)
        # self.waitAndClick("action__search")
        # self.assertNotIn("available", meghajto.page_source)
        # self.assertNotIn("pending", meghajto.page_source)

    def tearDown(self):
        self.meghajto.close()


if __name__ == '__main__':
    unittest.main()
