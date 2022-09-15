import asyncio
from pyppeteer import launch
import logging
from pyppeteer.errors import TimeoutError


INDEX_URL = 'https://spa2.scrape.center/page/{page}'
WINDOW_WIDTH,WINDOW_HEIGHT=1366,768
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-:%(message)s')
browser,tab=None,None

async def init():
  global tab
  global browser
  browser = await launch(headless=False,devtools = True,args=['--disable-infobars',f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'])
  tab = await browser.newPage()
  await tab.setViewport({'width':WINDOW_WIDTH,'height':WINDOW_HEIGHT})

async def scrape_page(url,selector):
    logging.info('%s',url)
    try:
     await tab.goto(url)
     await tab.waitForSelector(selector,options=({'timeout':10*1000}))
    except TimeoutError:
        logging.info('%s',url,exc_info=True)
async def scrape_index(page):
    url = INDEX_URL.format(page = page)
    await scrape_page(url,'.item.name')
async def parse_index():
    return await tab.querySelectorAllEval('.item.name','nodes => nodes.map(node => node.herf)')

async def main():
    await init()
    try:
        for page in range(1,11):
            await scrape_index(page)
            await parse_index()
    finally:
        await browser.close()

if __name__ =='__main__':
    asyncio.get_event_loop().run_until_complete(main())