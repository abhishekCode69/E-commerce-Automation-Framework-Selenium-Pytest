# Parent of all pages -> contains all common browser actions  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage : 
    def __init__(self, driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver, 10)
    
    def click(self, locator):
        element= self.wait.until(EC.element_to_be_clickable(locator)).click()
        
        try:
            element.click()
        except ElementClickInterceptedException:
            # something (like an ad) is covering the element, so click via JavaScript
            self.driver.execute_script("arguments[0].click();", element)
            
        
    def typeText(self, locator, text):
        element = self.wait.until(EC.visibility_of_all_elements_located(locator))
        element.clear()
        element.send_keys(text)
        
    def getText(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def getTexts(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return [element.text for element in self.driver.find_elements(*locator)]
    
    def isVisible(self,locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
        
    def is_title_containing(self, text):
        try:
            self.wait.until(EC.title_contains(text))
            return True
        except Exception:
            return False
    