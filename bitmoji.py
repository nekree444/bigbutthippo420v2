from curl_cffi import requests
from selectolax import parser
from pprint import pprint

def bitmoji_webp(snap='thomasm444'):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

    r = requests.get(f'https://www.snapchat.com/add/{snap}', headers=headers)
    return parser.HTMLParser(r.text).css_first('picture.Bitmoji3DImage_webPImage__sMFoZ').css_first('source').attributes.get('srcset')

if __name__ == '__main__':
    print('\n--- 😅😅😅😅😅😅😅😅😅😅 ---\n')
    moji = input('\n Enter snapchat username ->>')
    print(f'\n {bitmoji_webp(moji)}')

