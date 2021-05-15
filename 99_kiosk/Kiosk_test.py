import tkinter
from tkinter import *
# from tkinter import tkinter
from PIL import ImageTk, Image

def button_pressed(value):
  number_entry.insert("end", value)
  print(value, "pressed")

def math_button_pressed(value):
  print(value, "pressed")

def equal_button_pressed():
  print("equal pressed")

root = Tk()
root.title("신으슈")
root.geometry("1200x800")  # 화면폭에 맞춰서 늘려줌.

entry_value = StringVar(root, value='')

# number_entry = tkinter.Entry(root, textvariable=entry_value, width=20)
# number_entry.grid(row=0, columnspan=4)

img1 = ImageTk.PhotoImage(Image.open("image/s1.png"))
button1 = tkinter.Button(root, text="메뉴1", width='270', height='320', image=img1, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button1.grid(row=0, column=0)

img2 = ImageTk.PhotoImage(Image.open("image/s2.png"))
button2 = tkinter.Button(root, text="메뉴2",  width='270', height='320', image=img2, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button2.grid(row=0, column=1)

img3 = ImageTk.PhotoImage(Image.open("image/s3.png"))
button3 = tkinter.Button(root, text="메뉴3",  width='270', height='320', image=img3, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button3.grid(row=0, column=2)

img4 = ImageTk.PhotoImage(Image.open("image/s4.png"))
button1 = tkinter.Button(root, text="메뉴4", width='270', height='320', image=img4, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button1.grid(row=1, column=0)

img5 = ImageTk.PhotoImage(Image.open("image/s5.png"))
button5 = tkinter.Button(root, text="메뉴5",  width='270', height='320', image=img5, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button5.grid(row=1, column=1)

img6 = ImageTk.PhotoImage(Image.open("image/s6.png"))
button6 = tkinter.Button(root, text="메뉴6",  width='270', height='320', image=img6, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button6.grid(row=1, column=2)

# viewList = tkinter.Frame(root, background='yellow')
viewList = tkinter.Frame
# viewList.pack(ipadx=20, ipady=20, side=RIGHT)
viewList.grid(row=0, column=3, rowspan=2)

#
# imgg = Image.open("image/mac.png")
# img = ImageTk.PhotoImage(imgg)  # PIL solution
#
# button10 = tkinter.Button(root, image=img, width='450', height='400', command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
# button10.grid(row=4, column=0, rowspan=2, sticky=W + E + N + S)
# button10tag = tkinter.Label(text="캬")
# button10tag.grid(row=6, column=0)

root.mainloop()
