from selenium import webdriver
from time import sleep
import requests
from selenium.webdriver.common.by import By

bro = webdriver.Chrome()
bro.get('https://music.163.com/#/discover/toplist')
bro.switch_to.frame('g_iframe')
songs = bro.find_elements(By.XPATH,'//table[@class="m-table m-table-rank"]/tbody/tr')
for song in songs:

 name = song.find_element(By.XPATH,'.//span[@class="txt"]/a/b').get_attribute('title')
 herf = song.find_element(By.XPATH,'.//a').get_attribute('href')
 song_id = herf.split('=')[1]
 print(name,herf)
 headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
 base_url = "http://music.163.com/song/media/outer/url?id="  # 歌曲播放页面，只需传递歌曲ID
 path = "D:/python网络爬虫/pythonProject/实战项目/项目/歌曲/"  # 歌曲保存路径
 response = requests.get(base_url + song_id, headers=headers)  # 发送请求
 with open(path + name + ".mp3", mode="wb") as fp:
  fp.write(response.content)
 print("歌曲：{} 下载完毕!".format(name))
 sleep(1)
bro.quit()
