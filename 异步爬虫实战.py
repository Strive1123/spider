import asyncio
import aiohttp
import logging
import json
from motor.motor_asyncio import AsyncIOMotorClient

#配置log日志
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s:%(message)s')
#Ajax网页链接模板
INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
#网页信息 每页电影数目  总页数
PAGE_SIZE = 18
PAGE_NUMBER = 100
CONCURRENCY = 5

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None

async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scrape url %s',url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('error occurred while scraping %s',url,exc_info=True)
async def scrape_index(page):
    url = INDEX_URL.format(offset = (page-1)*PAGE_SIZE,)
    return await scrape_api(url)

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1,PAGE_NUMBER+1)]
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info('result %s',json.dumps(results,ensure_ascii=False,indent=2))
    ids=[]
    for index_data in results:
        if not index_data:continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.wait(scrape_detail_tasks)
    await session.close()

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_COLLECTION_NAME = 'books'

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]
async def save_data(data):
    logging.info('saved data %s',data)
    if data:
        return await collection.update_one({
         'id':data.get('id')},{'$set':data},upsert=True)

async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data(data)


if __name__== '__main__':
    asyncio.get_event_loop().run_until_complete(main())






