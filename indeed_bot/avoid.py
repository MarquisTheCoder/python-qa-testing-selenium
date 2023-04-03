
from time import sleep
from random import uniform
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

# class to handle the anti fingerprinting algorithm of the Bot
class BotAvoidance: 

    # this bot uses chrome this is to avoid conflicts in fingerprinting 'story' 
    software_names = [SoftwareName.CHROME.value]

    # making sure the user agent OS is MAC
    operating_systems = [OperatingSystem.MAC.value]   
    
    #object for getting a random user agent
    user_agent_rotator = UserAgent(software_names=software_names, 
                                   operating_systems=operating_systems, 
                                   limit=100)
    # randoming user agent within the type of a mac computer because APPLE
    def return_mac_user_agent():
        return BotAvoidance.user_agent_rotator.get_user_agents()

    # trying to make sure Indeed doesnt detect our bot
    def randomize_sleep_to_avoid_detection(minimum_value: float = 1.1, maximum_value: float = 3.5) -> None:
        sleep(uniform(minimum_value, maximum_value))
    