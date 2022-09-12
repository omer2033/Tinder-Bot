from selenium import webdriver
from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
FB_MAIL = "@hotmail.com"
FB_PASSWORD = "password"
chrome_driver_path = r"C:\Users\username\PycharmProjects\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.maximize_window()
driver.get(url="https://tinder.com/")
sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="t-1801132545"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')

login_button.click()
sleep(3)
facebook_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
sleep(2)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(FB_MAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)
sleep(1)

driver.switch_to.window(base_window)
print(driver.title)
sleep(5)

location = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
location.click()
sleep(1)

notif = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
notif.click()

cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

sleep(2)


like_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')

for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except ElementClickInterceptedException:
            no_thanks = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
            no_thanks.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
