import tkinter as tk
from math import sqrt, cbrt

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(value))

def button_clear():
    display.delete(0, tk.END)

def button_clear_entry():
    display.delete(len(display.get())-1, tk.END)

def button_equal():
    try:
        expression = display.get().replace('\u00D7', '*').replace('\u00F7', '/')
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_percentage():
    try:
        value = float(display.get()) / 100
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_inverse():
    try:
        value = 1 / float(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_square():
    try:
        value = float(display.get()) ** 2
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_sqrt():
    try:
        value = sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_cbrt():
    try:
        value = cbrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_negate():
    try:
        value = float(display.get()) * -1
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Basic Calculator")

display = tk.Entry(root, width=28, font=("Arial", 20), bd=6, justify="right")
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('%', button_percentage, None), ('1/x', button_inverse, None), ('C', button_clear, "lightcoral"), ('⌫', button_clear_entry, "lightcoral"),
     ('x²', button_square, None), ('²√x', button_sqrt, None), ('³√x', button_cbrt, None), ('÷', lambda: button_click("\u00F7"), None),
    ('7', lambda: button_click("7"), None), ('8', lambda: button_click("8"), None), ('9', lambda: button_click("9"), None), ('×', lambda: button_click("\u00D7"), None),
    ('4', lambda: button_click("4"), None), ('5', lambda: button_click("5"), None), ('6', lambda: button_click("6"), None), ('-', lambda: button_click("-"), None),
    ('1', lambda: button_click("1"), None), ('2', lambda: button_click("2"), None), ('3', lambda: button_click("3"), None), ('+', lambda: button_click("+"), None),
    ('+/-', button_negate, None), ('0', lambda: button_click("0"), None), ('.', lambda: button_click("."), None), ('=', button_equal, "lightgreen")
]

row_val = 1
col_val = 0
for text, command, color in buttons:
    tk.Button(root, text=text, font=("Arial", 15), padx=3, pady=3,width=9,height=3, command=command, bg=color).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()