from pydantic import BaseModel
from models import Wish


class ApiInfo(BaseModel):
    name: str
    version: str
    replica_id: str


class WishesOut(BaseModel):
    wishes: list[Wish] = []
    api_info: ApiInfo


class WishOut(BaseModel):
    wish: Wish
    api_info: ApiInfo
