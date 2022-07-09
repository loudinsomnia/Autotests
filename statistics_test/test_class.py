import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class SEL:
    PATH = Service(r"path\to\webdriver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    ds = DesiredCapabilities.CHROME
    ds['goog:loggingPrefs'] = {'browser': 'SEVERE'}
    driver = webdriver.Chrome(service=PATH, options=chrome_options)

    def auth(self, port, host):
        if port == '':
            url = f'http://{host}'
        else:
            url = f'http://{host}:{port}'
        SEL.driver.get(url=url)
        assert SEL.driver.title == 'Authentication Logon Parameters With Code', f'Wrong url or truble with auth page'
        login = self.driver.find_element(By.XPATH,
                                         "//table[@class='GroupContent Adaptivity AdaptivityEditorContainer CardGroupBase lastVerticalCardGroup']//input[@type='text']")
        paswd = self.driver.find_element(By.XPATH, "//input[@type='password']")
        sub = SEL.driver.find_element(By.XPATH, '//*[@id="Logon_PopupActions_Menu_DXI0_T"]/span')
        auth = ActionChains(self.driver)
        auth.send_keys_to_element(login, 'login')
        auth.send_keys_to_element(paswd, 'pass')
        auth.click(sub)
        auth.perform()
        for logs in SEL.driver.get_log('browser'):
            assert logs == [], f"{logs['message']}"

    def check_errors(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, '#Vertical_ErrorInfo_Header > td')
        except EC.NoSuchElementException:
            return False
        return True

    def statistics_page(self, xpath, time_out):
        statistics_page = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        statistics_page.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        for log in self.driver.get_log('browser'):
            assert log == [], f"{log['message']}"

    def statistic_execute(self, time_out, selector):
        execute_query = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        execute_query.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        for log in self.driver.get_log('browser'):
            assert log == [], f"{log['message']}"
        assert self.check_errors() == False, 'Error on page when try to execute data'

    def statistics_with_required_fields(self, time_out, xpath, required, for_place, selector):
        self.statistics_page(xpath=xpath, time_out=time_out)
        choose_product = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH, for_place)))
        choose_product.click()
        product = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH, required)))
        product.click()
        choose_product.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        self.statistic_execute(time_out=time_out, selector=selector)

    def new_view_statistics(self, time_out, xpath):
        self.statistics_page(xpath=xpath, time_out=time_out)
        WebDriverWait(self.driver, int(time_out)).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH,
                                                       "//div[@class='Layout LayoutViewMode DashboardView ']//iframe")))
        execute = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#advanced_search > div.ant-row.header-filter > div.ant-col.ant-col-18.ant-col-xs-15.ant-col-sm-18 > button:nth-child(3)')))
        execute.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#root > section > main > div > div > div > div > div > div > div > div > div > div.ant-table-body > table > tbody')))
        self.driver.switch_to.parent_frame()
        for log in self.driver.get_log('browser'):
            assert log == [], f"{log['message']}"

    def warehous_statistics(self, time_out, xpath, selector, table_param):
        self.statistics_page(xpath=xpath, time_out=time_out)
        warehouses = self.driver.find_element(By.XPATH, "//td[@title='Find']")
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        warehouses.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        WebDriverWait(self.driver, int(time_out)).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, "//div[@class='dxpcLite_XafTheme dxpclW dxpc-mainDiv white findPopupControl dxpc-shadow']//iframe")))
        warehouses_searcher = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH, "//td[@title='Filter records by text']")))
        warehouses_searcher.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        chosen_warehous = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH, table_param)))
        chosen_warehous.click()
        submit = self.driver.find_element(By.XPATH, "//div[@class='dxm-main dxm-horizontal menuButtons menuButtons_XafTheme dx-acc-r dxm-noWrap']//span[.='OK']")
        ActionChains(self.driver).move_to_element(submit).click(submit).perform()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        self.driver.switch_to.parent_frame()
        self.statistic_execute(time_out=time_out, selector=selector)
