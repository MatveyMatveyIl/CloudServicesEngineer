import uvicorn
from fastapi import FastAPI, Request

from config import Settings
from models import Wish
from schemes import WishesOut, ApiInfo, WishOut
from wishService import WishService

settings = Settings()
app = FastAPI()
service = WishService()
replica_id = service.get_replica_id()
api_info = ApiInfo(name='Wish api', version=settings.version, replica_id=replica_id)


@app.get('/')
async def root():
    return {'message': 'Wishes api'}


@app.get('/api', response_model=ApiInfo)
async def get_api_info():
    return api_info


@app.get('/api/ping', status_code=200)
async def ping(request: Request):
    return {'message': 'ok!'}


@app.get('/api/wishes', response_model=WishesOut, status_code=200)
async def get_wishes():
    wishes = await service.get_wishes()
    return {'wishes': wishes, 'api_info': api_info}


@app.post('/api/wish', status_code=201, response_model=WishOut)
async def create_wish(author: str, title: str, description: str, whom: str):
    wish = Wish(author=author, title=title, description=description, whom=whom, wish_id='1')
    created_wish = await service.create_wish(wish)
    return {'wish': created_wish, 'api_info': api_info}


if __name__ == '__main__':
    uvicorn.run(app, host=settings.host, port=settings.port)
