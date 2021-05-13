
with open("i_have_a_dream.txt", "r") as f:
    try:
        contents = f.read()
    except FileNotFoundError as e:
        print(e, '파일이 존재하지 않습니다.')
    else:
        print(contents)
