from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "Application Running",
        "environment": os.getenv("ENV"),
        "database": os.getenv("DB_HOST"),
        "db_username": os.getenv("DB_USERNAME"),
        "db_password": os.getenv("DB_PASSWORD")
<<<<<<< HEAD
    }
@app.get("/")
def root():
    return {
=======
>>>>>>> 2e361f1892b88901ca2e28a961fe7fa428f4e646
        "status": "Application Running",
        "pod": os.getenv("HOSTNAME")
    }