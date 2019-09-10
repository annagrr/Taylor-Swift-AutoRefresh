from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def init_webdriver():
    #TODO:insert your driver path here! :)
    path = '/Users/AnnaGrr/Downloads/chromedriver'
    driver_path = path
    #Add AdBlock
    chop = webdriver.ChromeOptions()
    #chop.add_extension('adblockpluschrome-3.0.0.1921.crx')
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chop)
    return driver

#initialise webdriver
driver = init_webdriver()
driver.get('https://tickets.taylorswift.com/entry/activity/watch/music_video')
#to navigate page and click on stuff. change xpath !
xpath1 = '//*[@id="tcApprovalCheckbox"]'
xpath2 = '//*[@id="tm-signup"]'
driver.find_element_by_xpath(xpath1).click()
driver.find_element_by_xpath(xpath2).click()
#driver.implicitly_wait(30)

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="loginFrame"]'))
driver.find_element_by_xpath('//*[@id="login-input"]').send_keys('anna.greer@outlook.com')
driver.find_element_by_xpath('//*[@id="password-input"]').send_keys('Blerper8')
driver.find_element_by_xpath('//*[@id="login-btn"]').click()

#driver.implicitly_wait(30)

vid_xpath = {'lwymmd':'//*[@id="app-root"]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[5]/a',
             'lyric': '//*[@id="app-root"]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[7]/a',
             'mount': '//*[@id="app-root"]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[9]/a',
             'now': '//*[@id="app-root"]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[10]/a',
             'tasty': '//*[@id="app-root"]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[11]/a',
             'bts': '//*[@id="app-root"]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[6]/a'
             }

vid_time = {'lwymmd':4*60+20,
             'lyric': 3*60+40,
             'mount': 7*60+10,
             'now': 1*60+50,
             'tasty': 65,
             'bts': 35
             }


for i in range(50):
    for vid in vid_xpath:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, vid_xpath[vid])))
        driver.implicitly_wait(30)
        driver.find_element_by_xpath(vid_xpath[vid]).click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath('//*[@id="watch-video-frame"]').click()
        time.sleep(vid_time[vid])
        driver.find_element_by_xpath('//*[@id="app-root"]').click()
        print('played'+vid)
    i += 1
    
    
    