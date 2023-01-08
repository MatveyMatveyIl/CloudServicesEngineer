import uvicorn
from fastapi import FastAPI

from config import Settings
from models import Wish
from schemes import WishesOut
from wishService import WishService

settings = Settings()
app = FastAPI()
service = WishService()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/ping")
async def ping():
    return {"message": "ok"}


@app.get("/api/wishes", response_model=WishesOut, status_code=200)
async def get_wishes():
    wishes = await service.get_wishes()
    return {"wishes": wishes}


@app.post("/api/wish", status_code=201, response_model=Wish)
async def create_wish(wish: Wish):
    await service.create_wish(wish)
    return {"title": wish.title, "author": wish.author, "description": wish.description, "whom": wish.whom}


if __name__ == '__main__':
    uvicorn.run(app, host=settings.host, port=settings.port)
