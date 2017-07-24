"""
Python script to download Bing daily wallpaper automatically and set it as the desktop wallpaper in Windows systems.

This script was developed using Python 2.7.13

@author: Harsh Khatore
Date: 24 July, 2017

"""

# Modules not present by-default in Python 2.7.13. Install these seperately before using this script.
# 1. requests

from PIL import Image
import urllib
import installation
import json                                         # For using json functionalities
try:
    import requests                                 # For using HTTP and HTTPS service to access a webpage
except ImportError:
    installation.install()
    import requests
from requests.exceptions import ConnectionError     # For ConnectionError handling
import os                                           # For using operating system services
import datetime                                     # For using date for naming the wallpaper image
import time                                         # For using sleep()
import ctypes                                       # For calling functions outside the Python environment

def get_bing_image_url():
    """ Returns the URL of Bing image of the day """
        
        #Explanation begin - for understanding
            #r = requests.get("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
    
            #Converts the response object into json object
            #obj = r.json()
            
            #Since, json is a dictionary, fetches the value for 'images' key and returns a list containing a dictionary inside it
            #obj = obj['images']                        
            
            #Fetches the image url from the list using the 'url' key
            #obj = obj[0]['url']                        
        #Explanation end
        
    try:    
        url = "http://bing.com"+requests.get("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US").json()['images'][0]['url']
        print url
        return url
    except ConnectionError as e:
        return "Connection Error",e
    
    
def get_image_path():
    """ Returns the local path of the downloaded image 
        
        Final path -> "C:\Users\<username>\Desktop\bing\'bing-<date>.jpg' "
    """
    time = datetime.datetime.now()                                  # Getting date and time of the day
    wpName = 'bing ' + time.strftime('%d-%m-%y') + '.jpg'           # Setting the wallpaper name
        
    username = os.environ.get("USERNAME")                           # Setting target directory as a folder in desktop
    targetDir = 'C:\Users\\' + username + '\Desktop\\bing\\'
    if not os.path.exists(targetDir):                               # Checking if the directory exists or not. If not, make a new directory
        os.makedirs(targetDir)
    
    imagePath = targetDir + wpName                                  # Final path 
    url = get_bing_image_url()                                      # Get the image link form the 'get_bing_image_url' function
    if set(url.split()) == set("Connection Error".split()):
        return False
    
    urllib.urlretrieve(url, imagePath)                           # Download the image to the path
	
    if not os.path.exists(imagePath):                               # Checking if the directory exists or not. If not, make a new directory
        print "Image not present"

    return imagePath


def set_wallpaper():
    """ Sets the system's wallpaper as Bing image of the day """
    
    path = get_image_path()                                         # Get the image local path from 'get_image_path' function
    if path == False:
        return False
    
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)
    
    
if __name__ == "__main__":
    result = set_wallpaper()
    if result == False:
        print "Task could not be completed, please try again."
