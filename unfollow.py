from selenium import webdriver

from time import *
from selenium.common.exceptions import NoSuchElementException
        
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

# Establish chrome driver and go to report site URL
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, ' ', text)


url = "https://facebook.com"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\User Data\\test")

driver = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe', chrome_options=options)

my_file = open("usernames.txt", "r")
content_list = my_file.readlines()
final = []
for i in content_list:
    final.append(i.rstrip('\n'))

final2 = final

print("there are : " + str(len(final)) + " accounts.")
cnt = 0
for i in final:
    ddd = True
    driver.get("https://www.instagram.com/" + i)
    sleep(2)
    if(check_exists_by_xpath("//button[@class='_acan _aiit _acap _aijb _acat _aj1-']")):
        button2 = driver.find_element_by_xpath("//button[@class='_acan _aiit _acap _aijb _acat _aj1-']")
        button2.click()
        sleep(.2)
        button3 = driver.find_element_by_xpath("//button[@class='_a9-- _a9-_']")
        button3.click()
        print(i + " unfollowed " + str(cnt))
        cnt+=1
        sleep(1)
        driver.refresh()
        sleep(2)
        if(not check_exists_by_xpath("//button[@class='_acan _aiit _acap _aijb _acat _aj1-']")):
            final2.remove(i)
        else:
            print("You've reached your limit.")
            break
    else:
        print(i + " is already unfollowed.")
        final2.remove(i)



driver.close()
print("there are : " + str(len(final2)) + " accounts left.")
textfile = open("usernames.txt", "w")
for element in final2:
    textfile.write(element + "\n")
textfile.close()
#driver.delete_all_cookies()