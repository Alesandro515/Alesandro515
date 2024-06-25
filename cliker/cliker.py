from tkinter import *

root = Tk()
root.title('Кликер')
root.geometry("650x400")
root.config(bg='pink')
m = str()
n = 0

def Click():
    global n
    n += 1
    if n == 1:
        label1["text"] = f"{n} Факт"
    elif 2 <= n <= 4:
        label1["text"] = f"{n} Факта"
    else:
        label1["text"] = f"{n} Фактов"

    if n == 10:
        label2["text"] = 'Дохляк'
    elif n == 100:
        label2["text"] = 'Слабак'
    elif n == 200:
        label2["text"] = 'Салага'
    elif n == 300:
        label2["text"] = 'Чайник'
    elif n == 400:
        label2["text"] = 'Крендель'
    elif n == 500:
        label2["text"] = 'Детина'
    elif n == 600:
        label2["text"] = 'Крепыш'
    elif n == 700:
        label2["text"] = 'Бугай'
    elif n == 800:
        label2["text"] = 'Амбал'
    elif n == 900:
        label2["text"] = 'Монстр'
    elif n == 1000:
        label2["text"] = 'Громила'
    elif n == 1100:
        label2["text"] = 'Кинг-конг'
    elif n == 2000:
        label2["text"] = 'МАРАТ'

def Develop():
    global n
    if enabled.get() == 1:
        n += 99
        label1["text"] = f"{n} Фактов"

enabled = IntVar()
b1 = Button(root, text="Клик", background="white", padx=150, pady=20, font="16", command=Click)
b1.place(x=150, y=150)

label1 = Label(root, text=n, font=("Helvetica", 50), background="#d1ddde", width=20, justify=CENTER)
label1.pack()

label2 = Label(root, text=m, font=("Helvetica", 60), background="pink", width=20, justify=CENTER)
label2.place(x=-150, y=250)

BL = Checkbutton(root, text='Режим разработчика', variable=enabled, background="pink", padx=10, pady=10, font="16", command=Develop)
BL.place(x=0, y=350)

root.mainloop()
