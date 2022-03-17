<h1 align="center">Google-translator</h1>

#### pip install GoogleTranslator



**ASYNC**


```python
import asyncio
from google.translator import GoogleTranslator

translator = GoogleTranslator()

async def my_translator(text, src_lang: str):
    await translator.translate_async(text, src_lang)

print(asyncio.run(my_translator("test", "ru")))
```


**SYNC**

```python
from google.translator import GoogleTranslator

translator = GoogleTranslator()

def my_translator(text, src_lang: str):
    translator.translate_async(text, src_lang)

print(my_translator("test", "ru"))
```
