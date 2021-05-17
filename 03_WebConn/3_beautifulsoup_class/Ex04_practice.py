from bs4 import BeautifulSoup
from urllib import request as req

# 녹색 글자만 추출하여 출력
url = 'http://www.pythonscraping.com/pages/warandpeace.html'
res = req.urlopen(url)
bs = BeautifulSoup(res, 'html.parser')
green = bs.select('.green')
for gr in green:
    print(gr.text)

print('---------------------------')

# 아이템과 가격을 추출
# .gift 첫번째 자손
url = 'http://www.pythonscraping.com/pages/page3.html'
res = req.urlopen(url)
bs = BeautifulSoup(res, 'html.parser')
items = bs.select('.gift td:first-child')
prices = bs.select('.gift td:nth-child(3)')
for i in range(len(items)):
    print(items[i].text.strip() + " : " + prices[i].text.strip())

print('---------------------------')

# 1) 책 제목과 설명만 추출
# url = 'https://wikidocs.net/'
# res = req.urlopen(url)
# bs = BeautifulSoup(res, 'html.parser')
# titles = bs.select('.media-body a')
# for i in range(len(titles)):
#     print(titles[i].text)
# 2) 이미지 다운