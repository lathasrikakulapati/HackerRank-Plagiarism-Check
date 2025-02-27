from fastapi import FastAPI
from plagiarism_check import check_plagiarism

app = FastAPI()

@app.get("/check_plagiarism")
def plagiarism_api():
    similarity_matrix = check_plagiarism()
    return {"similarity_matrix": similarity_matrix.tolist()}
