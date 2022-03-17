import re
import html

import aiohttp
import requests


class GoogleTranslator:
    
    def __init__(self):
        self.regex = r'(?s)class="(?:t0|result-container)">(.*?)<'
        self.user_agent = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70 (Edition Yx GX)"
        }

    def normal_data(self, text):
        return html.unescape(text)

    async def translate_async(self, text: str, to_lang: str = 'auto', from_lang: str = 'auto'):
        async with aiohttp.ClientSession().get(f'https://translate.google.com/m?tl={to_lang}&sl={from_lang}&q={text}', headers=self.user_agent) as response:
            data = await response.read()

        data = data.decode('utf-8')

        return list(filter(lambda data: data, re.findall(self.regex, data)))[0]

    def translate_sync(self, text: str, to_lang: str = 'auto', from_lang: str = 'auto'):
        data = requests.get(f'https://translate.google.com/m?tl={to_lang}&sl={from_lang}&q={text}', headers=self.user_agent)
        data = data.decode('utf-8')

        return list(filter(lambda data: data, re.findall(self.regex, data)))[0]
