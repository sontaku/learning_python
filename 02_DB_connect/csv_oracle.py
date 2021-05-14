import csv

import cx_Oracle as oci


def createDBTable():
    # 1. 연결 얻어오기
    conn = oci.connect('SCOTT/TIGER@127.0.0.1:1521/xe')
    # 2) 커서(Cursor) 얻어오기
    cursor = conn.cursor()
    # 3) SQL 문장
    sql = 'DROP TABLE supply'
    # 4) SQL 실행
    cursor.execute(sql)

    # 3) SQL 문장
    sql2 = 'DROP SEQUENCE seq_supply_id'
    # 4) SQL 실행
    cursor.execute(sql2)
    # 3) SQL 문장
    sql3 = '''
    CREATE TABLE supply (
        id INTEGER PRIMARY KEY,
        Supplier_Name VARCHAR2(30),
        Invoice_Number VARCHAR2(30),
        Part_Number VARCHAR2(30),
        Cost NUMBER,
        Purchase_Date DATE
    )
    '''
    # 4) SQL 실행
    cursor.execute(sql3)

    # 3) SQL 문장
    sql4 = 'CREATE SEQUENCE seq_supply_id'
    # 4) SQL 실행
    cursor.execute(sql4)
    # 5) 커서 닫기
    cursor.close()
    # 6) 연결 닫기
    conn.close()

def saveDB(data):
    # 1. 연결 얻어오기
    conn = oci.connect('SCOTT/TIGER@127.0.0.1:1521/xe')
    # 2) 커서(Cursor) 얻어오기
    cursor = conn.cursor()
    # 3) SQL 문장
    sql = '''
    INSERT INTO supply VALUES(
        seq_supply_id.nextval, :0, :1, :2, :3, :4
    )
    '''
    # 4) SQL 실행
    cursor.execute(sql, data)
    # 5) 커서 닫기
    cursor.close()

    # [중요] 파이썬에서는 오토커밋되지 않으므로 커밋!
    conn.commit()

    # 6) 연결 닫기
    conn.close()

def viewDB(tablename):
    # 1. 연결 얻어오기
    conn = oci.connect('SCOTT/TIGER@127.0.0.1:1521/xe')
    # 2) 커서(Cursor) 얻어오기
    cursor = conn.cursor()
    # 3) SQL 문장
    sql = 'SELECT * FROM {}'.format(tablename)
    # 4) SQL 실행
    # cursor.execute(sql)
    datas = cursor.execute(sql)
    for row in datas:
        print(row)
    # 5) 커서 닫기
    cursor.close()
    # 6) 연결 닫기
    conn.close()
if __name__ == '__main__':
    # 1) 테이블 생성
    # createDBTable()

    # 2) 파일의 데이터 읽어서 저장
    # file_name = 'supply.csv'
    # f = open(file_name, 'r')
    # datas = csv.reader(f, delimiter=',')
    # # 읽으면서 아무일도 하지 않음
    # header = next(datas, None)
    # print(header)
    # print('-' * 50)
    #
    # for row in datas:
    #     print(row)
    #     saveDB(row)

    # 3) 테이블의 레코드 검색
    viewDB('supply') # 테이블명을 받아서 해당 테이블 검색
