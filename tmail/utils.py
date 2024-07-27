from bs4 import BeautifulSoup

bs4 = lambda html: BeautifulSoup(html, 'html.parser')
gurl = lambda soup, context: [x['href'] for x in soup.find_all('a', href=lambda href: context in href)]
