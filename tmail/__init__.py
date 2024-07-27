import requests
from .messages import MsgScrapper
from .utils import bs4

class TMail:
    session = requests.session()
    host = 'https://generator.email/'

    def __init__(self):
        source = bs4(self.session.get(self.host).text)
        self.mail = source.find('span', {'id': 'email_ch_text'}).get_text()

    def messages(self, mail: str=None):
        parse = bs4(self.session.get(self.host + (mail if mail is not None else self.mail)).text)
        msg = MsgScrapper(parse, mail if mail is not None else self.mail).messages()
        return msg
