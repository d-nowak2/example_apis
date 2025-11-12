# minimal_fastapi.py
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root(name: Optional[str] = None):
    message = f"Hello, {name}!" if name else "Hello, World!"
    return {"message": message}