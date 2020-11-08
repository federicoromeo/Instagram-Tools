from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from faker import Faker as faker
from selenium import webdriver
from random import randrange
from time import sleep
import pathlib, os


#account = input("Insert account name: ")
#account = "myAccount"
current_email = ""
autenthication_code = ""

def print_file(username, password, email):
    current_path = pathlib.Path().absolute()
    myuser = username + username
    with open(os.path.join(current_path + "/instagram_tools_accounts/", "accounts.txt"), 'a') as f:
        f.write(myuser + " " + password + " " + email + "\n")


if __name__ == '__main__':
    try:
        chrome_options = Options()
        #chrome_options.add_argument("--incognito")
        chrome_options.add_argument("user-data-dir=selenium")
        browser = webdriver.Chrome(options=chrome_options)
        browser.get("http://it.emailfake.com")
        sleep(2)

        #get current email
        current_email = browser.find_element_by_xpath("/html/body/div[3]/div/div/b/span").text
        print("\n")
        print(current_email)

        #second tab
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get("http://instagram.com")
        sleep(2)

        # accept cookies: not useful now because i already save cookies as default
        try:
            cookies = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
            cookies.click()
            print("cookies")
        except NoSuchElementException:
            pass

        # register
        browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a/span").click()
        print("register")
        sleep(2)

        fake = faker()

        # email
        browser.find_element_by_xpath("//input[@name=\"emailOrPhone\"]").send_keys(current_email)
        print("email")

        # name and surname
        name = fake.name()
        browser.find_element_by_xpath("//input[@name=\"fullName\"]").send_keys(name)
        print("name")

        # username        #todo: get better with trycatch
        username = fake.user_name() + str(randrange(10)) + str(randrange(10))  #johnwic98, then x2
        browser.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username+username)
        print("username")

        # password
        password = fake.password()
        browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input").send_keys(password)
        print("password")

        # submit
        browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button").click()
        print("submit")
        sleep(2)

        # change date and select valid year
        browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select").send_keys("2001")
        print("date")

        # submit
        browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[6]/button").click()
        print("submit")
        sleep(2)

        # back to the other tab
        browser.switch_to.window(browser.window_handles[0])
        browser.get("http://it.emailfake.com")
        print("switched page to wait code")

        # get autenthication_code
        autenthication_code = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[2]/div[4]/div[3]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]"))).text
        print("code: " + str(autenthication_code))

        browser.switch_to.window(browser.window_handles[1])
        sleep(2)

        code = "'" + autenthication_code + "'"
        browser.execute_script("document.getElementsByName('email_confirmation_code')[0].sendKeys("+ code +");")
        submit = browser.find_element_by_xpath('//button[@type="submit"]')
        browser.execute_script("arguments[0].click();", submit)



        # BUG here
        # BUG here
        # BUG here
        # BUG here
        # BUG here
        # BUG here
        # BUG here
        # BUG here
        # BUG here
        # BUG here



        response = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[2]/form/div/div[4]/div").text
        print(response)
    
        sleep(10)

        # ask new code
        #browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[1]/div[2]/div/button").click()

        # not now notifications
        browser.find_element_by_xpath("/html/body/div[4]/ div/div/div/div[3]/button[2]").click()
        print("notifications")
        sleep(1)

        # search for account
        browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div").send_keys(account)
        print("account")
        sleep(3)

        # click on account
        browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div").click()
        print("click on " + str(account))
        sleep(3)

        # click on first pic
        browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]").click()
        print("first pic")
        sleep(3)

        # like last *times* pics
        times = 0
        for times in range(10):
            # like pic
            browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg").click()
            # get description
            description = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span").text
            print("liked pic with description: [" + str(description) + "]")
            sleep(3)
            # next
            browser.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()

        # close pics
        browser.find_element_by_xpath("/html/body/div[5]/div[3]/button/div/svg/path").click()
        print("close pics")

        # settings
        browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()
        sleep(1)
        # exit account
        browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div").click()
        print("exited from " +str(account))
        sleep(3)

        print("Disconnecting...")
        browser.close()

    except Exception as e:
        print(e)
