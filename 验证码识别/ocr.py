import re
from selenium.webdriver.support.wait import WebDriverWait
import numpy as np
import tesserocr
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from io import BytesIO
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from retrying import retry

bro = webdriver.Chrome()
bro.maximize_window()
#for i in range(12):
#@retry(stop_max_attempt_num=10,retry_on_result=lambda x:x is False)
bro.get('https://captcha7.scrape.center/')
bro.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div/div/div/form/div[1]/div/div/input').send_keys('admin')
bro.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div/div/div/form/div[2]/div/div/input').send_keys('admin')
captcha = bro.find_element(By.ID,'captcha')
#captcha = bro.find_element(By.XPATH,'//*[@id="header"]/div/div/div')
image = Image.open(BytesIO(captcha.screenshot_as_png))
image = image.convert('L')
array = np.array(image)
array = np.where(array > 165,255,0)
image = Image.fromarray(array.astype('uint8'))
#image.show()
result = tesserocr.image_to_text(image)
result = re.sub('[^A-Za-z0-9]','',result)
image.show()
bro.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div/div/div/form/div[3]/div/div/div[1]/div/input').send_keys(result)
bro.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div/div/div/form/div[4]/div/button').click()
print(result)
#try:
 #WebDriverWait(bro,10).until(EC.presence_of_element_located((By.XPATH,'//h2[contains(.,"登陆成功")]')))
sleep(3)
bro.close()
sleep(3)
 #return True
#except TimeoutException:
 #return False