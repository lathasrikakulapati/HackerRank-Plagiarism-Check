import mysql.connector

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="hackerrank"
)
cursor = db.cursor()

# Function to Insert Data into MySQL
def store_submission(username, problem, score, code):
    query = "INSERT INTO submissions (username, problem, score, code) VALUES (%s, %s, %s, %s)"
    values = (username, problem, score, code)
    cursor.execute(query, values)
    db.commit()

# Insert Extracted Data
for submission in data:
    store_submission(submission["username"], submission["problem"], submission["score"], submission["code"])

# Close Database Connection
cursor.close()
db.close()
