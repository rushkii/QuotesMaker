from Quotes.maker import QuotesMaker
import sys, asyncio

if float(sys.version[:3]) > 3.7:
    '''
    English:
    asyncio.run() only works on Python version 3.7 or above.

    Bahasa:
    asyncio.run() hanya dapat bekerja pada Python versi 3.7 atau ke atasnya.
    '''
    quotes = QuotesMaker()
    
    async def main():
        '''
        English:
        Edit your quotes and the image, but I recommend you just edit the `quote` and the `watermak`.
        
        Bahasa:
        Edit quotesmu dan gambarnya, tapi aku sarankan kamu hanya edit `quote` dan `watermark`nya saja.
        '''
        quotes.set_quote("I am enough of an artist to draw freely upon my imagination. Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.")
        quotes.set_watermark("- Albert Einstein")
        quotes.set_width(1024)
        quotes.set_height(1024)
        quotes.set_brightness(0.5)
        print(quotes)
        await quotes.show()
    asyncio.run(main())

else:
    quotes = QuotesMaker()
    loop = asyncio.get_event_loop()

    async def main():
        '''
        English:
        Edit your quotes and the image, but I recommend you just edit the `quote` and the `watermak`.

        Bahasa:
        Edit quotesmu dan gambarnya, tapi aku sarankan kamu hanya edit `quote` dan `watermark`nya saja.
        '''
        quotes.set_quote("I am enough of an artist to draw freely upon my imagination. Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.")
        quotes.set_watermark("- Albert Einstein")
        quotes.set_width(1024)
        quotes.set_height(1024)
        quotes.set_brightness(0.5)
        print(quotes)
        await quotes.show()
    loop.run_until_complete(main())

