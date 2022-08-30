import requests
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-:%(message)s')

index_url = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'

def scrape_api(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.json()
        logging.info('get status code %s while scrape %s',response.status_cod,url)
    except:
        logging.error('error occurred while scrape %s',url,exc_info=True)

Limit = 10
def scrape_index(page):
    url = index_url.format(limit = Limit,offset =Limit*(page-1))
    return scrape_api(url)


detail_url = 'https://spa1.scrape.center/api/movie/{id}'

def scrape_detail(id):
    url = detail_url.format(id = id)
    return scrape_api(url)

total_page = 10

def main():
    for page in range(1,total_page):
        index_data=scrape_index(page)
        for item in index_data.get('results'):
            id=item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s',detail_data)
            save_data(detail_data)
            logging.info('data saved successfully')


MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'

import pymongo

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']

def save_data(data):
    collection.update_one({'name':data.get('name')},{'$set':data},upsert=True)




if __name__ == '__main__':
    main()











