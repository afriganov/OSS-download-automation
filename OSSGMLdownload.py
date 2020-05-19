import time
from selenium import webdriver
import tkinter as tk
from tkinter import filedialog
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

cestice=[]
with open(file) as f:
    for line in f:
        cestice.append(line.strip())

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

driver = webdriver.Chrome("") #path od webdrivera
driver.get('https://oss.uredjenazemlja.hr/private/login.jsp')

loginform = driver.find_element_by_xpath("/html/body/div[3]/div[2]/form[1]/div[2]/div/input")
loginform.send_keys("")  #uname

passform = driver.find_element_by_xpath("/html/body/div[3]/div[2]/form[1]/div[3]/div/input")
passform.send_keys("") #password

captcha = input("Captcha je: ")
capform = driver.find_element_by_xpath("/html/body/div[3]/div[2]/form[1]/div[5]/div/input")
capform.send_keys(captcha)
prijava = driver.find_element_by_xpath("/html/body/div[3]/div[2]/form[1]/div[6]/button")
prijava.click()
time.sleep(1)
katapad = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[8]/a")
katapad.click()
time.sleep(1)
izvozpod = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[8]/ul/li[2]/a")
izvozpod.click()
time.sleep(1)
zaizd = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr/td[2]/div/div")
zaizd.click()
time.sleep(1)
katured = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/fieldset[1]/div/div/div[1]/div[1]/div/input")
katured.send_keys(input("Katastarski ured: "))
katured.send_keys(Keys.ENTER)
katured = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/fieldset[1]/div/div/div[2]/div[1]/div/input")
katured.send_keys(input("Katastarska općina: "))
katured.send_keys(Keys.ENTER)
time.sleep(1)
brkatces = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/fieldset[1]/div/div/div[3]/table/tbody/tr/td[1]/div/div/div[1]/div/table/tbody/tr/td[1]/input")
dodkatces = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/fieldset[1]/div/div/div[3]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/em/button")
nepocestikat = []
for i in range(0,len(cestice)):
    while check_exists_by_id("x-auto-30") is True:
        time.sleep(0.1)
    else:
        brkatces.clear()
        brkatces.send_keys(cestice[i])
        dodkatces.click()
        while check_exists_by_id("x-auto-30") is True:
            time.sleep(0.1)
        else:
            if check_exists_by_class("x-window.x-window-dlg") is True:
                makni = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div/div/div[4]/div[2]/div[2]/div/div/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[2]/em/button")
                nepocestikat.append(cestice[i])
                makni.click()
            else:
                pass
for i in range(0,len(cestice)):
    if cestice[i].startswith("*"):
            cestice[i] = cestice[i].replace("*","")
            cestice[i] = cestice[i]+" ZGR"
    else:
        pass

glavknjig = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/fieldset[3]/div/div/div[1]/div[1]/div/input")
glavknjig.send_keys(input("Glavna knjiga: "))
glavknjig.send_keys(Keys.ENTER)
brojzkcest = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/fieldset[3]/div/div/div[2]/table/tbody/tr/td[1]/div/div/div[1]/div/table/tbody/tr/td[1]/input")
dodkatceszk = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/form/fieldset[3]/div/div/div[2]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/em/button")
time.sleep(1)
nepocestizk=[]
for i in range(0,len(cestice)):
    while check_exists_by_id("x-auto-30") is True:
        time.sleep(0.1)
    else:
        brojzkcest.clear()
        brojzkcest.send_keys(cestice[i])
        dodkatceszk.click()
        while check_exists_by_id("x-auto-30") is True:
            time.sleep(0.1)
        else:
            if check_exists_by_class("x-window.x-window-dlg") is True:
                makni2 = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div/div/div[4]/div[2]/div[2]/div/div/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[2]/em/button")
                nepocestizk.append(cestice[i])
                makni2.click()
            else:
                pass
print("Nepostojece cestice u katastru:")
print(nepocestikat)
print("Nepostojece cestice u ZK:")
print(nepocestizk)



