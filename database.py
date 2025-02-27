import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def get_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

def store_submission(user_id, problem_id, code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO submissions (user_id, problem_id, submission_code, timestamp)
        VALUES (%s, %s, %s, NOW())
    """, (user_id, problem_id, code))
    conn.commit()
    conn.close()
