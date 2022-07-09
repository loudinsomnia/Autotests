import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time


class SEL:
    PATH = Service(r"path\to\webdriver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option('useAutomationExtension', False)
    js_scr = '//*[@id="dxis_1149438735"]'
    ds = DesiredCapabilities.CHROME
    ds['goog:loggingPrefs'] = {'browser': 'SEVERE'}
    driver = webdriver.Chrome(service=PATH, options=chrome_options)

    def auth(self,port,host):
        if port == '':
            url = f'http://{host}'
        else:
            url = f'http://{host}:{port}'
        SEL.driver.get(url=url)
        assert SEL.driver.title == 'Authentication Logon Parameters With Code', f'Wrong url or truble with auth page'
        login = self.driver.find_element(By.XPATH,
                                         "//table[@class='GroupContent Adaptivity AdaptivityEditorContainer CardGroupBase lastVerticalCardGroup']//input[@type='text']")
        paswd = self.driver.find_element(By.XPATH,"//input[@type='password']")
        sub = SEL.driver.find_element(By.XPATH, '//*[@id="Logon_PopupActions_Menu_DXI0_T"]/span')
        auth=ActionChains(self.driver)
        auth.send_keys_to_element(login,'login')
        auth.send_keys_to_element(paswd,'pass')
        auth.click(sub)
        auth.perform()
        for logs in SEL.driver.get_log('browser'):
            assert logs == [], f"{logs['message']}"


    def mass_function(self, time_out, xpath):
        ancor = WebDriverWait(SEL.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        ancor.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        for logs in SEL.driver.get_log('browser'):
            assert SEL.driver.get_log('browser') == [], f"{logs['message']}"
        # assert SEL.driver.title == ancor.text + ' - Leads CRM', f'Wrong page {self.driver.title}'