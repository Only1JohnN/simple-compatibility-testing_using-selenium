import pytest
import logging
import random
from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from time import sleep


#Configure the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SEACRH_QUERIES = [
    "Selenium Automation",
    "Web testing best practices",
    "Cross-browser compatibility testing",
    "Adeniyi John",
    "Automated testing using cypress"
]


# Define a fixture for the webdriver
@pytest.fixture(params = ["Chrome", "Edge"])
def driver(request):
    browser_name = request.param
    logger.info(f"Staring the tests on {browser_name}...")
    
    if browser_name == "Chrome":
        driver = webdriver.Chrome()
        
    elif browser_name == "Edge":
        driver = webdriver.Edge()
        
    else:
        raise ValueError("Unsupported browser: + browser_name")
    
    yield driver
    driver.quit()
    
    
#Functions to perform the search and get the required results
def test_run_search(driver):
    search_query = random.choice(SEACRH_QUERIES)      # For Dyanmic data
    driver.get("https://www.google.com/")
    logger.info(f"Searching for: {search_query}")
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query + Keys.RETURN)
    
    
    sleep(2)
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    logger.info(f"Results from {driver.capabilities['browserName']} for '{search_query}':")
    
    for result in results:
        logger.info(result.text)
        
