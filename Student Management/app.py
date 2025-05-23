from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pheon!xk!ngrana@84",
        database="student_db"
    )

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, email, roll_number, stream, year, semester, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (data['name'], data['email'], data['roll_number'], data['stream'], data['year'], data['semester'], data['password'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Student added successfully"})

@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, roll_number, stream, year, semester FROM students")
    result = cursor.fetchall()
    students = []
    for row in result:
        students.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "roll_number": row[3],
            "stream": row[4],
            "year": row[5],
            "semester": row[6]
        })
    cursor.close()
    conn.close()
    return jsonify(students)

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Student deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
