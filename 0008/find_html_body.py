import re
import requests
from bs4 import BeautifulSoup

def find_html_body(url):
    data = requests.get(url)
    r = re.findall(r'<body>[\s\S]*<body', data.text)
    #print(r[0])

    soup = BeautifulSoup(data.text, 'html.parser')
    print(soup.body.text)

if __name__ == '__main__':
    #url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text'
    url = 'http://xiaqunfeng.cc'
    find_html_body(url)
