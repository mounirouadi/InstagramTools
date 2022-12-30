from selenium import webdriver
import sys
from time import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
        
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:
        return False
    return True



# Establish chrome driver and go to report site URL
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, ' ', text)


if(len(sys.argv)>2):
    user = sys.argv[1]
    passw = sys.argv[2]
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\User Data\\test")
    options.add_argument('--disable-logging') 
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe', options=options)
    driver.get("https://instagram.com")
    driver.delete_all_cookies()
    driver.refresh()
    sleep(2)

    username = driver.find_element(By.CSS_SELECTOR,"input[name='username']")
    username.clear()
    username.send_keys(user)

    password = driver.find_element(By.CSS_SELECTOR,"input[name='password']")
    password.clear()
    password.send_keys(passw)
    button = driver.find_element(By.XPATH,"//button[@type='submit']")
    button.click()
    while(not check_exists_by_xpath("//button[@class='_acan _aiit _acap _aijb _acas _aj1-']")):
        pass
    print("Login to ",user,"is successful.")

    driver.quit()
else:
    print("Enter both your Instagram username and password!")