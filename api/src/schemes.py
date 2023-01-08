from pydantic import BaseModel
from models import Wish


class WishesOut(BaseModel):
    wishes: list[Wish] = []
