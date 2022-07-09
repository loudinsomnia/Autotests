import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
import datetime


class Filters():
    def Sphere_Filter(self,data_lead_crm,excel):
        lead = data_lead_crm.split()
        date = lead[2]
        newdate = datetime.datetime.strptime(date, '%d.%m.%Y')
        truedate = datetime.datetime.strftime(newdate, '%Y-%m-%d')
        number = lead[5]
        truenumber = number.replace('+', '')
        quotes = excel[7]
        with_out_quotes = quotes.replace('"','')
        assert excel[1] == lead[1], f"Wrong LEAD_ID - {excel[1]} {excel}/////{lead}"
        assert excel[2] == truedate, f"Wrong DATE - {excel[2]} {excel}/////{lead}"
        assert excel[5] == truenumber, f"Wrong Number - {excel[5]} {excel}/////{lead}"
        assert excel[6] == lead[6], f"Wrong GEO - {excel[6]} {excel}/////{lead}"
        assert with_out_quotes == lead[7], f"Wrong STATE - {excel[7]} {lead[7]} {excel}/////{lead}"
        assert excel[9] == lead[9], f"Wrong POST-CODE - {excel[8]} {excel}/////{lead}"
        assert excel[10] == lead[10], f"Wrong SITY - {excel[9]} {excel}/////{lead}"
        assert excel[11] == lead[11], f"Wrong STREET - {excel[10]} {excel}/////{lead}"
        assert excel[12] == lead[12], f"Wrong House - {excel[11]} {excel}/////{lead}"

    def DapSide_Filter(self,data_lead_crm,excel):
        lead = data_lead_crm.split()
        number = lead[8]
        truenumber = number.replace('+', '')
        assert excel[2] == lead[2], f"Wrong LEAD_ID - {excel[2]} {excel}/////{lead}"
        assert excel[3] == lead[3],f"Wrong adress - {excel[3]} {excel}/////{lead}"
        assert excel[4] == lead[4],f"Wrong POST_CODE - {excel[4]} {excel}/////{lead}"
        assert excel[5] == lead[5], f"Wrong SITY - {excel[5]} {excel}/////{lead}"
        assert excel[6] == lead[6], f"Wrong STATE - {excel[6]} {excel}/////{lead}"
        assert excel[7] == lead[7], f"Wrong GEO - {excel[7]} {excel}/////{lead}"
        assert excel[8] == truenumber,f"Wrong number {excel[8]} {excel}/////{lead}"
        assert excel[9] == lead[9],f"Wrong date - {excel[9]} {excel}/////{lead}"
        assert excel[12] == lead[12],f"Wrong total cost - {excel[12]} {excel}/////{lead}"