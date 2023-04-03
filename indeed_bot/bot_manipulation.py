
# general dependencies
import random
from typing import List
from time import sleep

# bot dependencies
from .avoid import BotAvoidance

# selenium dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

class BotManipulation:
     
    class input:

        # making it easy to enter text into the search bar
        def enter(web_element: WebElement):
            web_element.send_keys(Keys.RETURN)

        # typing slowley into the search bar
        def type_slowly_to_avoid_detection(element: WebElement, text: str): 
            for letter in text:
                element.send_keys(letter)
                sleep(random.uniform(0.01, 0.08))

        def search(query: str):
            pass

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
            BotManipulation.page.y_scroll_to(driver, driver.get_window_size()['height'] * page)
            BotAvoidance.randomize_sleep_to_avoid_detection()
            return driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")

        def pause_page(time_in_minutes: int = 1) -> None:
            sleep(time_in_minutes * 60_000)