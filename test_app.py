# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DataScrapeApp(unittest.TestCase):

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
        input_element.send_keys(Keys.RETURN)
        payMonthlyButton = WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.ID, "paymonthly")))
        self.assertIn("Pay Monthly", payMonthlyButton.text)
        payMonthlyButton.click()
        callCost = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="standardRatesTable"]/tbody/tr[1]/td[2]""")))
        self.assertEquals("£1.50", callCost.text.encode('utf-8'))
        
    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
