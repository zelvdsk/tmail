import requests
import string, random
from .utils import bs4, gurl

class MsgScrapper:
    def __init__(self, parse, mail):
        self.mail = mail
        self.host = 'https://generator.email/'
        self.parse = parse

    def messages(self):
        return self.singgle()

    def singgle(self): 
        try:
            wrap_msg = self.parse.find('div', {'class': True, 'style': 'display: inline-block;'})
            
            sender_mail = wrap_msg.find(string='From: ').find_next('span').text.split(' ')[0]
            subject = wrap_msg.find(string='Subject: ').find_next('div').find('h1').text
            received = wrap_msg.find(string='Received: ').find_next('span').text.strip().split('\n')[0]
            
            try: 
                # string messages
                messages = self.parse.find('div', {'dir': 'auto'}).text
            except AttributeError:
                # html messages
                messages = str(self.parse.find('td', {'id': 'email_content'}))
            
            return [{'from': sender_mail, 'subject': subject, 'received': received, 'messages': messages}]
        except AttributeError:
            return self.multi()

    def multi(self):
        wrap_url = self.parse.find('div', {'id': 'email-table'})

        try:
            message_data = list()
            patch = gurl(wrap_url, self.mail.split('@')[0])
            for msg_patch in patch:
                try:
                    message_data.append(self.gmmsg(msg_patch))
                except requests.exceptions.ConnectionError:
                    message_data.append(self.infinity_loop(msg_patch))

            return message_data
        except AttributeError:
            return []

    def gmmsg(self, msg_patch):
        msg_source = bs4(requests.get(self.host + msg_patch).text)
        #try:
        sender_mail = msg_source.find(string='From: ').find_next('span').text.split(' ')[0]
        subject = msg_source.find(string='Subject: ').find_next('div').find('h1').text
        received = msg_source.find(string='Received: ').find_next('span').text.strip().split('\n')[0]

        try:
            # string messages
            messages = msg_source.find('div', {'dir': 'auto'}).text
        except AttributeError:
            # html messages
            messages = str(msg_source.find('td', {'id': 'email_content'}))

        x = {'from': sender_mail, 'subject': subject, 'received': received, 'messages': messages}
        return x

    def infinity_loop(self, msg_patch):
        while True:
            try:
                return self.gmmsg(msg_patch)
            except requests.exceptions.ConnectionError:
                continue
        

'''
ses = requests.session()
url = 'https://generator.email/cmkane82@816qs.com'
while True:
    try:
        parse = bs4(ses.get(url).text)
        print('1')
        print(MsgScrapper(parse, 'cmkane82@816qs.com').messages())
        break
    except requests.exceptions.ConnectionError:
        continue

'''
