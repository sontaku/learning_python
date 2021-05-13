# from tkinter import *
# from tkinter import ttk
#
#
# def button_pressed(value):
#     number_entry.insert("end", value)
#     print(value, "pressed")
#
#
# def math_button_pressed(value):
#     print(value, "pressed")
#
#
# def equal_button_pressed():
#     print("equal pressed")
#
#
# root = Tk()
# root.title("진영이의 잡동사니")
# root.geometry("500x600")  # 화면폭에 맞춰서 늘려줌.
#
# entry_value = StringVar(root, value='')
#
# number_entry = ttk.Entry(root, textvariable=entry_value, width=20)
# number_entry.grid(row=0, columnspan=3)
#
#
# button1 = ttk.Button(root, text="메뉴1", command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
# button1.grid(row=1, column=0, rowspan=2, sticky=W+E+N+S)
# button2 = ttk.Button(root, text="메뉴2", command=lambda: button_pressed('2 추가하시겠습니까?'))
# button2.grid(row=1, column=1)
# button3 = ttk.Button(root, text="메뉴3", command=lambda: button_pressed('3 추가하시겠습니까?'))
# button3.grid(row=1, column=2)
#
# # button4 = ttk.Button(root, text="메뉴4", command=lambda: button_pressed('4'))
# # button4.grid(row=2, column=0)
# button5 = ttk.Button(root, text="메뉴5", command=lambda: button_pressed('5'))
# button5.grid(row=2, column=1)
# button6 = ttk.Button(root, text="메뉴6", command=lambda: button_pressed('6'))
# button6.grid(row=2, column=2)
#
# button7 = ttk.Button(root, text="메뉴7", command=lambda: button_pressed('7'))
# button7.grid(row=3, column=0)
# button8 = ttk.Button(root, text="메뉴8", command=lambda: button_pressed('8'))
# button8.grid(row=3, column=1)
# button9 = ttk.Button(root, text="메뉴9", command=lambda: button_pressed('9'))
# button9.grid(row=3, column=2)
#
# root.mainloop()