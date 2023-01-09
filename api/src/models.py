from pydantic import BaseModel


class Wish(BaseModel):
    wish_id: str
    title: str
    author: str
    description: str
    whom: str
