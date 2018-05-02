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

# クローリング処理
def crawling(url, check_url):

    # html取得
    resp = requests.get(url)

    # aタグを取得
    address = re.findall('<a.*href=\"(https://no1s.biz/.*?)\".*>(.*)</a>', resp.text)

    for i in range(len(address)):
        # すでに登場済みの場合はパス
        if address[i][0] in check_url:
            continue

        # ダブりを削除するため
        check_url.append(address[i][0])

        # titleを取得する
        urlTitle = getTitle(address[i][0])

        # 表示させる
        print(urllib.parse.unquote(address[i][0])    + "\t" + urlTitle)

        # 再度取得したURL内をクローリング
        crawling(urllib.parse.unquote(address[i][0]), check_url)


def main():
    check_url = []
    # アクセスするURL
    url = "https://no1s.biz/"

    # クローリング処理
    crawling(url, check_url)

if __name__ == "__main__":
    main()