import errno, os, getpass
from selenium import webdriver
import keyboard
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from datetime import datetime
from faker import Faker as faker
from random import randrange
from threading import Thread, Lock
import pdb

usernames = []
passwords = []
emails    = []

aux_email = ""
current_email = ""
autenthication_code = ""

def print_file(username, password, email):
    #ok = False
    #if ok:
    with open(os.path.join("C:/Users/feder/Desktop/insta/fake/", "accounts.txt"), 'a') as f:
        f.write(username+username + " " + password + " " + email + "\n")
    usernames.append(username+username)
    passwords.append(password)
    emails.append(email)

def insta_bot(self):
    browser = webdriver.Chrome()
    browser.get("https://instagram.com")
    sleep(2)
    # accept cookies
    browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")\
        .click()
    print("cookies")
    # register
    browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a/span")\
        .click()
    print("register")
    sleep(1)
    fake = faker()
    # email
    #print("current_email: " + str(current_email))
    browser.find_element_by_xpath("//input[@name=\"emailOrPhone\"]")\
        .send_keys(aux_email)
    print("email")
    # name and surname
    name = fake.name()
    browser.find_element_by_xpath("//input[@name=\"fullName\"]")\
        .send_keys(name)
    print("name")
    # username
    username = fake.user_name() + str(randrange(10)) + str(randrange(10))  #johnwic98 x2
    browser.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(username+username)
    print("username")
    # password
    password = fake.password()
    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input")\
        .send_keys(password)
    print("password")
    # submit
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button")\
        .click()
    print("submit")
    sleep(3)


    # change date and select valid year
    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select")\
        .send_keys("2001")
    print("date")
    # submit
    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[6]/button")\
        .click()
    print("go on")
    sleep(3225)

    #print_file(username, password, "vabdullahejazzafe@devcard.com")

    sleep(10)

    # switch tab
    self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

    # put autenthication code
    #driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[2]/form/div/div[1]/input")\
    #    .send_keys(autenthication_code)
    # submit
    #driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[2]/form/div/div[2]")\
    #    .click()

            #cose

    sleep(1)

def fake_email(self):

    browser = webdriver.Chrome()
    browser.get("https://it.emailfake.com")
    sleep(2000)

    #get current email
    current_email = browser.find_element_by_xpath("/html/body/div[3]/div/div/b/span").text

    browser.refresh()
    sleep(15)
    browser.refresh()
    #get autenthication code
    autenthication_code = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[2]/div[4]/div[3]/div").text
    sleep(1)


class InstaCreator:

    def __init__(self):
        pass

    def run(self):

        try:
            chrome_options = Options()
            chrome_options.add_argument("user-data-dir=selenium")
            browser = webdriver.Chrome(options=chrome_options)

            #first tab
            #browser.execute_script("window.open('http://instagram.com', 'insta_page');")
            #insta_page = browser.window_handles[0]
            #sleep(3)

            #second tab
            #browser.execute_script("window.open('http://it.emailfake.com', 'fakeemail_page');")
            #fakeemail_page = browser.window_handles[1]
            #sleep(333)

            browser.get("http://it.emailfake.com")
            #fakeemail_page = browser.window_handles[0]
            sleep(5)

            #get current email
            current_email = browser.find_element_by_xpath("/html/body/div[3]/div/div/b/span").text
            print(current_email)

            #second tab
            #browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
            browser.get("http://instagram.com")
            #insta_page = browser.window_handles[1]

                #browser.execute_script("window.open('http://instagram.com', 'insta_page');")
            #insta_page = browser.window_handles[0]
            sleep(5)

            #browser.switch_to.window("insta_page")
            #sleep(2)

            # accept cookies
            #browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")\
            #    .click()
            #print("cookies")
            # register
            browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a/span")\
                .click()
            print("register")

            sleep(3)
            fake = faker()
            # email
            browser.find_element_by_xpath("//input[@name=\"emailOrPhone\"]")\
                .send_keys(current_email)
            print("email")
            # name and surname
            name = fake.name()
            browser.find_element_by_xpath("//input[@name=\"fullName\"]")\
                .send_keys(name)
            print("name")
            # username
            username = fake.user_name() + str(randrange(10)) + str(randrange(10))  #johnwic98 x2
            browser.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username+username)
            print("username")
            # password
            password = fake.password()
            browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input")\
                .send_keys(password)
            print("password")
            # submit
            browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button")\
                .click()
            print("submit")
            sleep(3)

            # change date and select valid year
            browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select")\
                .send_keys("2001")
            print("date")
            # submit
            browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[6]/button")\
                .click()
            print("go on")
            sleep(1)

            #keyboard.press("ctrl+t")
            #keyboard.press("ctrl+tab")
            #browser.switch_to.window(window_name=fakeemail_page)

            #ActionChains(browser).key_down(Keys.SHIFT).send_keys('t').key_up(Keys.SHIFT).perform()

            #browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

            actions = ActionChains(browser)
            about = browser.find_element_by_link_text('About')
            actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()
            browser.switch_to.window(browser.window_handles[-1])
            browser.get("http://it.emailfake.com")

            #browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            #browser.switch_to.window(browser.window_handles[-1])
            #sleep(20)
            #browser.refresh()

            autenthication_code = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[2]/div[4]/div[3]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]"))).text
            print(autenthication_code)
            #autenthication_code = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[2]/div[4]/div[3]/div").text
            sleep(5)
            browser.close()

            #browser.get("https://www.instagram.com")
            sleep(4)
            #browser.switch_to.window("insta_page")

            browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[2]/form/div/div[1]/input")\
                .send_keys(autenthication_code)
            browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[2]/form/div/div[2]")\
                .click()

            sleep(7999)

        except Exception as e:
            print(e)



if __name__ == '__main__':
    insta_bot = InstaCreator()
    insta_bot.run()
