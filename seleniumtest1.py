

from selenium import webdriver

# important : dont save the file as Selenium.py (it will be as a module and there may be original module with the same name).

#if you want to use chrome:

#from webdriver_manager.chrome import ChromeDriverManager
#driver= webdriver.Chrome(ChromeDriverManager().install())
#driver.get("https:\\automatetheboringstuff.com")
# refer to :  https://www.youtube.com/watch?v=5Teelzjzl0s


# here we will use Firefox:

from webdriver_manager.firefox import GeckoDriverManager # the webdriver_manager will download the browser driver for any browsers version 

driver1 = webdriver.Firefox(executable_path=GeckoDriverManager().install()) # to install the browser driver
driver1.get("https://nostarch.com/automatestuff2")# to get the web page
# to find the selector of the button you need to click on :
searchElem= driver1.find_element_by_css_selector('div.logo-wrapper:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
searchElem.send_keys('games')# to send the key , text you want to search it.
searchElem.submit()# to click the search button and start search engine

#---------------------------------------------

# how to click on chapter0 button

#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver.get("https:\\automatetheboringstuff.com")
#elem = driver.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)') # it will get the selectror of chapter 0
#elem.click()# it will click on chapter0 button
#print(elem)


#----------------------------------------------

#another way: to write something in search and press the search button:

#driver1 = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver1.get("https://nostarch.com/automatestuff2")
#searchElem= driver1.find_element_by_css_selector('div.logo-wrapper:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
#searchElem.send_keys('games')
#Cliking_searchElem = driver1.find_element_by_css_selector('div.logo-wrapper:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2) > button:nth-child(1)')
#Cliking_searchElem.click()


# refer to :  https://www.youtube.com/watch?v=5Teelzjzl0s.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)



