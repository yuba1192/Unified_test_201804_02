# coding: UTF-8
import requests
import re
import html.parser as hp
import urllib

# HTMLParserを継承したクラスを定義
def getTitle(url):
    data = urllib.request.urlopen(url)

    # HTMLの取得
    html = data.read()
    html = html.decode('utf-8')
    title = re.findall('<title.*>(|\n)(.*?)</title>', html)

    return title[0][1]

def main():
    check_url = []

    # アクセスするURL
    url = "https://no1s.biz/"
    # html取得
    resp = requests.get(url)

    # aタグを取得
    address = re.findall('<a href=\"(https://no1s.biz/.*?)\".*>(.*)</a>', resp.text)

    for i in range(len(address)):
        if address[i][0] in check_url:
            continue

        # ダブりを削除するため
        check_url.append(address[i][0])

        # titleを取得する
        urlTitle = getTitle(address[i][0])

        # 表示させる
        print(urllib.parse.unquote(address[i][0])    + "\t" + urlTitle)

if __name__ == "__main__":
    main()