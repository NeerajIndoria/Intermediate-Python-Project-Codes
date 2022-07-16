from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)


def miles_to_kms():
    miles = entry1.get()
    kilometers = float(miles) * 1.609
    result_label.config(text=f"{kilometers}")


label1 = Label(text="is equals to", width=15)
label1.grid(row=1, column=0)
label2 = Label(text="Miles", width=15)
label2.grid(row=0, column=2)
label3 = Label(text="Km's", width=15)
label3.grid(row=1, column=2)

entry1 = Entry(width=10)
entry1.grid(row=0, column=1)

result_label = Label(text='0', width=10)
result_label.grid(row=1, column=1)

button = Button(text="Calculate", width=10, command=miles_to_kms)
button.grid(row=2, column=1)
window.mainloop()
