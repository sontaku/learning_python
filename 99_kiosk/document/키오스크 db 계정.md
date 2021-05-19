# 키오스크 db 계정

- sql 실행

  ```mariadb
  sqlplus SYSTEM/manager
  ```


pip

- SYSTEM 계정 연결

  ```mariadb
  conn SYSTEM/manager
  ```

  

- 중복 계정 삭제

  ```mariadb
  DROP USER ksk CASCADE;
  ```

  

- oracle 계정 생성

  ```mariadb
  CREATE USER ksk IDENTIFIED BY ksk
  DEFAULT tablespace USERS
  TEMPORARY tablespace TEMP;
  ```



- 접속 권한 부여

  ```mariadb
  conn SYSTEM/manager
  
  GRANT RESOURCE, CONNECT TO ksk;
  ```

  

- 계정 연결

  ```mariadb
  conn ksk/ksk
  
  --계정 확인
  show user
  ```



- 계정 활성화

  ```mariadb
  ALTER USER ksk IDENTIFIED BY ksk;
  ```

  

- 테스트 코드 진행

  ```mariadb
  DROP TABLE testtable;
  
  CREATE TABLE testtable(
      a VARCHAR2(10), 
  	b NUMBER);
  	
  DESC testtable;
  
  DROP TABLE testtable;
  ```


- 해당 계정 테이블 조회

  ```mariadb
  SELECT * FROM tabs;
  ```



<hr>



- ## DDL & DML

```mariadb
DROP TABLE od_list;
DROP TABLE product;
DROP TABLE t_od_list;
DROP SEQUENCE seq_oid;

-- 제품목록 테이블
CREATE TABLE product(
    pid NUMBER, -- idx 제품번호
    name VARCHAR2(60), -- 제품명
	price NUMBER -- 가격
); 

-- 주문내역 테이블
CREATE TABLE t_od_list(
    oid NUMBER, -- 주문번호
    t_price NUMBER, -- 합계금액
    order_date date -- 주문일자
);

CREATE SEQUENCE seq_oid;

INSERT INTO product VALUES(1, '인터로킹 G 슬라이더 샌들 black', 490000);
INSERT INTO product VALUES(2, '인터로킹 G 슬라이더 샌들 white', 490000);
INSERT INTO product VALUES(3, '웹 패널 슬라이더 샌들', 440000);
INSERT INTO product VALUES(4, 'GG 수프림 프린트 슬라이더 샌들', 600000);
INSERT INTO product VALUES(5, '월드와이드 슬리퍼', 450000);
INSERT INTO product VALUES(6, '로고 가죽 슬리퍼', 790000);

commit;




```

