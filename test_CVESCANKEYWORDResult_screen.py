# Generated by Selenium IDE
import pytest
import pdb
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class TestCVESCANKEYWORDRESULT_screen():
    '''
    def setup_method(self, method):
        #print("\n=============")
        #print(id(self))
        #print("setup_method")
        #browser = webdriver.Firefox()
        browser = conftest.browser()
        #pdb.set_trace()
        #browser = browser()
        #pdb.set_trace()
        self.vars = {}

    def teardown_method(self, method):
        browser.quit()
    '''

    def test_cVESCANKEYhumax(self, browser):     
        # Test name: CVESCAN_KEY_humax
        # Step # | name | target | value | comment
        # 1 | open | /cve/search_cve_list.html |  |         
        browser.get("https://cve.mitre.org/cve/search_cve_list.html")
        # 2 | setWindowSize | 1154x878 |  | 
        browser.set_window_size(1154, 878)
        # 3 | click | name=keyword |  | 
        browser.find_element(By.NAME, "keyword").click()
        # 4 | type | name=keyword | humax | 
        browser.find_element(By.NAME, "keyword").send_keys("humax")
        # 5 | sendKeys | name=keyword | ${KEY_ENTER} | 
        browser.find_element(By.NAME, "keyword").send_keys(Keys.ENTER)
        # 6 | assertText | css=.smaller:nth-child(2) | There are 8 CVE entries that match your search. | 
        time.sleep(3)
        assert browser.find_element(By.CSS_SELECTOR, ".smaller:nth-child(2)").text == "There are 8 CVE entries that match your search."
        #assert False
        # 7 | close |  |  | 
        #browser.close()

    
    def test_cVESCANKEYmongoose(self, browser):
        # Test name: CVESCAN_KEY_mongoose
        # Step # | name | target | value | comment
        # 1 | open | /cve/search_cve_list.html |  | 
        browser.get("https://cve.mitre.org/cve/search_cve_list.html")
        # 2 | setWindowSize | 1154x854 |  | 
        browser.set_window_size(1154, 854)
        # 3 | click | name=keyword |  | 
        browser.find_element(By.NAME, "keyword").click()
        # 4 | type | name=keyword | mongoose | 
        browser.find_element(By.NAME, "keyword").send_keys("mongoose")
        # 5 | sendKeys | name=keyword | ${KEY_ENTER} | 
        browser.find_element(By.NAME, "keyword").send_keys(Keys.ENTER)
        # 6 | click | css=.smaller:nth-child(2) |  | 
        #time.sleep(3)
        #browser.find_element(By.CSS_SELECTOR, ".smaller:nth-child(2)").click()
        # 7 | assertText | css=.smaller:nth-child(2) | There are 29 CVE entries that match your search. | 
        time.sleep(3)
        assert browser.find_element(By.CSS_SELECTOR, ".smaller:nth-child(2)").text == "There are 29 CVE entries that match your search."
        #assert False
        # 8 | close |  |  | 
        #browser.close()
    
    def test_cVESCANKEYecos(self, browser):
        # Test name: CVESCAN_KEY_ecos
        # Step # | name | target | value | comment
        # 1 | open | /cve/search_cve_list.html |  | 
        browser.get("https://cve.mitre.org/cve/search_cve_list.html")
        # 2 | setWindowSize | 1154x854 |  | 
        browser.set_window_size(1154, 854)
        # 3 | click | name=keyword |  | 
        browser.find_element(By.NAME, "keyword").click()
        # 4 | type | name=keyword | ecos | 
        browser.find_element(By.NAME, "keyword").send_keys("ecos")
        # 5 | sendKeys | name=keyword | ${KEY_ENTER} | 
        browser.find_element(By.NAME, "keyword").send_keys(Keys.ENTER)
        # 6 | click | css=.smaller:nth-child(2) |  | 
        #time.sleep(3)
        #browser.find_element(By.CSS_SELECTOR, ".smaller:nth-child(2)").click()
        # 7 | assertText | css=.smaller:nth-child(2) | There are 12 CVE entries that match your search. | 
        time.sleep(3)
        assert browser.find_element(By.CSS_SELECTOR, ".smaller:nth-child(2)").text == "There are 12 CVE entries that match your search."
        #assert False
        # 8 | close |  |  | 
        #browser.close()
    
    def test_cVESCANKEYbroadcom(self, browser):
        # Test name: CVESCAN_KEY_broadcom
        # Step # | name | target | value | comment
        # 1 | open | /cve/search_cve_list.html |  | 
        browser.get("https://cve.mitre.org/cve/search_cve_list.html")
        # 2 | setWindowSize | 1154x854 |  | 
        browser.set_window_size(1154, 854)
        # 3 | click | name=keyword |  | 
        browser.find_element(By.NAME, "keyword").click()
        # 4 | type | name=keyword | broadcom | 
        browser.find_element(By.NAME, "keyword").send_keys("broadcom")
        # 5 | sendKeys | name=keyword | ${KEY_ENTER} | 
        browser.find_element(By.NAME, "keyword").send_keys(Keys.ENTER)
        # 6 | click | css=.smaller:nth-child(2) |  | 
        #time.sleep(3)
        #browser.find_element(By.CSS_SELECTOR, ".smaller:nth-child(2)").click()
        # 7 | assertText | css=.smaller:nth-child(2) | There are 80 CVE entries that match your search. | 
        time.sleep(3)
        assert browser.find_element(By.CSS_SELECTOR, ".smaller:nth-child(2)").text == "There are 81 CVE entries that match your search."
        #assert False
        # 8 | close |  |  | 
        #browser.close()
    

#pytest.main(['test_CVESCANKEYWORDResult_screen.py', '--html=./resultreport/report.html'])    
#pytest.main(['test_CVESCANKEYWORDResult_screen.py'])    
