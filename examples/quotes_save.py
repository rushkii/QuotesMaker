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
        filename can be empty, and generate the filename with your quotes
        
        Bahasa:
        filename bisa dikosongkan dan meng-generate filenamenya dengan quotemu
        '''
        print(await quotes.save()) # return filename
    asyncio.run(main())

else:
    quotes = QuotesMaker()
    loop = asyncio.get_event_loop()

    async def main():
        '''
        English:
        filename can be empty, and generate the filename with your quotes

        Bahasa:
        filename bisa dikosongkan dan meng-generate filenamenya dengan quotemu
        '''
        print(await quotes.save()) # return filename
    loop.run_until_complete(main())