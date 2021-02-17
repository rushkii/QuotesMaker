from .api import Unsplash

from pybase64 import b64decode, b64encode
from PIL import Image, ImageFont, ImageFilter, ImageDraw, ImageEnhance
import asyncio, os, sys, random, io, aiohttp, json, textwrap, logging

slash = "\\" if sys.platform == "win32" else "/"
results_path = f"{os.getcwd()}{slash}results"
assets_path = f"{os.getcwd()}{slash}assets"

class QuotesMaker:
    def __init__(self, quote:str="Input your quotes", watermark:str="Unknown", width:int=1024, height:int=1024, brightness:float=0.5):
        self.__quote = quote
        self.__watermark = watermark
        self.__width = width
        self.__height = height
        self.__brightness = brightness
        
    def __repr__(self):
        L = ['%s=%r' % (key.replace(f"_{self.__class__.__name__}__", ""), value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    async def __create(self):
        async with aiohttp.ClientSession() as ses:
            imsplash = Unsplash()
            images = random.choice([a['links']['download'] for a in await imsplash.images("nature")])
            async with ses.get(images)as r:
                b64e = b64encode(await r.read())
            b64d = b64decode(b64e)
            im = Image.open(io.BytesIO(b64d))
            resized = im.resize((self.__width, self.__height))
            darkened = ImageEnhance.Brightness(resized).enhance(self.__brightness)
            W,H = darkened.size
            draw = ImageDraw.Draw(darkened)
            font_quote = ImageFont.truetype(os.path.join(f'{assets_path}{slash}fonts{slash}BiminiCondensed.TTF'), size=50)
            font_watermark = ImageFont.truetype(os.path.join(f'{assets_path}{slash}fonts{slash}Goldfinger Kingdom.ttf'), size=50)
            wrapper = textwrap.TextWrapper(width=50) 
            word_list = wrapper.wrap(text=self.__quote)
            caption_new = '\n'.join(line.center(80) for line in word_list)
            w, h = draw.textsize(caption_new, font_quote)
            w2, h2 = draw.textsize(self.__watermark, font_watermark)
            h += int(h*0.21);h2 += int(h*0.21)
            draw.text(((W-w)/2,(H-h)/2), caption_new, fill='rgb(255, 255, 255)', font=font_quote)
            draw.text(((W-w2)/2,(H-h2)/2*2), self.__watermark, fill='rgb(255, 255, 255)', font=font_watermark)
            return darkened
    
    async def fonts(self):
        return os.listdir(f"{os.getcwd()}{slash}fonts")
    
    async def show(self):
        im = await self.__create()
        im.show()
        return True

    async def save(self, filename=""):
        im = await self.__create()
        if filename == "":
            res = results_path+slash+self.__quote.lower().replace(" ","-") if self.__quote.lower().endswith(".jpg") or self.__quote.lower().endswith(".png") else results_path+slash+self.__quote.lower().replace(" ","-")+".jpg"
        else:
            res = results_path+slash+filename if filename.lower().endswith(".jpg") or filename.lower().endswith(".png") else results_path+slash+filename+".jpg"
        im.save(res)
        return res

    @property
    def quote(self):
        return self.__quote

    @property
    def watermark(self):
        return self.__watermark
        
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def brightness(self):
        return self.__brightness

    def set_quote(self, text: str="Input your quote."):
        self.__quote = text
        return self.__quote

    def set_watermark(self, text: str="Unknown."):
        if len(text) > 20:
            self.__watermark = text[0:20]
            logging.warning(f"Watermark length cannot be more than > 20, program has slicing your watermak to `{self.__watermark}`")
        else:
            self.__watermark = text
        return self.__watermark

    def set_width(self, width: int):
        self.__width = width
        return self.__width

    def set_height(self, height: int):
        self.__height = height
        return self.__height

    def set_brightness(self, brightness: float):
        self.__brightness = brightness
        return self.__brightness

if __name__ == '__main__':
    import json
    img = QuotesMaker()
    img.set_quote("Don't stop until you reach your goals.")
    async def main():print(await img.show())
    asyncio.run(main())