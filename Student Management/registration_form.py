import tkinter as tk
from tkinter import messagebox
import requests

def show_registration_form():
    def register_user():
        data = {
            'name': entry_name.get(),
            'email': entry_email.get(),
            'roll_number': entry_roll.get(),
            'stream': entry_stream.get(),
            'year': entry_year.get(),
            'semester': entry_semester.get(),
            'password': entry_password.get()
        }

        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            res = requests.post("http://127.0.0.1:5000/students", json=data)
            messagebox.showinfo("Success", res.json().get('message', 'Success!'))
            reg_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not connect to server: {e}")

    reg_window = tk.Toplevel()
    reg_window.title("Student Registration Form")
    reg_window.geometry("600x550")

    frame = tk.Frame(reg_window)
    frame.pack(pady=10)

    labels = ["Name:", "Email:", "Roll Number:", "Stream:", "Year:", "Semester:", "Password:"]
    entries = []
    for i, text in enumerate(labels):
        tk.Label(frame, text=text, width=15, font=("Arial", 12), anchor="w").grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(frame, width=30, font=("Arial", 12))
        entry.grid(row=i, column=1, padx=5, pady=5, ipady=5)
        entries.append(entry)

    entry_name, entry_email, entry_roll, entry_stream, entry_year, entry_semester, entry_password = entries

    tk.Button(reg_window, text="Register", font=("Arial", 12), command=register_user).pack(ipadx=20, ipady=5, pady=10)

def show_student_list():
    try:
        res = requests.get("http://127.0.0.1:5000/students")
        students = res.json()
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch students: {e}")
        return

    list_window = tk.Toplevel()
    list_window.title("Student List")
    list_window.geometry("1500x400")

    frame = tk.Frame(list_window)
    frame.pack(pady=10)

    headers = ["ID", "Name", "Email", "Roll", "Stream", "Year", "Semester", "Delete"]
    for col, text in enumerate(headers):
        tk.Label(frame, text=text, font=("Arial", 10, "bold"), borderwidth=1, relief="solid", width=23).grid(row=0, column=col)

    for i, student in enumerate(students):
        for j, key in enumerate(["id", "name", "email", "roll_number", "stream", "year", "semester"]):
            tk.Label(frame, text=student[key], borderwidth=1, relief="solid", width=26).grid(row=i+1, column=j)
        del_btn = tk.Button(frame, text="Delete", fg="red", command=lambda sid=student["id"]: delete_student(sid, list_window))
        del_btn.grid(row=i+1, column=7)

def delete_student(student_id, window):
    try:
        res = requests.delete(f"http://127.0.0.1:5000/students/{student_id}")
        messagebox.showinfo("Success", res.json().get('message', 'Deleted!'))
        window.destroy()
        show_student_list()  # Refresh list
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete student: {e}")
