import os
import sys
import urllib.request
import json

client_id = "6HlwuXpGakcyl4ykbpVt"
client_secret = "jtKQPgyTSJ"


def call(keyword):
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText  # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        return (response_body.decode('utf-8'))
    else:
        return ("Error Code:" + rescode)
    keyword = input()

    with open('./moviedata.json', 'w+') as moviedata:
        moviedata.write(json.dumps(call(keyword)))