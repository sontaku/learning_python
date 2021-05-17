# 내장모듈 urllib 이용
from urllib import request # s 안 붙음

url = 'http://www.google.com'

site = request.urlopen(url)
print(site)
page = site.read()
print(page)