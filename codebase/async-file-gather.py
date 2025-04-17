from fastapi import FastAPI
import aiohttp

app = FastAPI()

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.example.com/data") as resp:
            return await resp.json()

@app.get("/data")
async def get_data():
    data = await fetch_data()
    return {"result": data}
