import mysql.connector
import Levenshtein

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="hackerrank"
)
cursor = db.cursor()

# Fetch All Submissions from Database
cursor.execute("SELECT id, username, problem, code FROM submissions")
submissions = cursor.fetchall()

# Compare Each Pair of Submissions
plagiarized_pairs = []

for i in range(len(submissions)):
    for j in range(i + 1, len(submissions)):  # Avoid duplicate comparisons
        id1, user1, problem1, code1 = submissions[i]
        id2, user2, problem2, code2 = submissions[j]

        # Only compare submissions of the same problem
        if problem1 == problem2:
            distance = Levenshtein.distance(code1, code2)
            similarity = 1 - (distance / max(len(code1), len(code2)))  # Normalize similarity (0 to 1)

            if similarity >= 0.8:  # 80% similarity threshold
                plagiarized_pairs.append((user1, user2, problem1, similarity * 100))

# Print Plagiarized Code Pairs
print("\nPlagiarized Submissions:")
for pair in plagiarized_pairs:
    print(f"{pair[0]} and {pair[1]} plagiarized in problem '{pair[2]}' with {pair[3]:.2f}% similarity")

# Close Database Connection
cursor.close()
db.close()
