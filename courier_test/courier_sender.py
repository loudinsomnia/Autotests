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
from class_test import SEL


class CourierSender(SEL):
    # Переход на страницу courier
    def courier(self, time_out):
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        courier = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//li[@title='Switch current view representation']//input[@type='text']")))
        new_view_selector = ActionChains(self.driver)
        new_view_selector.click(on_element=courier)
        new_view_selector.double_click(on_element=courier)
        new_view_selector.send_keys_to_element(courier, 'Courier')
        new_view_selector.send_keys_to_element(courier,Keys.ENTER)
        new_view_selector.perform()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        time.sleep(2)


    # Поиск лида в представлении courier
    def courier_lead(self, time_out,oid):
        identifer = WebDriverWait(self.driver, int(time_out)).until(
            EC.presence_of_element_located(
                (By.XPATH,"//tr[@class='dxgvFilterRow_XafTheme']//*[@class='dxgv'][1]//input")))
        identifer.send_keys(oid)
        time.sleep(1)
        identifer.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        time.sleep(2)


    # Переход на страницу отправки в курьерскую службу
    def send_to_courier(self, time_out):
        order_to_send = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//tr[@class='dxgvDataRow_XafTheme dxgvLVR']//td[@class='dxgvCommandColumn_XafTheme dxgv dx-ac'][1]//span[@class='dxWeb_edtCheckBoxUnchecked_XafTheme dxICheckBox_XafTheme dxichSys dx-not-acc']")))
        order_to_send.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        dots_to_send = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='dxm-popOut']//span[@class='dx-acc dxWeb_mAdaptiveMenu_XafTheme dxm-pImage dx-acc-s']")))
        dots_to_send.click()
        send_to_courier = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//li[@title='Send to Courier service']//span[@class='dx-vam dxm-ait']")))
        send_to_courier.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))


    # Выбор курьерской службы и отправка лида в курьерку
    def choose_courier_services(self, time_out, courier, partner):
        WebDriverWait(self.driver, int(time_out)).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, "//div[@class='dxpcLite_XafTheme dxpclW dxpc-mainDiv white dxpc-shadow']//iframe")))
        courier_service = self.driver.find_element(
            By.XPATH, "//table[@class='dxeButtonEditSys dxeButtonEdit_XafTheme dxeReadOnly_XafTheme']//td[@title='Find']")
        courier_service.click()
        self.driver.switch_to.parent_frame()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH,
                 "//div[@class='dxpcLite_XafTheme dxpclW dxpc-mainDiv white findPopupControl dxpc-shadow']//iframe")))
        chose_service = self.driver.find_element(
            By.XPATH,
            "//table[@class='ParametrizedActionControl ParametrizedActionWithImage TemplatedItem']//input[@name='FindDialog$SAC$Menu$ITCNT0$xaf_a4$Ed']")
        chose_service.send_keys(courier, Keys.RETURN)
        service = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable(
            (By.XPATH, f"//table[@class='dxgvTable_XafTheme dxgvRBB']//td[.='{courier}']")))
        service.click()
        submit = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//li[@title='OK']//span[.='OK']")))
        submit.click()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        self.driver.switch_to.parent_frame()
        WebDriverWait(self.driver,int(time_out)).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH,"//div[@class='dxpcLite_XafTheme dxpclW dxpc-mainDiv white dxpc-shadow']//iframe")))
        time.sleep(1)
        partner_service = self.driver.find_element(
            By.XPATH, "//table[@class='dxeButtonEditSys dxeButtonEdit_XafTheme xafLookupEditor']//input[@type='text']")
        partner_service_chooser = ActionChains(self.driver)
        partner_service_chooser.double_click(on_element=partner_service)
        partner_service_chooser.click(on_element=partner_service)
        partner_service_chooser.send_keys_to_element(partner_service,partner)
        partner_service_chooser.perform()
        WebDriverWait(self.driver, int(time_out)).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[.='Loading…']")))
        prepare = WebDriverWait(self.driver, int(time_out)).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//li[@title='Prepare rows']//span[.='Prepare rows']")))
        prepare.click()