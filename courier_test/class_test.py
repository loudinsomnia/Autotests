import time
import pandas as pd
import pytest
import random
import string
import uuid
import json
import requests
import os.path
import datetime
from data_filter import Filters
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service



class SEL:
    PATH = Service(r"path\to\webdriver") #Путь к вебдрайверу
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": r"C:\Temp",#Путь к папке Downloads
        "download.prompt_for_download": False,
    })
    chrome_options.add_experimental_option('useAutomationExtension', False)
    ds = DesiredCapabilities.CHROME
    ds['goog:loggingPrefs'] = {'browser': 'SEVERE'}
    driver = webdriver.Chrome(service=PATH, options=chrome_options)
    dt = datetime.datetime.now()
    tru_dt = dt.strftime("%d.%m.%Y")
    day_to_send = dt.strftime('%#d')



    # Процесс авторизации
    def auth(self, port,host):
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
        auth.send_keys_to_element(paswd, 'path')
        auth.click(sub)
        auth.perform()
        for logs in SEL.driver.get_log('browser'):
            assert logs == [], f"{logs['message']}"



    # Переход на страницу ордерс
    def orders(self, time_out):
        orders = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH, '//span[.="Orders"]')))
        orders.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))

    # Поиск созданного лида по идентификатору и переход в карточку созданного лида
    def find_identifer(self, time_out,oid):
        id_search = self.driver.find_element(By.XPATH,
                                             "//*[@class='dxgvFilterRow_XafTheme']/td[10]//input")
        id_search.click()
        id_search.send_keys(oid)
        time.sleep(1)
        id_search.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        time.sleep(2)
        lead_link = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//td[@class='dx-nowrap dxgv dx-al']//a[.='Open lead']")))
        lead_link.click()

    # Смена статуса лида, заполнение полей age, postcode, street, house выбор параметра, если есть таковой у продукта
    # выбор даты календаря и сохранение лида
    def order_change_status(self, time_out,pparam):
        # Смена статуса
        edit = WebDriverWait(self.driver, int(time_out)).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='page-header']//mat-icon[.='edit']")))
        edit.click()
        status = self.driver.find_element(
                By.XPATH, "//*[@class='ng-star-inserted'][2]//span[text()='UNPROCESSED']")
        status.click()
        status_to_send = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH,'//span[.="TO SEND ORDER"]')))
        status_to_send.click()
        # Смена сабстатуса
        substatus = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@class='ng-star-inserted'][2]//mat-form-field[2]//div[@class='mat-select-value']//span")))
        substatus.click()
        substatus_to_sale = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH,'//span[.="TSO - Reject Turned to Sale"]')))
        substatus_to_sale.click()
        # Выбор гендера
        gender = self.driver.find_element(
            By.XPATH,"//div[@class='mat-select-value']//span[@class='ng-tns-c6-43 ng-star-inserted']")
        gender.click()
        choose_gender = WebDriverWait(self.driver,int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH,"//span[.='Male']")))
        choose_gender.click()
        order_source = self.driver.find_element(By.XPATH,"//div[@id='mat-select-value-29']")
        order_source.click()
        choose_source = WebDriverWait(self.driver,int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH,"//span[.='Instagram']")))
        choose_source.click()
        # Заполнение полей age, street, house
        age = self.driver.find_element(By.XPATH, "//input[@id='mat-input-16']")
        post_code = self.driver.find_element(By.XPATH, "//input[@name='PostCode']")
        street = self.driver.find_element(By.XPATH, "//input[@name='Street']")
        house = self.driver.find_element(By.XPATH, "//mat-form-field[@title='House']//input")
        state = self.driver.find_element(By.XPATH,"//input[@name='State']")
        province = self.driver.find_element(By.XPATH, "//input[@name='Province']")
        town = self.driver.find_element(By.XPATH, "//input[@name='Town']")
        params_init = ActionChains(self.driver)
        params_init.send_keys_to_element(age, '33')
        params_init.send_keys_to_element(street, '12')
        params_init.send_keys_to_element(house, '12')
        params_init.send_keys_to_element(post_code, '12')
        params_init.send_keys_to_element(state,'12')
        params_init.send_keys_to_element(province,'12')
        params_init.send_keys_to_element(town,'12')
        params_init.perform()
        # Параметры для продукта если есть таковые
        if pparam == True:
            prod_param = self.driver.find_element(By.CSS_SELECTOR, '#mat-select-value-25 > span')
            prod_param.click()
            prod_new_param = self.driver.find_element(By.CSS_SELECTOR, '#mat-option-48 > span')
            prod_new_param.click()
        # Заполнение календаря
        calendar = self.driver.find_element(
            By.XPATH,"//mat-form-field[@title='Delivery Date']//button")
        calendar.click()
        choose_day = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable(
                (By.XPATH,f"//div[.={self.day_to_send}]")))
        choose_day.click()
        # Сохранение изменений
        save = self.driver.find_element(
            By.XPATH,"//button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary ng-star-inserted']//span[.='Save']")
        save.click()
        acept_lead_update = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH,"//span[.='Close']")))
        acept_lead_update.click()
        go_back = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable(
                (By.XPATH,"//span[.='Go back']")))
        go_back.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))


    # Сравнение информации по продукту отправленному в курьерку в CRM и xlsx файле
    def compare_data(self,time_out,courier,partner):
        data_lead = ''
        WebDriverWait(self.driver, int(time_out)).until(
            EC.text_to_be_present_in_element(
                (By.XPATH,f"//li[@class='dxtc-activeTab dxtc-lead dxtc-last dxtc-psi']//span[.='Rows for {courier}']"),f"{courier}"))
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        rows = self.driver.find_elements(By.XPATH,
                                         "//div[@class='NestedFrameViewSite']//tr[@class='dxgvDataRow_XafTheme']")
        for row in rows:
            data_lead = row.text
        send_manual = WebDriverWait(self.driver,int(time_out)).until(
            EC.element_to_be_clickable(
            (By.XPATH,"//li[@title='Send to Courier (Manual)']//span[.='Send to Courier (Manual)']")))
        send_manual.click()
        file_name = f"C:\\Temp\\Manual_SendToCourier_{courier}_{partner}_{self.tru_dt}.xlsx"#Путь к папке Downloads указывается до Manual_SendTo
        time.sleep(5)
        assert os.path.isfile(file_name) == True,f"file name = {file_name}"
        pd.set_option('display.max_rows',None)
        pd.set_option('display.max_columns',None)
        pd.set_option('display.max_colwidth', None)
        data_excel = pd.read_excel(file_name).to_csv(header=None,sep=' ',index=False)
        excel = data_excel.split()
        #Выборка фильтров
        if courier == 'Sphere':
            Filters().Sphere_Filter(data_lead_crm=data_lead,excel=excel)

        if courier == 'DapSide':
            Filters().DapSide_Filter(data_lead_crm=data_lead,excel=excel)
        os.remove(file_name)


    def cookie_delete(self):
        self.driver.delete_all_cookies()
    def close_driver(self):
        self.driver.quit()