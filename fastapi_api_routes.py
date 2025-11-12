# minimal_fastapi.py
from fastapi import FastAPI, HTTPException
from datetime import date
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root(name: Optional[str] = None):
    message = f"Hello, {name}!" if name else "Hello, World!"
    return {"message": message}

@app.get("/hello")
def greet_with_age(name: str, yob: int):
    current_year = date.today().year
    if yob > current_year:
        raise HTTPException(status_code=400, detail="Year of birth cannot be in the future.")
    age = current_year - yob
    return {"message": f"Hello, {name}! You are {age} years old."}