import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from tkinter import filedialog
from selenium.common.exceptions import NoSuchElementException

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

zkulos=[]
with open(file) as f:
    for line in f:
        zkulos.append(line.strip())

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
driver.get('https://oss.uredjenazemlja.hr/public/lrServices.jsp?action=publicLdbExtract')
opsuin = input("Općinski sud / ZK odjel: ")
opsuin = opsuin[0].upper()+opsuin[1:len(opsuin)].lower()
opsu = driver.find_element_by_name("institution")
opsu.send_keys(opsuin)
opsu.send_keys(Keys.ENTER)
time.sleep(0.1)
gkin = input("Glavna knjiga: ").upper()
gk = driver.find_element_by_name("mainBook")
gk.send_keys(gkin)
gk.send_keys(Keys.ENTER)
time.sleep(0.1)
bc = driver.find_element_by_name("lrUnitNumber")
bc.send_keys(str(zkulos[0]))
bc.send_keys(Keys.ENTER)
nepocestizk = []
for i in range (0, len(zkulos)):
    bc.clear()
    bc.send_keys(str(zkulos[i]))
    bc.send_keys(Keys.ENTER)
    pregledaj = driver.find_element_by_class_name("x-btn-text.icon-complete")
    pregledaj.click()
    captcha = input("Captcha je: ")
    kb = driver.find_element_by_id("x-auto-64")
    kb.send_keys(captcha)
    potvrdi = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
    potvrdi.click()
    time.sleep(0.1)
    while check_exists_by_xpath('//*[text()[contains(.,"Informacija")]]') is True:
        uredu = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[2]/em/button")
        uredu.click()
        time.sleep(0.1)
        captcha = input("Captcha je: ")
        kb = driver.find_element_by_id("x-auto-64")
        kb.send_keys(captcha)
        potvrdi = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
        potvrdi.click()
        time.sleep(0.1)
    else:
        pass
    time.sleep(0.1)
    while check_exists_by_xpath('//*[text()[contains(.,"Učitavanje podataka")]]') is True:
        time.sleep(0.1)
    else:
        pass
    if check_exists_by_xpath('//*[text()[contains(.,"Upozorenje")]]') is True:
        makni = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[2]/em/button")
        nepocestizk.append(cestice[i])
        makni.click()
    else:
        if check_exists_by_xpath('//*[text()[contains(.,"Odabir tijela ili etaža")]]') is True:
            checketaze = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div/table/thead/tr/td[1]")
            checketaze.click()
            while check_exists_by_xpath('//*[text()[contains(.,"Učitavanje podataka")]]') is True:
                time.sleep(0.1)
            else:
                potvrdi = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
                potvrdi.click()
        else:
            pass
        while check_exists_by_xpath('//*[@class=" extractPanel extractLoader"]') is True:
            time.sleep(0.1)
        else:
            pass
        time.sleep(1)
        preuzmi = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div[1]/div/div/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
        preuzmi.click()
        while check_exists_by_xpath('//*[text()[contains(.,"Učitavanje podataka")]]') is True:
            time.sleep(0.1)
        else:
            pass
        povratak = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div[1]/div/div/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button")
        povratak.click()
print(nepocestizk)
