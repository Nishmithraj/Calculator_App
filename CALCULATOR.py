from tkinter import *

# Create a window
root = Tk()
root.title("NPR Calculator")

e = Entry(root, width=5, border=8, font=('calibri', 25, 'bold'))
e.grid(row=0, column=0, columnspan=3, sticky=E + W)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


# Define buttons
button1 = Button(root, text="1", padx=36, pady=12, command=lambda: button_click(1), bg="black", fg="white")
button2 = Button(root, text="2", padx=36, pady=12, command=lambda: button_click(2), bg="black", fg="white")
button3 = Button(root, text="3", padx=36, pady=12, command=lambda: button_click(3), bg="black", fg="white")
button4 = Button(root, text="4", padx=36, pady=12, command=lambda: button_click(4), bg="black", fg="white")
button5 = Button(root, text="5", padx=36, pady=12, command=lambda: button_click(5), bg="black", fg="white")
button6 = Button(root, text="6", padx=36, pady=12, command=lambda: button_click(6), bg="black", fg="white")
button7 = Button(root, text="7", padx=36, pady=12, command=lambda: button_click(7), bg="black", fg="white")
button8 = Button(root, text="8", padx=36, pady=12, command=lambda: button_click(8), bg="black", fg="white")
button9 = Button(root, text="9", padx=36, pady=12, command=lambda: button_click(9), bg="black", fg="white")
button0 = Button(root, text="0", padx=36, pady=12, command=lambda: button_click(0), bg="black", fg="white")
buttonplus = Button(root, text="+", padx=36, pady=12, command=button_add, bg="black", fg="white")
buttoneq = Button(root, text="=", padx=36, pady=12, command=button_equal, bg="black", fg="white")
buttonclr = Button(root, text="Clear", padx=113, pady=12, command=button_clear, bg="black", fg="white")
buttonexit = Button(root, text="EXIT", bg="black", fg="white", command=root.destroy)

buttonminus = Button(root, text="-", padx=38, pady=12, command=button_sub, bg="black", fg="white")
buttonmultiply = Button(root, text="*", padx=36, pady=12, command=button_mul, bg="black", fg="white")
buttondevide = Button(root, text="/", padx=36, pady=12, command=button_div, bg="black", fg="white")

# Put buttons on the grid

button7.grid(row=1, column=0, sticky=E + W)
button8.grid(row=1, column=1, sticky=E + W)
button9.grid(row=1, column=2, sticky=E + W)

button4.grid(row=2, column=0, sticky=E + W)
button5.grid(row=2, column=1, sticky=E + W)
button6.grid(row=2, column=2, sticky=E + W)

button1.grid(row=3, column=0, sticky=E + W)
button2.grid(row=3, column=1, sticky=E + W)
button3.grid(row=3, column=2, sticky=E + W)

button0.grid(row=4, column=0, sticky=E + W)
buttonplus.grid(row=4, column=1, sticky=E + W)
buttonminus.grid(row=4, column=2, sticky=E + W)

buttonmultiply.grid(row=5, column=0, sticky=E + W)
buttoneq.grid(row=5, column=2, sticky=E + W)
buttondevide.grid(row=5, column=1, sticky=E + W)

buttonclr.grid(row=6, column=0, columnspan=3, sticky=E + W)
buttonexit.grid(row=7, column=0, columnspan=3, sticky=W+E)

# beautify
button1.config(font=('calibri', 15, 'bold'))
button2.config(font=('calibri', 15, 'bold'))
button3.config(font=('calibri', 15, 'bold'))
button4.config(font=('calibri', 15, 'bold'))
button5.config(font=('calibri', 15, 'bold'))
button6.config(font=('calibri', 15, 'bold'))
button7.config(font=('calibri', 15, 'bold'))
button8.config(font=('calibri', 15, 'bold'))
button9.config(font=('calibri', 15, 'bold'))
button0.config(font=('calibri', 15, 'bold'))

buttonplus.config(font=('calibri', 15, 'bold'))
buttoneq.config(font=('calibri', 15, 'bold'))
buttonminus.config(font=('calibri', 15, 'bold'))
buttonmultiply.config(font=('calibri', 15, 'bold'))
buttondevide.config(font=('calibri', 15, 'bold'))
buttonclr.config(font=('calibri', 15, 'bold'))

root.mainloop()
