from pydantic import BaseModel


class Wish(BaseModel):
    title: str
    author: str
    description: str
    whom: str
