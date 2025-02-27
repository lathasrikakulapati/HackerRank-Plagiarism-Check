# 📌 HackerRank Plagiarism Check  

## 🚀 Overview  
This project **scrapes HackerRank submissions** using **Selenium**, stores them in a **MySQL database**, and **detects plagiarism** using **Machine Learning (TF-IDF and Cosine Similarity)**. A **FastAPI backend** provides an API endpoint for checking plagiarism.

---

## 💁️‍♂️ Folder Structure  
```
hackerrank-plagiarism-check/
│── main.py                # Entry point  
│── scraper.py             # Web Scraping using Selenium  
│── database.py            # MySQL Database connection  
│── plagiarism_check.py    # ML-based similarity detection  
│── api.py                 # FastAPI backend  
│── requirements.txt       # Required libraries  
│── config.py              # Config file (HackerRank credentials, DB details)  
```

---

## 🛠️ Setup Instructions  

### 1️⃣ Install Required Libraries  
```bash
pip install -r requirements.txt
```

### 2️⃣ Set Up MySQL Database  
Run the following SQL script to create the database and table:  
```sql
CREATE DATABASE plagiarism_db;
USE plagiarism_db;

CREATE TABLE submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255),
    problem_id VARCHAR(255),
    submission_code TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3️⃣ Configure `config.py`  
Edit the `config.py` file with your **HackerRank credentials** and **MySQL details**:  
```python
HACKERRANK_EMAIL = "your_email@example.com"
HACKERRANK_PASSWORD = "your_password"

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_mysql_password"
MYSQL_DATABASE = "plagiarism_db"
```

---

## 🔍 How It Works  

### 1️⃣ **Web Scraping (Selenium)**
- **Logs into HackerRank**
- **Fetches latest code submissions**
- **Stores them in the MySQL database**

Run the scraper:  
```bash
python scraper.py
```

### 2️⃣ **Plagiarism Detection (ML)**
- Uses **TF-IDF Vectorization** and **Cosine Similarity**
- Compares all submissions for plagiarism
- Returns a **similarity matrix**  

Run plagiarism check:  
```bash
python plagiarism_check.py
```

### 3️⃣ **FastAPI Backend**
- Provides a REST API to check plagiarism  
- API Endpoint: `http://127.0.0.1:8000/check_plagiarism`

Start the server:  
```bash
uvicorn api:app --reload
```
Visit API docs:  
```
http://127.0.0.1:8000/docs
```

---

## 📌 Features  
✅ **Automated web scraping** of HackerRank submissions  
✅ **Stores submissions** in a MySQL database  
✅ **Detects plagiarism** using Machine Learning (TF-IDF + Cosine Similarity)  
✅ **FastAPI backend** for accessing plagiarism results  
✅ **Easy setup & execution**  

---

## 🐝 License  
This project is **open-source** and available under the **MIT License**.

---
