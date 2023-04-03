#!/usr/bin/python3

# bot dependency
from .avoid import BotAvoidance

# driver dependency
import undetected_chromedriver as uc2

#selenium dependency
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# selenium dependencies
chrome_options: Options = Options()

#detaches code execution from browser functionality
chrome_options.add_experimental_option("detach", True)

# Exclude the collection of enable-automation switches 
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
chrome_options.add_experimental_option("useAutomationExtension", False) 

# Adding argument to disable the AutomationControlled flag 
chrome_options.add_argument("--disable-blink-features=AutomationControlled") 

#utilizing randomizer to automate user-agent generation 
chrome_options.add_argument(f'user-agent={BotAvoidance.return_mac_user_agent()}')

#setting the initial chromedriver to be used
chrome: webdriver = uc2.Chrome(version_main=111, chrome_options=chrome_options)
 
# Changing the property of the navigator value for webdriver to undefined 
chrome.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
