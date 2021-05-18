# 교촌 해외 탐방기



```mariadb
DROP TABLE country;
DROP TABLE store;

DROP SEQUENCE seq_cid;
DROP SEQUENCE seq_sid;

-- 국가 테이블 생성
CREATE TABLE country(
	cid NUMBER, -- idx
    name VARCHAR2(30) -- 국가명
);

-- 매장 테이블 생성
CREATE TABLE store(
	sid NUMBER, -- idx
    cid NUMBER, -- 국가명
    name VARCHAR2(100), -- 매장명
    tel VARCHAR2(50), -- 전화번호
    addr VARCHAR2(500), -- 주소
    img_url VARCHAR2(500), -- 이미지 주소
    latitude VARCHAR2(30), -- 위도
    longitude VARCHAR2(30) -- 경도
);

CREATE SEQUENCE seq_cid;
CREATE SEQUENCE seq_sid;

commit;



```

