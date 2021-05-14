"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""
from pathlib import Path
import os

# print(Path.cwd())
#
# # 체인지 디렉토리
# os.chdir('..')
# print(Path.cwd())

# shutil 라이브러리 이용
import shutil
# shutil.rmtree('imsi')

# shutil.copy('Ex00.txt', 'babo.txt')


shutil.copytree('../f_path_class', 'temp')
