from uuid import uuid1

import boto3
from config import Settings
from models import Wish


# https://practicum.yandex.ru/trainer/ycloud/lesson/0914346c-22d5-4180-b1c2-2d1134133de7/

class YDBclient:
    def __init__(self):
        self.settings = Settings()
        self.ydb_docapi_client = boto3.resource('dynamodb',
                                                endpoint_url=self.settings.wish_database_document_api_endpoint)

    def create_table(self):
        table = self.ydb_docapi_client.create_table(
            TableName='wishes',
            KeySchema=[
                {
                    'AttributeName': 'wish_id',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'title',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'wish_id',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'title',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'author',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'description',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'whom',
                    'AttributeType': 'S'
                },
            ]
        )
        return table

    def load_data(self, wish: Wish):
        table = self.ydb_docapi_client.Table('wishes')
        for item in table.objects.all():
            print(item)
        table.put_item(Item={
            'wish_id': uuid1().hex,
            'title': wish.title,
            'author': wish.author,
            'description': wish.description,
            'whom': wish.whom
        })

    def get_items(self):
        table = self.ydb_docapi_client.Table('wishes')
        response = table.scan()
        data = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

        return data
