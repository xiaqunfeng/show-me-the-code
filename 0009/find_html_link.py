import re
import requests
from bs4 import BeautifulSoup

def find_html_body(url):
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')
    urls = soup.findAll('a')

    for u in urls:
        print(u['href'])

if __name__ == '__main__':
    url = 'http://xiaqunfeng.cc'
    find_html_body(url)
