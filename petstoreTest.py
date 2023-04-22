import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):

    def waitAndClick(self, oldalelem):
        self.oldalelem = oldalelem
        wait = WebDriverWait(self.meghajto, 10)
        wait.until(EC.element_to_be_clickable((By.ID, oldalelem)))
        self.meghajto.find_element(By.ID, oldalelem).click()

    def setUp(self):
        self.meghajto = webdriver.Chrome()

    def test_something(self):
        meghajto = self.meghajto
        meghajto.maximize_window()
        meghajto.get("https://training.testifi.io/pets")
        self.waitAndClick("menu")
        self.waitAndClick("menu__add-view")
        self.waitAndClick("view-menu__card")
        self.assertIn("Card View", meghajto.page_source)

    def tearDown(self):
        self.meghajto.close()


if __name__ == '__main__':
    unittest.main()
