'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request as req

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=python&vPplace=top")
# html = urlopen("https://search.kyobobook.co.kr/web/search?vPstrKeyWord=python")

bs = BeautifulSoup(html, 'html.parser')

# -------------------------------------
# 책 제목 추출, 총 권수 출력
titles = bs.select('div.title > a > strong')
# prices = bs.select('div.title > a > sell_price')
print(titles)
for i in titles:
    # print(i.text)
    print(i.string.strip())
print('총 권수 : ', len(titles))

# ----------------------------
# 이미지 다운받아 파일 저장
print('----------------------------------')
imgUrl = bs.select('.cover > a > img')
# print(imgUrl)

for i in range(len(imgUrl)):
    # print(imgUrl[i].attrs['src'])
    imgPath = imgUrl[i].attrs['src']
    imgName = imgUrl[i].attrs['alt'].replace(':', '-')
    print(imgPath + " : " + imgName)
    req.urlretrieve(imgPath, 'images/' + imgName + '.jpg')