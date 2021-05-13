
class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_number)
        print("이메일:", self.email)
        print("주소;", self.addr)

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    # 여기에 코드 작성
    name = input('이름을 입력해주세요 : ')
    phone_number = input('연락처를 입력해주세요 : ')
    email = input('이메일을 입력해주세요 : ')
    addr = input('주소를 입력해주세요 : ')
    return Contact(name, phone_number, email, addr)
    # pass

def print_contact(contact_list):
    print('=== 연락처 목록 ===')
    for i in range(len(contact_list)):
        c = contact_list[i]
        print('{}. 이름 : {}, 연락처 : {}, 이메일 : {}, 주소 : {}'.format(i + 1, c.name, c.phone_number, c.email, c.addr))
    print('==================')
    pass

def delete_contact(contact_list, name):
    # print('=== 연락처 목록 ===')
    # for i in range(len(contact_list)):
    #     c = contact_list[i]
    #     print('{}. 이름 : {}, 연락처 : {}, 이메일 : {}, 주소 : {}'.format(i + 1, c.name, c.phone_number, c.email, c.addr))
    # print('==================')
    # d = input(print('삭제할 연락처의 번호를 입력해주세요 : '))
    # del contact_list[d - 1]
    # print('삭제가 완료되었습니다.')
    del contact_list[contact_list.index()]
    # contact_list.remove(contact_list.index())
    pass

def run():
    # Contact 인스턴스를 저장할 리스트 자료구조 생성
    contact_list = []
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            contact = set_contact()
            contact_list.append(contact)
        elif menu==2: # 출력을 선택하면
            print_contact(contact_list)
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(contact_list,name)


if __name__ == "__main__":
    run()