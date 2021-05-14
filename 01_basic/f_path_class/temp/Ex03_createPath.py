from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd()) # 리눅스의 pwd
print(Path.home()) # 리눅스의 홈디렉토리

p = Path('Ex03_createPath.py')
print(p.stat()) # 리눅스 stat

# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
print('----------------------------')
from datetime import datetime
tm = p.stat().st_atime # 1620952926.139031
print(tm)
print(datetime.fromtimestamp(tm))

# ------------------------------------------------
# # 3. 디렉토리 생성
# p1 = Path('imsi')
# p1.mkdir(exist_ok=True)
#
# p2 = Path('imsi')
# # 이미 존재해도 생성
# p2.mkdir(exist_ok=True)
#
#
# p3 = Path('imsi2/temp2/test')
# p3.mkdir(parents=True)

# ------------------------------------------------
# 4. 파일 생성
print('---------------------------------')
# with open('imsi/1.txt', 'wt', encoding='UTF-8') as f:
#     f.write('오늘도화이팅')

# p = Path('imsi/2.txt')
# with open(p, 'wt', encoding='UTF-8') as f:
#     f.write('오늘도화이팅')

p = Path('imsi/3.txt')
p.write_text('주말행복', encoding='utf-8')

# ------------------------------------------------
#  5. 경로 제거
print('----------------------------------')
f = Path('imsi/3.txt')
f.unlink()

# 자식으로 파일or디렉토리가 있으면 삭제 불가
p = Path('imsi')
p.rmdir()

# 다른 라이브러리 이용
