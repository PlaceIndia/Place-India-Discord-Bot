from selenium import webdriver
import time
import pytesseract
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import credentials  # this is a file with the sensitive credentials and paths


def Screenshoter():
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('headless')
    edge_options.add_argument('disable-gpu')
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = Edge(executable_path=credentials.webdrive_path,
                  options=edge_options)

    driver.get('https://www.reddit.com/r/place/?cx=307&cy=315&px=200')
    time.sleep(5)
    driver.get_screenshot_as_file('yo.png')
    driver.quit()


def Screenshoter2():
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('headless')
    edge_options.add_argument('disable-gpu')
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = Edge(executable_path=credentials.webdrive_path,
                  options=edge_options)

    driver.get('https://www.reddit.com/r/place/?cx=166&cy=1216&px=100')
    time.sleep(5)
    driver.get_screenshot_as_file('yo2.png')
    driver.quit()
