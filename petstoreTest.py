import unittest
import time
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.meghajto = webdriver.Chrome()
        self.meghajto.maximize_window()

    def test_something(self):
        self.meghajto.get("https://training.testifi.io/pets")
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
