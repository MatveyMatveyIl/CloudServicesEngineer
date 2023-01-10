from YDBclient import YDBclient
from models import Wish


class WishService:
    def __init__(self):
        self.ydb_client = YDBclient()

    async def create_wish(self, wish: Wish):
        wish_id = self.ydb_client.load_data(wish)
        wish.wish_id = wish_id
        return wish

    async def get_wishes(self):
        items = self.ydb_client.get_items()
        wishes = [Wish.parse_obj(el) for el in items]
        return wishes

    def get_replica_id(self):
        return self.ydb_client.get_replica()
