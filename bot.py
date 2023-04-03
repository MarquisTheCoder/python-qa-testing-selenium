# base dependencies
import random
from time import sleep
from typing import List
from colored import fg, attr

# bot dependencies (custom)
from avoid import BotAvoidance
from indeed import Indeed

# driver dependency
import undetected_chromedriver as uc2

# selenium dependencies
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec


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


#class to handle all interactions with Indeed
class Bot:

    WINDOW_PAUSE_TIME: int = 1_000_000
    DEFAULT_TIMEOUT: int = 60

    

    # root of bot don't need an initialization so we start here
    def run() -> None:
        
        Bot.display_program_banner()

         #navigating to the initial login page
        chrome.get(Indeed.login_page_url)

        #displaying whats happening to admin
        Bot.show_where_bots_going(Indeed.login_page_url)

        #setting the window to fullscreen
        chrome.maximize_window()

        # wait until the host logs in to bypass the login page
        Bot.wait_for_manual_user_login(chrome)

        # starts the actual search function and applications
        Bot.start_application_search_loop(chrome)

    def display_program_banner() -> None:
        print("""
    \n\n
    _____  ________   ________  _______   _______   ________  ________  ________  ________  _______   ________
    \n
          ____          ____
    |oooo|        |oooo|
    |oooo| .----. |oooo|
    |Oooo|/\_||_/\|oooO|
    `----' / __ \ `----'
    ,/ |#|/\/__\/\|#| \,
   /  \|#|| |/\| ||#|/  \
  / \_/|_|| |/\| ||_|\_/ \
 |_\/    o\=----=/o    \/_|
 <_>      |=\__/=|      <_>
 <_>      |------|      <_>
 | |   ___|======|___   | |
//\\  / |O|======|O| \  //\\
|  |  | |O+------+O| |  |  |
|\/|  \_+/        \+_/  |\/|
\__/  _|||        |||_  \__/
      | ||        || |
     [==|]        [|==]
     [===]        [===]
      >_<          >_<
     || ||        || ||
     || ||        || ||
     || ||        || ||    -- Jay Thaler 
   __|\_/|__    __|\_/|__
  /___n_n___\  /___n_n___\
 \n\n



 ___  ________   ________  _______   _______   ________  ________  ________  ________  ________  _______   ________     
|\  \|\   ___  \|\   ___ \|\  ___ \ |\  ___ \ |\   ___ \|\   __  \|\   __  \|\   __  \|\   ____\|\  ___ \ |\   __  \    
\ \  \ \  \\ \  \ \  \_|\ \ \   __/|\ \   __/|\ \  \_|\ \ \  \|\  \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|\ \  \|\  \   
 \ \  \ \  \\ \  \ \  \ \\ \ \  \_|/_\ \  \_|/_\ \  \ \\ \ \   ____\ \   __  \ \   _  _\ \_____  \ \  \_|/_\ \   _  _\  
  \ \  \ \  \\ \  \ \  \_\\ \ \  \_|\ \ \  \_|\ \ \  \_\\ \ \  \___|\ \  \ \  \ \  \\  \\|____|\  \ \  \_|\ \ \  \\  \| 
   \ \__\ \__\\ \__\ \_______\ \_______\ \_______\ \_______\ \__\    \ \__\ \__\ \__\\ _\ ____\_\  \ \_______\ \__\\ _\ 
    \|__|\|__| \|__|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|__|\|__|\|__|\_________\|_______|\|__|\|__|
                                                                                         \|_________|                   
                                                                                                                        
                                                                                                                        

  \n
  \t\tREADY TO DESTROY YOUR CHANCES OF NOT GETTING HIREEEEED!!!!!!
  \n
  \t\twritten by - MarquisTheCoder
  \n
  __________________________________________________________________________________________________________________________\n
  """)
        

    class input:

        # making it easy to enter text into the search bar
        def enter(web_element: WebElement):
            web_element.send_keys(Keys.RETURN)

        # typing slowley into the search bar
        def type_slowly_to_avoid_detection(element: WebElement, text: str): 
            for letter in text:
                element.send_keys(letter)
                sleep(random.uniform(0.01, 0.08))

    class page:

        # using chrome script to scroll to given y position 
        def y_scroll_to(driver: webdriver, y_position):
            driver.execute_script(f'window.scrollTo(0, {y_position})') 
        
        # using chrome script to scroll to given x position
        def x_scroll_to(driver: webdriver, x_position):
            driver.execute_script(f'window.scrollTo({x_position}, 0)')

        # allows the bot to save window state
        def get_current_window(drvier) -> webdriver:
            return drvier.current_window_handle

        # allows the bot to change window state
        def change_window(driver: webdriver, window_handle: webdriver) -> None:
            driver.switch_to.window(window_handle)

        # retrieves the result links to be used for the application
        def retrieve_results_on_page(driver: webdriver, page: int) -> List[WebElement]:
            Bot.page.y_scroll_to(driver, driver.get_window_size()['height'] * page)
            BotAvoidance.randomize_sleep_to_avoid_detection()
            return driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")

        def pause_page(time_in_minutes: int = 1) -> None:
            sleep(time_in_minutes * 60_000)

    # updating the admin on the bots movements
    def show_where_bots_going(route: str) -> None:
        print(f"\n robot is now navigating to ->  {fg(30)} {route} {attr(0)} \n" )    

    # to bypass Indeed login we need to do it manually
    def wait_for_manual_user_login(driver: webdriver) -> None:  

        # settings how long the wait object will wait. minute by default
        wait: WebDriverWait = WebDriverWait(driver, Bot.DEFAULT_TIMEOUT)

        # finding the homepage button after login to confirm successful login
        home_logo: WebElement = wait.until(ec.presence_of_element_located((By.XPATH, Indeed.selectors.xpath.home_logo)))

        # navigating to the home page
        home_logo.click()
    
    # after user login we will start the search for our jobs and get the results
    def start_application_search_loop(driver: webdriver):

        #defines how long the wait object will wait. minute by default
        wait: WebDriverWait = WebDriverWait(driver, Bot.DEFAULT_TIMEOUT)

        #wait until the search bar element is visible by the ID which was saved in the Indeed data class
        search_bar = wait.until(ec.visibility_of_element_located((By.ID, Indeed.selectors.ids.main_searchbar_input))) 

        # randomizing the delay between each search
        BotAvoidance.randomize_sleep_to_avoid_detection()

        # scrolls to look at jobs to mimic average user behaviour
        Bot.page.y_scroll_to(driver, 400)
        Bot.page.y_scroll_to(driver, 0)

        # randomizing the delay between each typed character to mimic human typing
        Bot.input.type_slowly_to_avoid_detection(search_bar, Indeed.positions[0])
 
        # randomizing the delay between each search
        BotAvoidance.randomize_sleep_to_avoid_detection()

        Bot.input.enter(search_bar)

        # saving root window to be returned to later after navigating to all applications
        current_window: str = Bot.page.get_current_window(driver)
        print(f"\n root window hash -> {fg(30)} {current_window}  {attr(0)}")

        # list will contain all posting links
        all_job_posting_applications: List[str] = []

        # this list will be used to memoize the results of the search
        all_job_posting_visited_applications: List[str] = []

        # retrieving the result links to be used for the navigating to the application pages
        all_job_posting_links_on_page: List[WebElement] = Bot.page.retrieve_results_on_page(driver, 2)
         
        for job_posting_link in all_job_posting_links_on_page:
             Bot.show_where_bots_going(job_posting_link.get_attribute("href"))

        # pauses the page for an hour to get the developer time to inspect site code
        Bot.page.pause_page(time_in_minutes = 60)