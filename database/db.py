# database.py

import sqlite3

class DatabaseManager:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                national_id TEXT NOT NULL,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                address TEXT,
                gender TEXT
            )
        """)
        self.conn.commit()

    def insert_student(self, national_id, name, email, phone, address, gender):
        self.cursor.execute("""
            INSERT INTO students (national_id, name, email, phone, address, gender)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (national_id, name, email, phone, address, gender))
        self.conn.commit()

    def fetch_all_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def search_students(self, field, value):
        query = f"SELECT * FROM students WHERE {field} LIKE ?"
        self.cursor.execute(query, ('%' + value + '%',))
        return self.cursor.fetchall()

    def update_student(self, student_id, national_id, name, email, phone, address, gender):
        self.cursor.execute("""
            UPDATE students
            SET national_id=?, name=?, email=?, phone=?, address=?, gender=?
            WHERE id=?
        """, (national_id, name, email, phone, address, gender, student_id))
        self.conn.commit()

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
