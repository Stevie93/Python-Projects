from selenium import webdriver
from secrets import pw
from time import sleep


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        print('Accessing URL')
        self.driver.get("https://instagram.com/")
        sleep(2)
        print('Success')
        print()

        print('Attempting login')
        self.driver.find_element_by_xpath(
            '//button[@type="button"]').click()
        self.driver.find_element_by_xpath(
            "//input[@name=\"email\"]").send_keys(username)
        self.driver.find_element_by_xpath(
            "//input[@name=\"pass\"]").send_keys(pw)
        self.driver.find_element_by_xpath(
            '//button[@type="submit"]').click()
        sleep(5)
        print('Success')
        print()

        print('Ignoring notification')
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(1)
        print('Success')
        print()

    def get_unfollowers(self):
        print('Opening Account')
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a').click()
        sleep(5)
        print('Success')
        print()

        print('Accessing following')
        sFollowing = self.driver.find_element_by_partial_link_text('following')
        sFollowing.click()
        following = self._get_names()
        print('Success')
        print()

        print('Accessing followers')
        sFollowers = self.driver.find_element_by_partial_link_text('followers')
        sFollowers.click()
        followers = self._get_names()
        print('Success')
        print()

        print('Fetching non followers')
        not_following_back = [
            user for user in following if user not in followers]
        print('Success')
        print()
        print(not_following_back)

        # def unfollow():
        #     for non_follower in not_following_back:
        #         self.driver.get("https://instagram.com/" + non_follower)
        #         sleep(3)
        #         self.driver.find_element_by_xpath(
        #             '/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
        #         self.driver.find_element_by_xpath(
        #             '/html/body/div[4]/div/div/div[3]/button[1]').click
        #         sleep(3)
        #         print(non_follower + ' has been unfollowed')
        #         sleep(1)

    def _get_names(self):
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script(""" arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names


my_bot = InstaBot('0203328141', pw)
my_bot.get_unfollowers()
# my_bot.get_unfollowers.unfollow()
