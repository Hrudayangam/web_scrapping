# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 03:08:51 2020

@author: hruda
"""
import time
import os 
import selenium
from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException  
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
#from selenium.webdriver.support.u as ui
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path=r'C:\\Users\\local\\bin\\chromedriver.exe')
#driver = webdriver.Chrome() 
driver.get('https://www.youtube.com/results?search_query=science')