import urllib.request as ul
import json

url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=8fdd668963558afea98cf9efe23a1fb5"
request = ul.Request(url)

response = ul.urlopen(request)
rescode = response.getcode()

if(rescode == 200):
	responseData = response.read()

result = json.loads(responseData)

print(result)