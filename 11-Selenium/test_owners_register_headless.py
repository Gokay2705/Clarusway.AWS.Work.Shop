from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import os

driver = webdriver.Chrome(executable_path="/Users/home/Desktop/chromedriver")

APP_IP = os.environ['MASTER_PUBLIC_IP']
url = "http://"+APP_IP.strip()+":8080/"

driver.get(url)
sleep(2)

owners_link = driver.find_element_by_link_text("OWNERS")
owners_link.click()
sleep(2)

all_link = driver.find_element_by_link_text("REGISTER")
all_link.click()
sleep(2)

# Register new Owner to Petclinic App
fn_field = driver.find_element_by_name('firstName')
fn = 'Matt' + str(random.randint(0, 100))
fn_field.send_keys(fn)
sleep(1)

fn_field = driver.find_element_by_name('lastName')
fn_field.send_keys('Clarusway')
sleep(1)

fn_field = driver.find_element_by_name('address')
fn_field.send_keys('Ridge Corp. Street')
sleep(1)

fn_field = driver.find_element_by_name('city')
fn_field.send_keys('McLean')
sleep(1)

fn_field = driver.find_element_by_name('telephone')
fn_field.send_keys('+1230576803')
sleep(1)

fn_field.send_keys(Keys.ENTER)
sleep(1)

# Wait 2 second to get updated Owner List
sleep(6)

# Verify that new user is added to Owner List
if fn in driver.page_source:
    print(fn, 'is added and found in the Owners Table')
    print("Test Passed")
else:
    print(fn, 'is not found in the Owners Table')
    print("Test Failed")
driver.quit()