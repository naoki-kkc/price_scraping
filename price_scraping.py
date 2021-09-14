import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def exec(target_url, target_xpath):

    # init web driver
    # note: chromedriver.exe in current directory
    driver = webdriver.Chrome()

    try:
        # open url
        driver.get(target_url)
        time.sleep(1)

        # get element by XPath
        price = driver.find_element(By.XPATH, target_xpath)

        # get text
        raw_text = price.text

        # modify text
        mod_text = ''.join(raw_text.split(',')) # remove comma
        mod_text = mod_text[:len(mod_text) - 1] # remove "円"

        print("-- success --------")
        print("target_url   : " + target_url)
        print("target_xpath : " + target_xpath)
        print("text(raw)    : " + raw_text)
        print("text(modify) : " + mod_text)
    
    except:
        print("!! error -!!!!!!!!!")

    # close driver
    driver.close()
    driver.quit()

    return mod_text
