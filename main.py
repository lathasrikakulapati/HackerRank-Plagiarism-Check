from scraper import fetch_submissions
from api import app
import uvicorn

if __name__ == "__main__":
    fetch_submissions()
    uvicorn.run(app, host="0.0.0.0", port=8000)
