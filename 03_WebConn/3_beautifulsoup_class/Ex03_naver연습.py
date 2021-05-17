"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 금융 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""


from bs4 import BeautifulSoup
from urllib import request as req


# 웹 문서 가져오기
url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)
bs = BeautifulSoup(res, 'html.parser')
# print(bs.contents)
usd = bs.select_one('.usd')
print(usd)

print('============')
val = usd.select_one('.value')
won = usd.select_one('.txt_krw')
print(val.text, won.text)


print('===============')

bsl = bs.select('#exchangeList')
print(bsl)
for i in bsl:
    # bsl.select_one('.blind')
    # bsl.select_one('.value')
    print(i)
