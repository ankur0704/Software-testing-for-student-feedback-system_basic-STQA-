import sqlite3

def get_connection():
    return sqlite3.connect('feedback.db')

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            subject TEXT NOT NULL,
            rating INTEGER CHECK(rating >= 1 AND rating <= 5),
            comments TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_feedback(student_name, subject, rating, comments):
    if not (1 <= rating <= 5):
        return {"error": "Rating must be between 1 and 5"}
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO feedback (student_name, subject, rating, comments) VALUES (?, ?, ?, ?)",
                (student_name, subject, rating, comments))
    conn.commit()
    conn.close()
    return {"message": "Feedback added successfully"}

def get_all_feedback():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM feedback")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "student_name": r[1], "subject": r[2], "rating": r[3], "comments": r[4]} for r in rows]
