import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from tkinter import filedialog
from selenium.common.exceptions import NoSuchElementException

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

posjedovnilistovi=[]
with open(file) as f:
    for line in f:
        posjedovnilistovi.append(line.strip())

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_id(id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class(klasa):
    try:
        driver.find_element_by_class_name(klasa)
    except NoSuchElementException:
        return False
    return True

driver = webdriver.Chrome("C:/Users/andrija.friganovic/Desktop/chromedriver.exe")
driver.get('https://oss.uredjenazemlja.hr/public/cadServices.jsp?action=publicCadastreParcel')
katured = driver.find_element_by_name("institution")
katured.send_keys(input("Unesite ime katastarskog ureda: "))
katured.send_keys(Keys.ENTER)
time.sleep(1)
katopc = driver.find_element_by_name("cadastreMunicipality")
katopc.send_keys(input("Unesite ime katastarske opcine: "))
katopc.send_keys(Keys.ENTER)
time.sleep(1)
for i in range(0,len(posjedovnilistovi)):
    brpos = driver.find_element_by_name("possessionSheetNr")
    brpos.clear()
    brpos.send_keys(posjedovnilistovi[i])
    trazi = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/fieldset[2]/div/div/div[2]/div[1]/form/div/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/em/button")
    trazi.click()
    captcha = input("Captcha je: ")
    kb = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/div[2]/div[1]/input")
    kb.send_keys(captcha)
    potvrdi = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
    potvrdi.click()
    time.sleep(0.1)
    while check_exists_by_xpath('//*[text()[contains(.,"Učitavanje podataka")]]') is True:
        time.sleep(0.1)
    else:
        pass
    time.sleep(0.1)
    while check_exists_by_xpath('//*[text()[contains(.,"Informacija")]]') is True:
        moze = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[2]/em/button")
        moze.click()
        captcha = input("Captcha je: ")
        kb = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/div[2]/div[1]/input")
        kb.send_keys(captcha)
        potvrdi = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
        potvrdi.click()
        time.sleep(0.1)
    else:
        pass
    if check_exists_by_xpath('//*[text()[contains(.,"Upozorenje")]]') is True:
        uredu = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[2]/em/button")
        uredu.click()
    else:
        time.sleep(0.1)
        pregledajPLBZP = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
        pregledajPLBZP.click()
        captcha2 = input("Captcha je: ")
        kb2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/div[2]/div[1]/input")
        kb2.send_keys(captcha2)
        potvrdi2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
        potvrdi2.click()
        time.sleep(0.1)
        while check_exists_by_xpath('//*[text()[contains(.,"Informacija")]]') is True:
            moze = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[2]/em/button")
            moze.click()
            captcha2 = input("Captcha je: ")
            kb2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/div[2]/div[1]/input")
            kb2.send_keys(captcha2)
            potvrdi2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
            potvrdi2.click()
            time.sleep(0.1)
        else:
            pass
        while check_exists_by_xpath('//*[text()[contains(.,"Učitavanje podataka")]]') is True:
            time.sleep(0.1)
        else:
            pass
        time.sleep(0.1)
        while check_exists_by_xpath('//*[@class=" extractPanel extractLoader"]') is True:
            time.sleep(0.1)
        else:
            pass
        time.sleep(1)
        preuzmi = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
        preuzmi.click()
        while check_exists_by_xpath('//*[text()[contains(.,"Učitavanje podataka")]]') is True:
            time.sleep(0.1)
        else:
            pass
        odustani = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button")
        odustani.click()





