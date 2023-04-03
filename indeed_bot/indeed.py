#!/usr/bin/python3

#____________________________________________________________________________#
#               ! < Public Service Announcement > !                          #
#----------------------------------------------------------------------------#
# I'm putting all of the elements I find on the indeed site 
# inside of a class so this bot can be easy to maintain and update 
# accordingly to the sites changes in the future. Many times
# bot creators are single minded and don't give their creations 
# any flexibility in their design. I'm starting out working against 
# this problem before it becomes a problem in the future. And if you choose
# to contribute to this pojects please approach the project with this mindset!
# Thank you! - MarquisTheCoder
#_____________________________________________________________________________#

import configparser
import json

parser = configparser.ConfigParser()
parser.read('project.toml')

#all usefule information for bot
class Indeed:

    #indeed data
    login_page_url: str = json.loads(parser.get("indeed","base_url"))
     
    #authentication data
    password:str = json.loads(parser.get("authentication", "password"))
    username:str = json.loads(parser.get("authentication", "username"))
    positions: list = json.loads(parser.get("positions", "developer"))
    email:str = json.loads(parser.get("authentication", "email"))

    # useful resuable selector variables for driver element searches
    # these are organized and put into class variables to make this bot easier to maintain and update
    class selectors: 

        class xpath:
            captcha_iframe:str = '/html/body/div[1]/div[2]/main/div/div/div[2]/div/form/div[2]/div/iframe'
            home_logo:str = '/html/body/nav/div/div/div[1]/a[1]' 

        class ids:
            authentiication_password_fallback:str  = "auth-page-google-password-fallback" 
            h_captcha_authentication_checkbox:str = "checkbox"
            google_signin:str = "gsuite-login-google-button"
            main_searchbar_input:str = "text-input-what"

        class names:
            email:str = "__email"
            password:str = "__password"

  