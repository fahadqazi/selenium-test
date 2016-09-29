import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DataScrapApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/Fahad/Downloads/chromedriver")

    def test_scrape(self):
        driver = self.driver
        driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")
        self.assertIn("O2", driver.title)
        country = "Canada"
        input_element = driver.find_element_by_id("countryName")
        input_element.clear()
        self.assertEquals("", input_element.get_attribute('value'))
        input_element.send_keys(country)
        self.assertEquals("Canada", input_element.get_attribute('value'))

        
    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
