from tkinter import *
import random

root = Tk()
root.title("Custom Password Generator")

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
numbers = "0123456789"
symbols = "~!@#$%^&*()_+"


all_ans = lowercase + uppercase + numbers + symbols
all_but_sym = lowercase + uppercase + numbers
all_but_num = lowercase + uppercase + symbols
all_but_caps = lowercase + numbers + symbols
only_letters = lowercase + uppercase
nums = lowercase + numbers
symbols = lowercase + symbols

lgth = Label(root, text="Password Length?")
lgth.grid(row=0, column=0)

e = Entry(root, width=2, borderwidth=2, text="10")
e.grid(row=1, column=0)
e.insert(0, "10")

cs = IntVar()
c = Checkbutton(root, text="Symbols?", variable=cs, onvalue=1, offvalue=0)
c.grid(row=4, column=0, padx=10, pady=10)

cc = IntVar()
check_caps = Checkbutton(root, text="Caps?", variable=cc, onvalue=1, offvalue=0)
check_caps.grid(row=2, column=0, padx=10, pady=10)

cn = IntVar()
check_nums = Checkbutton(root, text="Nums?", variable=cn, onvalue=1, offvalue=0)
check_nums.grid(row=3, column=0, padx=10, pady=10)


def generate():
    length = int(e.get())

    if cs.get() == 1 and cc.get() == 1 and cn.get() == 1:
        my_password = Text(root, height=1, borderwidth=2, width=32)
        my_password.insert(1.0, "".join(random.sample(all_ans, length)))
        my_password.grid(row=6, column=0, columnspan=1)

    elif cs.get() == 1 and cc.get() == 1 and cn.get() == 0:
        my_password = Text(root, height=1, borderwidth=2, width=32)
        my_password.insert(1.0, "".join(random.sample(all_but_num, length)))
        my_password.grid(row=6, column=0)

    elif cs.get() == 1 and cc.get() == 0 and cn.get() == 1:
        my_password = Text(root, height=1, borderwidth=2, width=32)
        my_password.insert(1.0, "".join(random.sample(all_but_caps, length)))
        my_password.grid(row=6, column=0)

    elif cs.get() == 0 and cc.get() == 1 and cn.get() == 1:
        my_password = Text(root, height=1, borderwidth=2, width=32)
        my_password.insert(1.0, "".join(random.sample(all_but_sym, length)))
        my_password.grid(row=6, column=0)

    elif cs.get() == 1 and cc.get() == 0 and cn.get() == 0:
        my_password = Text(root, height=1, borderwidth=2, width=32)
        my_password.insert(1.0, "".join(random.sample(symbols, length)))
        my_password.grid(row=6, column=0)

    elif cs.get() == 0 and cc.get() == 1 and cn.get() == 0:
        my_password = Text(root, height=1, borderwidth=2, width=32)
        my_password.insert(1.0, "".join(random.sample(only_letters, length)))
        my_password.grid(row=6, column=0)

    elif cs.get() == 0 and cc.get() == 0 and cn.get() == 1:
        my_password = Text(root, height=1, borderwidth=2, width=32)
        my_password.insert(1.0, "".join(random.sample(nums, length)))
        my_password.grid(row=6, column=0)

    elif cs.get() == 0 and cc.get() == 0 and cn.get() == 0:
        my_password = Text(root, height=1, borderwidth=2, width=32)
        my_password.insert(1.0, "".join(random.sample(lowercase, length)))
        my_password.grid(row=6, column=0)


button_generate = Button(
    root, text="Generate", padx=40, pady=20, command=lambda: generate()
)
button_generate.grid(row=5, column=0)

root.mainloop()
