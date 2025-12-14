from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import aiofiles
import os

app = FastAPI()

# Разрешаем запросы с любого источника
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = os.getenv("DATA_PATH", "data.txt")

@app.post("/submit")
async def submit_data(request: Request):
    data = await request.json()
    text = data.get("text", "")
    async with aiofiles.open(DATA_PATH, mode="a", encoding="utf-8") as f:
        await f.write(text + "\n")
    return {"status": "success", "message": "Данные приняты"}

@app.get("/data")
async def get_data():
    try:
        async with aiofiles.open(DATA_PATH, mode="r", encoding="utf-8") as f:
            content = await f.read()
        return {"data": content}
    except FileNotFoundError:
        return {"data": ""}
