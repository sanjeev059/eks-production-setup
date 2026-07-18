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
    }
@app.get("/")
def root():
    return {
        "status": "Application Running",
        "pod": os.getenv("HOSTNAME")
    }