import tkinter as tk
from registration_form import show_registration_form, show_student_list

root = tk.Tk()
root.title("Student Management System")
root.geometry("400x200")

tk.Label(root, text="Student Management System", font=("Arial", 16)).pack(pady=20)
tk.Button(root, text="Add Student", font=("Arial", 14), command=show_registration_form).pack(pady=10)
tk.Button(root, text="View Students", font=("Arial", 14), command=show_student_list).pack(pady=10)

root.mainloop()
