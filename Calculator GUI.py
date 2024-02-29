import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=42, justify="right")
display.grid(row=0, column=0, columnspan=4)

button_1 = tk.Button(root, text="1", padx=100, pady=100, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=100, pady=100, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=100, pady=100, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=100, pady=100, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=100, pady=100, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=100, pady=100, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=100, pady=100, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=100, pady=100, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=100, pady=100, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=100, pady=100, command=lambda: button_click(0))

button_clear = tk.Button(root, text="C", padx=100, pady=100, bg = "red", command=button_clear)
button_equal = tk.Button(root, text="=", padx=100, pady=100, bg = "blue", command=button_equal)
button_plus = tk.Button(root, text="+", padx=100, pady=100, command=lambda: button_click("+"))
button_minus = tk.Button(root, text="-", padx=100, pady=100, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=100, pady=100, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=100, pady=100, command=lambda: button_click("/"))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()
