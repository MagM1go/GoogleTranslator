from google.translator import GoogleTranslator

translator = GoogleTranslator()

def my_translator(text, src_lang: str):
    translator.translate_sync(text, src_lang)

print(my_translator("test", "ru"))
