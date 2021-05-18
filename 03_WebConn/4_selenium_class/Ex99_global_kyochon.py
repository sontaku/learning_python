# 교촌 해외 탐방기


from selenium import webdriver
import time
from bs4 import BeautifulSoup
import cx_Oracle as oci
# -------------------------------1. 웹 페이지 접근
# 웹드라이버 객체 생성
url = 'http://www.kyochon.com/shop/overseas_view.asp?'
url2 = 'http://www.kyochon.com'
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.get(url)

html = driver.page_source
bs = BeautifulSoup(html, 'html.parser')

cls = bs.select(".overseasTab a")

attr = []
for i in cls:
    attr.append(str(i["href"]).split("?")[1])

for j in range(len(cls)):
    driver.get(url + attr[j])
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    dd = bs.select(".slide dd")
    img = bs.select(".slide img")

    cntr = cls[j].select_one("img")
    print(cntr["alt"])
    # 1. 연결 얻어오기
    conn = oci.connect('SCOTT/TIGER@127.0.0.1:1521/xe')
    print('연결 성공', conn.version)
    # 2) 커서(Cursor) 얻어오기
    cursor = conn.cursor()
    # 3) SQL 문장
    data = [j + 1, cntr["alt"]]
    sql = 'INSERT INTO country VALUES(:0, :1)'
    # print(sql, data)
    # 4) SQL 실행
    cursor.execute(sql, data)
    conn.commit()
    cursor.close()
    conn.close()
    # store_name = ''
    # store_tel = ''
    # store_addr = ''
    # store_imgUrl =''
    for k, i in zip(dd, img):
        store_name = str(k.text.replace('\t', '').split('\n')[1])
        store_tel = str(k.text.replace('\t', '').split('\n')[2])
        store_addr = str(k.text.replace('\t', '').split('\n')[3])
        print('매장명 : ' + store_name + ' 번호 : ' + store_tel + ' 주소 : ' + store_addr)
        store_imgUrl = url2 + i["src"]
        print(url2 + i["src"])

        # 1. 연결 얻어오기
        conn = oci.connect('SCOTT/TIGER@127.0.0.1:1521/xe')
        # 2) 커서(Cursor) 얻어오기
        cursor = conn.cursor()
        # 3) SQL 문장
        sql = '''INSERT INTO store VALUES(
            seq_sid.nextval, 
            :0, :1, :2, :3, :4, '', ''
        )'''
        data = [j + 1, store_name, store_tel, store_addr, str(store_imgUrl)]
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()
# j, store_name, store_tel, store_addr, store_imgUrl