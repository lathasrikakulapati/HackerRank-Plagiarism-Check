from fastapi import FastAPI
import mysql.connector
import Levenshtein

app = FastAPI()

# Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="hackerrank"
    )

# API Endpoint to Detect Plagiarism
@app.get("/detect-plagiarism")
def detect_plagiarism():
    db = get_db_connection()
    cursor = db.cursor()

    # Fetch all submissions
    cursor.execute("SELECT id, username, problem, code FROM submissions")
    submissions = cursor.fetchall()
    
    plagiarized_pairs = []

    # Compare each pair of submissions
    for i in range(len(submissions)):
        for j in range(i + 1, len(submissions)):
            id1, user1, problem1, code1 = submissions[i]
            id2, user2, problem2, code2 = submissions[j]

            if problem1 == problem2:  # Compare only same problem submissions
                distance = Levenshtein.distance(code1, code2)
                similarity = 1 - (distance / max(len(code1), len(code2)))

                if similarity >= 0.8:  # 80% similarity threshold
                    plagiarized_pairs.append({
                        "user1": user1,
                        "user2": user2,
                        "problem": problem1,
                        "similarity": round(similarity * 100, 2)
                    })

    cursor.close()
    db.close()

    return {"plagiarism_results": plagiarized_pairs}

