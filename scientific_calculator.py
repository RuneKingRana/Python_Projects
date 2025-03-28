import tkinter as tk
from math import sqrt, cbrt, sin, cos, tan, asin, acos, atan, radians, log, log10, factorial, pi, e, exp


def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(value))


def button_clear():
    display.delete(0, tk.END)


def button_clear_entry():
    display.delete(len(display.get()) - 1, tk.END)


def button_equal():
    try:
        expression = display.get().replace('\u00D7', '*').replace('\u00F7', '/').replace('^', '**')
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


def button_power():
    display.insert(tk.END, "^")


def button_negate():
    try:
        value = float(display.get()) * -1
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def button_sin():
    try:
        value = sin(radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def button_cos():
    try:
        value = cos(radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def button_tan():
    try:
        value = tan(radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def button_asin():
    try:
        value = asin(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def button_acos():
    try:
        value = acos(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def button_atan():
    try:
        value = atan(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def button_log():
    try:
        value = log10(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def button_ln():
    try:
        value = log(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def button_fact():
    try:
        value = factorial(int(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def button_exp():
    try:
        value = exp(int(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


root = tk.Tk()
root.title("Scientific Calculator")

display = tk.Entry(root, width=28, font=("Arial", 20), bd=6, justify="right")
display.grid(row=0, column=0, columnspan=5)

button_clear = tk.Button(root, text="C", font=("Arial", 15), padx=2, pady=10, width=9, height=1, command=button_clear,
                         bg="lightcoral")
button_clear_entry = tk.Button(root, text="⌫", font=("Arial", 15), padx=2, pady=10, width=9, height=1,
                               command=button_clear_entry, bg="lightcoral")
buttons = [
    ('%', button_percentage, None), ('1/x', button_inverse, None), ('π', lambda: button_click(str(pi)), None),
    ('e', lambda: button_click(str(e)), None),
    ('log', button_log, None), ('ln', button_ln, None), ('n!', button_fact, None), ('exp', button_exp, None),
    ('x²', button_square, None), ('x^y', button_power, None), ('²√x', button_sqrt, None), ('³√x', button_cbrt, None),
    ('sin', button_sin, None), ('cos', button_cos, None), ('tan', button_tan, None), ('+/-', button_negate, None),
    ('sin⁻¹', button_asin, None), ('cos⁻¹', button_acos, None), ('tan⁻¹', button_atan, None),
    ('÷', lambda: button_click("\u00F7"), None),
    ('7', lambda: button_click("7"), None), ('8', lambda: button_click("8"), None),
    ('9', lambda: button_click("9"), None), ('×', lambda: button_click("\u00D7"), None),
    ('4', lambda: button_click("4"), None), ('5', lambda: button_click("5"), None),
    ('6', lambda: button_click("6"), None), ('-', lambda: button_click("-"), None),
    ('1', lambda: button_click("1"), None), ('2', lambda: button_click("2"), None),
    ('3', lambda: button_click("3"), None), ('+', lambda: button_click("+"), None),
    ('00', lambda: button_click("00"), None), ('0', lambda: button_click("0"), None),
    ('.', lambda: button_click("."), None), ('=', button_equal, "lightgreen")
]

button_clear.grid(row=1, column=0, columnspan=2, sticky="nsew")
button_clear_entry.grid(row=1, column=2, columnspan=2, sticky="nsew")
row_val = 2
col_val = 0
for text, command, color in buttons:
    tk.Button(root, text=text, font=("Arial", 15), padx=2, pady=10, width=9, height=1, command=command, bg=color).grid(
        row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
