from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException


class TypeRacerBot:
    def __init__(self, driver, is_private, link, wpm=70):
        self.driver = driver
        self.is_private = is_private
        self.wpm = wpm

        self.link = link
        self.driver.get(self.link)

        sleep(2)

        if self.is_private:
            while not self.can_join_race():
                pass

            self.enter_private_race()

        else:
            self.enter_race()

        sleep(2)
        while not self.has_started():
            pass

        self.type_text(self.get_text())

    def enter_race(self):
        """ Click the link to enter a new race """
        self.driver.find_element_by_partial_link_text('Enter a typing race').click()

    def enter_private_race(self):
        """ Click the link to enter a new race """
        self.driver.find_element_by_partial_link_text('join race').click()

    def race_again(self):
        """ Click the link to race again """
        self.driver.find_element_by_partial_link_text('Race Again').click()

    def has_started(self):
        """ Returns whether the race has started or not """
        return self.driver.find_element_by_css_selector(
            'table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td > input'
        ).is_enabled()

    def can_join_race(self):
        """ Returns whether the cool-down between private races has ended """
        return len(self.driver.find_elements_by_partial_link_text('join race')) > 0

    def get_text(self):
        """ Returns the text you are supposed to type """
        return self.driver.find_elements_by_css_selector(
            'table > tbody > tr:nth-child(2) > td > table > tbody'
            ' > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div > div'
        )[3].text

    def type_text(self, text):
        """ Types the text with an average WPM of the parameter words_per_minute. """

        textbox = self.driver.find_element_by_css_selector(
            'table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td > input'
        )

        words = text.split()

        if self.wpm != 0:
            pause_time = 60 / self.wpm
        else:
            pause_time = 0

        for word in words:
            textbox.send_keys(word + ' ')

            if pause_time != 0:
                sleep(pause_time)


def main():
    is_private = input('Is the race private? (y/n): ').lower() == 'y'

    if is_private:
        link = input('Please enter the link of the race: ')
    else:
        link = 'https://play.typeracer.com'

    wpm = int(input('Please enter the WPM you would like (0 for max speed): '))

    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome('chromedriver.exe', options=options)

    while True:
        try:
            TypeRacerBot(driver, is_private, link, wpm)
        except UnexpectedAlertPresentException:
            pass

        print()
        input('Press enter to start new race')
        wpm = int(input('Please enter the WPM you would like (0 for max speed): '))


if __name__ == '__main__':
    main()
