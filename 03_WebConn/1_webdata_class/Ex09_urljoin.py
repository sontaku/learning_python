"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""

# from urllib import parse
# parse.urljoin()

from urllib.parse import urljoin
baseurl = 'http://www.example.com/html/aaaaa/aaaa/ffffff/a.html'

print(urljoin(baseurl, 'b.html'))
print(urljoin(baseurl, 'sub/c.html'))
print(urljoin(baseurl, '/sub/d.html'))
print(urljoin(baseurl, '../sub/e.html'))
print(urljoin(baseurl, '../temp/f.html'))

print('---------------------------------')

print(urljoin(baseurl, 'www.other.com/mypage'))
print(urljoin(baseurl, '//www.other.com/mypage'))
print(urljoin(baseurl, 'http://www.other.com/mypage'))