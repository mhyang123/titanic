class Contacts:
    def __init__(self,name, phone, mail, addr):

        self.name = name
        self.phone = phone
        self.mail = mail
        self.addr = naddr

    def print_info(self):
        print("이름:",self,name)
        print("전화번호:", self,phone )
        print("이메일:", self, email)
        print("주소:", self, addr)

    def set_contact(self):
        name= input("이름:")
        phone = input("전화번호:")
        email = input("이메일:")
        addr = input("주소:")
        contact=Contacts(name,phone,email,addr)
        return contact

    @staticmethod
    def get_contact(list):
        for i in list:
            i.print_info()
    @staticmethod
    def del_contact():
        for i,t in enumerate(list):
            if t.name == name:
                del list[i]
    @staticmethod
    def print_menu():
        print("1,연락처 입력")
        print("2,연락처 출력")
        print("3,연락처 삭제")
        print("4, 종료")
        menu = input("메뉴선택:")
        return int(menu)



    @staticmethod
    def run():
        list = []
        while 1:
            menu = print_menu()
           if menu ==1:
                 t=Contacts_ set_contact()
                 list.append(t)
           elif menu==2:
               contacts.get_contacts(list)
           elif menu == 3:
               name=input ("삭제할 이름")
               Contacts.del_contact(list,name)
           elif menu == 4:
               break