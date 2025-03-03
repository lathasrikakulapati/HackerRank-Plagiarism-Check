from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# HackerRank Credentials (Admin Required)
USERNAME = "your_hackerrank_email"
PASSWORD = "your_hackerrank_password"
CONTEST_URL = "https://www.hackerrank.com/contests/{contest_name}/submissions"

# Set up ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
driver = webdriver.Chrome(options=options)

def login_hackerrank():
    driver.get("https://www.hackerrank.com/auth/login")
    time.sleep(3)

    # Enter username
    email_field = driver.find_element(By.NAME, "username")
    email_field.send_keys(USERNAME)

    # Enter password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for login to complete

def scrape_submissions():
    driver.get(CONTEST_URL)
    time.sleep(5)

    submissions = []
    
    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) < 4:
            continue
        
        username = cols[0].text
        problem_name = cols[1].text
        score = cols[2].text
        submission_link = cols[3].find_element(By.TAG_NAME, "a").get_attribute("href")

        # Open submission page to extract code
        driver.get(submission_link)
        time.sleep(3)

        code_element = driver.find_element(By.CSS_SELECTOR, ".ace_content")
        code = code_element.text

        submissions.append({
            "username": username,
            "problem": problem_name,
            "score": score,
            "code": code
        })

        driver.back()  # Go back to submissions page
        time.sleep(2)

    return submissions

if __name__ == "__main__":
    login_hackerrank()
    data = scrape_submissions()
    
    for submission in data:
        print(submission)

    driver.quit()
