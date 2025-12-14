from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import aiofiles

app = FastAPI()

# Разрешаем запросы с любого источника
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit")
async def submit_data(request: Request):
    data = await request.json()
    text = data.get("text", "")
    async with aiofiles.open("data.txt", mode="a", encoding="utf-8") as f:
        await f.write(text + "\n")
    return {"status": "success", "message": "Данные приняты"}
