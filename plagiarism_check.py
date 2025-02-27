from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import mysql.connector
from database import get_connection

def fetch_all_submissions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT submission_code FROM submissions")
    submissions = [row[0] for row in cursor.fetchall()]
    conn.close()
    return submissions

def check_plagiarism():
    submissions = fetch_all_submissions()
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(submissions)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix
