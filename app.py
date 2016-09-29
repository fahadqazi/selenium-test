
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chromedriver_path = "/Users/Fahad/Downloads/chromedriver"

driver = webdriver.Chrome(chromedriver_path)
driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")

countries = ["Canada","Germany", "Iceland","Pakistan", "Singapore", "South Africa"]

for country in countries:    
    input_element = driver.find_element_by_id("countryName")
    input_element.clear()
    input_element.send_keys(country)
    input_element.text
    input_element.send_keys(Keys.RETURN)

    try:
        payMonthlyButton = WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.ID, "paymonthly")))
    except Exception as e:
        print e
        
    payMonthlyButton.click()

    try:
        callCost = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="standardRatesTable"]/tbody/tr[1]/td[2]""")))
    except Exception as e:
        print e
        
    print country + " ", callCost.text
    driver.refresh()

