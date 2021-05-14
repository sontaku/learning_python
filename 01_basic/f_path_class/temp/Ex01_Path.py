"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path

# (1) 해당 경로와 하위 목록들 확인
# p = Path('C:\windows')

# 점 1개는 현재경로
# 점 2개는 상위경로임을 확인 가능하다
p = Path('.')
print(p)
print(p.resolve())  # 현재 패키지 경로를 가리킴 즉, 실제 절대경로

test = []

# 현재경로의 하위경로를 iterator로 잡아줌
# for d in p.iterdir():
#     # 디렉토리만 잡아줌
#     if d.is_dir():
#         test.append(d)
# print(test)

test = [d for d in p.iterdir() if d.is_dir()]
print(test)

print('---------------------------------')

p = Path('..') # f_path_class
# glob : 파일 같은 애를 한꺼번에 처리
i = list(p.glob('**/a_datatype_class/*.py'))
print(i)