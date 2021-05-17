"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
     
     [참고] 파싱방법
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

def download_file(url):
    p = parse.urlparse(url)
    print('1>', p)
    savepath = './' + p.netloc + p.path
    print('2>', savepath)
    # 마지막에 '/'로 끝나면 뒤에 index.html 붙이기
    if re.search('/$', savepath):
        savepath += 'index.html'
        print('3>', savepath)
    # else:
    #     savepath += '.html'

    # 해당 파일이 존재하는지
    if os.path.exists(savepath):
        return savepath

    # 다운로드 할 폴더 생성
    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):
        os.makedirs(savedir) # dirs 는 하위 경로까지 생성

    # 해당 url을 다운받기
    try:
        print('다운로드 : ', url)
        request.urlretrieve(url, savepath)
        time.sleep(2)
        return savepath
    except:
        print('다운로드 실패 : ', url)
        return None
if __name__ == '__main__':
    # url 지정
    # url = 'https://docs.python.org/3.6/library/'
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_opt&query=%EB%A6%AC%EB%B2%84%ED%92%80+%EB%B9%85%ED%81%B4%EB%9F%BD+%EC%95%84%EB%8B%88%EC%95%BC&nso=so%3Add%2Cp%3A1h&nso_open=1'
    result = download_file(url)
    print(result)