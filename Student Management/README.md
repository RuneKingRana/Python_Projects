# Student Management System

এই প্রজেক্টটি একটি সহজ Student Management System, যেখানে ছাত্রদের তথ্য যোগ, দেখা ও ডিলিট করা যায়।

## প্রয়োজনীয় সফটওয়্যার ও প্যাকেজ

- Python (3.7 বা তার উপরে)
- MySQL Server (XAMPP/WAMP/Standalone)
- Python প্যাকেজ: flask, flask-cors, mysql-connector-python, requests, tkinter

---

## ১. ডাটাবেস সেটআপ

১. MySQL চালু করুন।
২. `student_db.sql` ফাইলটি MySQL-এ রান করুন (phpMyAdmin বা MySQL CLI দিয়ে):

```sql
CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    roll_number VARCHAR(50),
    stream VARCHAR(50),
    year VARCHAR(10),
    semester VARCHAR(10),
    password VARCHAR(100)
);
```

---

## ২. প্রয়োজনীয় Python প্যাকেজ ইন্সটল

কমান্ড প্রম্পট/টার্মিনালে নিচের কমান্ড দিন:

```bash
pip install flask flask-cors mysql-connector-python requests
```

---

## ৩. MySQL কানেকশন সেটিং

`app.py`-এর এই অংশে আপনার MySQL ইউজারনেম ও পাসওয়ার্ড দিন:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="আপনার_পাসওয়ার্ড",
    database="student_db"
)
```

---

## ৪. সার্ভার চালু করুন

```bash
python app.py
```

এতে Flask API চালু হবে (ডিফল্ট: http://127.0.0.1:5000)

---

## ৫. GUI চালু করুন

নতুন টার্মিনালে:

```bash
python gui.py
```

---

## ৬. ব্যবহারের নিয়ম

- **Add Student:** নতুন ছাত্র যোগ করতে "Add Student" বাটনে ক্লিক করুন।
- **View Students:** ছাত্রদের তালিকা দেখতে "View Students" বাটনে ক্লিক করুন।
- **Delete:** তালিকা থেকে "Delete" বাটনে ক্লিক করলে ছাত্র ডিলিট হবে।

---

## ৭. সমস্যা হলে

- MySQL চালু আছে কিনা চেক করুন।
- পাসওয়ার্ড/ইউজারনেম ঠিক আছে কিনা দেখুন।
- Flask সার্ভার চালু আছে কিনা দেখুন।
- কোনো এরর হলে সেই মেসেজ দেখে সমাধান করুন বা ডেভেলপারকে জানান।

---

**শুভকামনা!** 