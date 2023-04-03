#!/usr/bin/python3

# general dependencies
import random
from time import sleep
from typing import List
from colored import fg, attr

# bot dependencies (custom)
from .bot_manipulation import BotManipulation
from .display import display_program_banner as banner
from .avoid import BotAvoidance
from .indeed import Indeed
from .driver import chrome

# selenium dependencies
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec


#class to handle all interactions with Indeed
class IndeedBot(BotManipulation):

    #constants for the bot
    DEFAULT_TIMEOUT: int = 60
    WINDOW_PAUSE_TIME: int = 1_000_000


    def run() -> None: 
        banner() 
        chrome.get(f"{Indeed.login_page_url}&radius=100")
        IndeedBot.show_where_bots_going(Indeed.login_page_url)
        chrome.maximize_window()
        IndeedBot.wait_for_manual_user_login(chrome)
        IndeedBot.start_application_search_loop(chrome)
 

    def show_where_bots_going(route: str) -> None:
        print(f"\n robot is now navigating to ->  {fg(30)} {route} {attr(0)} \n" )    


    def wait_for_manual_user_login(driver: webdriver) -> None:  

        # settings how long the wait object will wait. minute by default
        wait: WebDriverWait = WebDriverWait(driver, IndeedBot.DEFAULT_TIMEOUT)

        # finding the homepage button after login to confirm successful login
        home_logo: WebElement = wait.until(ec.presence_of_element_located((By.XPATH, Indeed.selectors.xpath.home_logo)))

        # navigating to the home page
        home_logo.click()


    def start_application_search_loop(driver: webdriver):

        #defines how long the wait object will wait. minute by default
        wait: WebDriverWait = WebDriverWait(driver, IndeedBot.DEFAULT_TIMEOUT)

        #wait until the search bar element is visible by the ID which was saved in the Indeed data class
        search_bar = wait.until(ec.visibility_of_element_located((By.ID, Indeed.selectors.ids.main_searchbar_input))) 

        # randomizing the delay between each search
        BotAvoidance.randomize_sleep_to_avoid_detection()

        # scrolls to look at jobs to mimic average user behaviour
        IndeedBot.page.y_scroll_to(driver, 400)
        IndeedBot.page.y_scroll_to(driver, 0)

        # randomizing the delay between each typed character to mimic human typing
        IndeedBot.input.type_slowly_to_avoid_detection(search_bar, Indeed.positions[0])
 
        # randomizing the delay between each search
        BotAvoidance.randomize_sleep_to_avoid_detection()

        IndeedBot.input.enter(search_bar)

        # saving root window to be returned to later after navigating to all applications
        current_window: str = IndeedBot.page.get_current_window(driver)
        print(f"\n root window hash -> {fg(30)} {current_window}  {attr(0)}")

        # list will contain all posting links
        all_job_posting_applications: List[str] = []

        # this list will be used to memoize the results of the search
        all_job_posting_visited_applications: List[str] = []

        # retrieving the result links to be used for the navigating to the application pages
        all_job_posting_links_on_page: List[WebElement] = IndeedBot.page.retrieve_results_on_page(driver, 2)
         
        for job_posting_link in all_job_posting_links_on_page:
             IndeedBot.show_where_bots_going(job_posting_link.get_attribute("href"))
             all_job_posting_applications.append(job_posting_link.get_attribute("href"))


        # pauses the page for an hour to get the developer time to inspect site code
        IndeedBot.page.pause_page(time_in_minutes = 60)
