import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
# 화면 창 사이즈 지정
root.geometry("1200x800")
root.title("Frame Test")

frame = tk.Frame(root, bd=5, bg='light blue', relief='groove')  # 메인프레임
frame.pack()

l_frame = tk.Frame(root, bg='red')  # 좌측 프레임
l_frame.pack(side=tk.LEFT, fill="y")

r_frame = tk.Frame(root, bg='blue')  # 우측 프레임
r_frame.pack(side=tk.RIGHT, fill="both", expand=True)

rt_frame = tk.Frame(r_frame, bg='green')  # 우측상단 프레임
rt_frame.pack(side=tk.TOP, fill="both", expand=True)

rb_frame = tk.Frame(r_frame, bg='yellow')  # 우측하단 프레임
rb_frame.pack(side=tk.BOTTOM)

# =========================================================================

label = tk.Label(frame, text='top label')  # top 쪽에 올라감
label.pack()

img1 = ImageTk.PhotoImage(Image.open("image/s1.png"))
button1 = tk.Button(l_frame, text="메뉴1", width='270', height='320', image=img1, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button1.grid(row=0, column=0)

img2 = ImageTk.PhotoImage(Image.open("image/s2.png"))
button2 = tk.Button(l_frame, text="메뉴2",  width='270', height='320', image=img2, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button2.grid(row=0, column=1)

img3 = ImageTk.PhotoImage(Image.open("image/s3.png"))
button3 = tk.Button(l_frame, text="메뉴3",  width='270', height='320', image=img3, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button3.grid(row=0, column=2)

img4 = ImageTk.PhotoImage(Image.open("image/s4.png"))
button1 = tk.Button(l_frame, text="메뉴4", width='270', height='320', image=img4, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button1.grid(row=1, column=0)

img5 = ImageTk.PhotoImage(Image.open("image/s5.png"))
button5 = tk.Button(l_frame, text="메뉴5",  width='270', height='320', image=img5, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button5.grid(row=1, column=1)

img6 = ImageTk.PhotoImage(Image.open("image/s6.png"))
button6 = tk.Button(l_frame, text="메뉴6",  width='270', height='320', image=img6, command=lambda: button_pressed('메뉴1 추가하시겠습니까?'))
button6.grid(row=1, column=2)

pay_button = tk.Button(rb_frame, text="결제하기", width='390', height='7')
pay_button.pack(padx=30)

root.mainloop()