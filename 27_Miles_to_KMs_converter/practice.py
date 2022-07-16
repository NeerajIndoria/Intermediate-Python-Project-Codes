# def add(*args):
#     # print(sum(args))
#     addition = 0
#     for n in args:
#         addition += n
#     print(addition)
#
#
# add(3, 4, 5, 3, 5, 3, 5)
from tkinter import *


def change_label():
    label1['text'] = user_input.get()


def change_label_again():
    label1.config(text="Back to Basics")


window = Tk()
window.title("My Gui Bakchodi")
window.minsize(width=500, height=400)

label1 = Label(text="Hello World!", width=10)
label1.grid(row=0, column=0)

button1 = Button(text="Click Me!", command=change_label)
button1.grid(row=1, column=1)
button2 = Button(text="Click Me!", command=change_label_again)
button2.grid(row=0, column=2)

user_input = Entry(width=20)
user_input.insert(END, string="Email: ")
user_input.grid(row=2, column=3)

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Something about you")
text.grid(row=4, column=0)


def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(row=4, column=2)


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, width=10, command=scale_used)
scale.grid(row=5, column=0)


def check_button_used():
    print(checked_state.get())


checked_state = IntVar()
check_button = Checkbutton(text="Is On?", variable=checked_state, command=check_button_used)
checked_state.get()
check_button.grid(row=5, column=1)


def radio_button_used():
    print(radio_state.get())


radio_state = IntVar()
radio_button = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_button_used)
radio_button1 = Radiobutton(text="Option1", value=2, variable=radio_state, command=radio_button_used)
radio_button.grid(row=6, column=0)
radio_button1.grid(row=7, column=0)


def listbox_used():
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<listboxselect>>", listbox_used)
listbox.grid(row=6, column=2, columnspan=2)

window.mainloop()
