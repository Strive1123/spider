import requests #爬取网页信息
import re #正则表达式获取信息
import logging #显示内容
from urllib.parse import urljoin #处理URL(拼接)
import json
from os import makedirs
from os.path import exists
import multiprocessing


RESULT_DIR ='results'#文件名
exists(RESULT_DIR) or makedirs(RESULT_DIR)#判断这个文件夹是否存在 不存在则创建一个文件夹

BASE_URL='https://ssr1.scrape.center'#站点的根路径
TOTAL_PAGE = 10#需爬取的总页面数
#日志输出级别与输出格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

def scrape_page(url): #爬取网页基础信息
    logging.info('scrape%s...',url)
    try:
     response = requests.get(url)
     if response.status_code == 200:
         return response.text
     logging.error('get invalid status code %s while scraping %s',response.status_code,url)
    except requests.RequestException:
     logging.error('error occurred while scraping %s',url)

def scrape_index(page):#爬取页面后 页数列表的爬取
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

def parse_index(html):#解析获取的html代码
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')#正则表达式获取详细页的ip
    items = re.findall(pattern,html)#匹配html代码中的符合正则表达式的内容
    if not items:#判断是否匹配成功，失败则返回空列表
        return []
    for item in items:#遍历
        detail_url = urljoin(BASE_URL,item)#拼接详细url
        logging.info('get detail url  %s',detail_url)#展示拼接后的url
        yield detail_url#返回详细页的url

def main(page):#整合函数
        index_html = scrape_index(page)#获取每个页面的html代码
        detail_urls = parse_index(index_html)#解析后得到详细页面的url
        for detail_url in detail_urls:
         detail_html = scrape_detail(detail_url)
         data = parse_detail(detail_html)
         logging.info('get detail data %s',data)#展示
         logging.info('saving data to json file')
         save_data(data)
         logging.info('data saved successfully')


def scrape_detail(url):#获取详细页面代码
    return (scrape_page(url))

def parse_detail(html):#获取详细页面的信息，用正则表达式
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">',re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>',re.S)
    published_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映</span>')
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>',re.S)
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>',re.S)

#strip()去掉首尾的空格
    cover = re.search(cover_pattern,html).group(1).strip() if re.search(cover_pattern,html) else None
    name = re.search(name_pattern,html).group(1).strip() if re.search(name_pattern,html) else None
    categories = re.findall(categories_pattern,html) if re.findall(categories_pattern,html) else []
    published = re.search(published_pattern, html).group(1) if re.search(published_pattern, html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    score = re.search(score_pattern, html).group(1).strip() if re.search(score_pattern, html) else None

    return {
        'cover':cover,
        'name':name,
        'categories':categories,
        'published':published,
        'drama':drama,
        'score':score
    }

def save_data(data):
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    json.dump(data,open(data_path,'w',encoding='utf-8'),ensure_ascii=False,indent=2)


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1,TOTAL_PAGE + 1)
    pool.map(main,pages)
    pool.close()
    pool.join()