from bs4 import BeautifulSoup as bsoup
import asyncio, aiohttp, lxml, time, json

class Unsplash:
    def __init__(self):
        self.base_url = "https://unsplash.com"
        self.headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
		}

    async def topics(self):
        async with aiohttp.ClientSession() as ses:
            async with ses.get(self.base_url) as res:
                s = bsoup(await res.text(), 'lxml')
                return [
                    {
                        "name": a.find("span", class_='_1WMnM xLon9').text,
                        "url": f"{self.base_url}{a.find('a', class_='qvEaq')['href']}"
                    }for a in s.find_all('li', class_='_1hkdt')
                ]

    async def images(self, topic, page=1, per=20):
        async with aiohttp.ClientSession() as ses:
            async with ses.get(f"{self.base_url}/napi/topics/{topic}/photos?page={page}&per_page={per}") as res:
                return json.loads(await res.text())

if __name__ == '__main__':
    import json
    async def main():img = await Unsplash().images("nature", page=1, per=20);print(json.dumps([a['links']['download'] for a in img],indent=4))
    asyncio.run(main())