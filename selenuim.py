from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s:%(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TOTAL_PAGE = 10
TIME_OUT = 10

browser = webdriver.Chrome()
wait = WebDriverWait(browser,TIME_OUT)

def scrape_page(url,condition,locator):
    logging.info('scrape url %s',url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error while %s',url,exc_info=True)

def scrape_index(page):
    url = INDEX_URL.format(page=page)
    scrape_page(url,condition=EC.visibility_of_all_elements_located,locator=(By.CSS_SELECTOR,'#index.item'))

def parse_index():
    elements = browser.find_elements_by_css_selector('#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL,href)
def scrape_detail(url):
    scrape_page(url,condition=EC.visibility_of_element_located,locator=(By.TAG_NAME,'h2'))

def paese_detail():
    url = browser.current_url
    name = browser.find_elements_by_tag_name('h2').text
    return {'name':name}

def main():
    try:
     for page in range(1,TOTAL_PAGE):
       scrape_index(page)
       detail_urls=parse_index()
       logging.info('details url %s',list(detail_urls))
     '''  for detail_url in list(detail_urls):
        scrape_detail(detail_url)
        detail_data = paese_detail()
        logging.info('%s',detail_data)
'''


    finally:
        browser.close()



