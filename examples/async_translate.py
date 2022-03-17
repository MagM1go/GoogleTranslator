import asyncio
from google.translator import GoogleTranslator

translator = GoogleTranslator()

async def my_translator(text, src_lang: str):
    await translator.translate_async(text, src_lang)

print(asyncio.run(my_translator("test", "ru")))
