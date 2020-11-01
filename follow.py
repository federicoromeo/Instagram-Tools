import errno, os, getpass
from selenium import webdriver
from time import sleep
from datetime import datetime
#import telepot

#TOKEN = "1210505790:AAFOsOXEgtM_ArwkZOi3AFqWACQxgnKraig"
#bot = telepot.Bot(TOKEN)
#print("Bot ready...")
#content_type, chat_type, chat_id = 0,0,0

#def handle(msg):
#    content_type, chat_type, chat_id = telepot.glance(msg)
#    #print(content_type, chat_type, chat_id)
#    bot.sendMessage(chat_id, "Enter your username and password separated by - : ")
#    bot.sendMessage(chat_id, "You have 10 seconds, hurry up! Then just wait")
#    bot.sendMessage(chat_id, "example:      user - psw")
#    sleep(10)
#    account = msg['text'].split("-")
#    user = account[0].strip()
#    password = account[1].strip()
#    print(user)
#    print(password)
#    bot.sendMessage(chat_id, "Processing...")
#    my_bot = InstaBot(user,password)

def dir_creation():
    now = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
    mydir = os.path.join(os.getcwd(),now)
    try:
        os.mkdir(mydir)
        return mydir
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise  # This was not a "directory exist" error..

def file_writing(list, path, filename):
    with open(os.path.join(path, filename), 'w') as d:
        d.write(str(len(list)))
        d.write("\n")
        for el in list:
            d.write(el + "\n")

class InstaBot:

    def __init__(self, username, psw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.psw = psw
        self.driver.get("https://instagram.com")
        sleep(2)
        # login
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")\
            .click()
        # username
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        # password
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(psw)
        #submit
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        try:
            # cookies not now
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
                .click()
            sleep(2)
            # notifications not now
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")\
                .click()
            sleep(2)
            self.get_unfollowers()
        except Exception as e:
            print(e)
            #bot.sendMessage(chat_id, "You entered invalid details..")

    def get_unfollowers(self):

        path = dir_creation()

        #my account
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img".format(self.username))\
            .click()
        # profile
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div".format(self.username))\
            .click()
        sleep(2)

        # following
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        file_writing(following, path, "following.txt")
        print("Done with the following")

        # followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        file_writing(followers, path, "followers.txt")
        print("Done with the followers")

        # not_following_back
        not_following_back = [user for user in following if user not in followers]
        file_writing(not_following_back, path, "not_following_back.txt")
        print("Done with the not following back")

        #bot.sendMessage(chat_id, "UNFOLLOWERS:")import stdiomask
        #for el in not_following_back:
        #bot.sendMessage(chat_id, el)

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names


user_name = "federicoromeo98" #input("Enter your username : ")
password = "mmmmmmmmmmeo98"   #input("Enter your password : ")
#password = getpass.getpass('Password :: ')

my_bot = InstaBot(user_name,password)


#bot.message_loop(handle)

#while 1:
#    sleep(1)
