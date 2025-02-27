from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from database import store_submission
from config import HACKERRANK_EMAIL, HACKERRANK_PASSWORD

def login_hackerrank(driver):
    driver.get("https://www.hackerrank.com/auth/login")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-1").send_keys(HACKERRANK_EMAIL)
    driver.find_element(By.ID, "input-2").send_keys(HACKERRANK_PASSWORD, Keys.RETURN)
    time.sleep(3)

def fetch_submissions():
    driver = webdriver.Chrome()
    login_hackerrank(driver)
    
    driver.get("https://www.hackerrank.com/submissions")
    time.sleep(2)
    
    submissions = driver.find_elements(By.CLASS_NAME, "submission-code")
    for submission in submissions:
        user_id = "test_user"
        problem_id = "test_problem"
        code = submission.text
        store_submission(user_id, problem_id, code)
    
    driver.quit()
