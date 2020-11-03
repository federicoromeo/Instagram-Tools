from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from datetime import datetime
import errno, os, getpass
from time import sleep

def dir_creation():
    now = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
    mydir = os.path.join(os.getcwd(),now)
    try:
        os.mkdir(mydir)
        return mydir
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise Exception

def file_writing(list, path, filename, string):
    with open(os.path.join(path, filename), 'w') as f:
        f.write("The number of account that " + string + str(len(list)))
        f.write("\n")
        for el in list:
            f.write(el + "\n")

class InstaBot:

    def __init__(self, username, psw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.driver.get("https://instagram.com")
        sleep(2)
        print("\nLogging into Instagram...")
        # login
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        # username
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        # password
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(psw)
        #submit
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        try:
            # cookies not now
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
            sleep(2)
        except NoSuchElementException:  #wrong password
            response = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/p').text
            print(response)
            return
        # notifications not now
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()
        sleep(2)
        self.get_unfollowers()
        sleep(1)
        self.driver.close()
        return

    def get_unfollowers(self):
        path = dir_creation()
        #my account
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img".format(self.username)).click()
        # profile
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div".format(self.username)).click()
        # following
        sleep(3)
        print("Scrolling Following accounts...")
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self.get_names()
        file_writing(following, path, "following.txt", "you are following is: ")
        print("Done with the Following")
        # followers
        sleep(1)
        print("Scrolling Followers accounts...")
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self.get_names()
        file_writing(followers, path, "followers.txt", "are following you is: ")
        print("Done with the Followers")
        # not_following_back
        sleep(1)
        print("Scrolling Not Following Back accounts...")
        not_following_back = [user  for user in following  if user not in followers]
        file_writing(not_following_back, path, "not_following_back.txt", "are not following you back are: ")
        print("Done with the Not Following Back")
        return

    def get_names(self):
        sleep(2)
        #scroll_box = self.driver.find_element_by_class_name("isgrP")        #scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        scroll_box = self.driver.find_element_by_xpath('//div[@class="isgrP"]')
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text  for name in links  if name.text != '']
        sleep(2)
        # close button
        self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button').click()
        return names


username = input("Username :: ")
password = getpass.getpass("Password :: ")
#password = input("Enter your password : ")

my_bot = InstaBot(username,password)
