from uuid import uuid1

import boto3
from config import Settings
from models import Wish


# https://practicum.yandex.ru/trainer/ycloud/lesson/0914346c-22d5-4180-b1c2-2d1134133de7/

class YDBclient:
    def __init__(self):
        self.settings = Settings()
        self.ydb_docapi_client = boto3.resource('dynamodb',
                                                endpoint_url=self.settings.wish_database_document_api_endpoint,
                                                region_name=self.settings.region,
                                                aws_access_key_id=self.settings.aws_key_id,
                                                aws_secret_access_key=self.settings.aws_secret)

    def create_table(self):
        wish_table = self.ydb_docapi_client.create_table(
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
        replica_table = self.ydb_docapi_client.create_table(
            TableName='replica',
            KeySchema=[
                {
                    'AttributeName': 'replica_id',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'replica_id',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'count',
                    'AttributeType': 'N'
                }
            ]
        )
        self.ydb_docapi_client.Table('replica').put_item(Item={'replica_id': 0, 'count': 0})
        return [wish_table, replica_table]

    def load_data(self, wish: Wish):
        table = self.ydb_docapi_client.Table('wishes')
        wish_id = uuid1().hex
        table.put_item(Item={
            'wish_id': wish_id,
            'title': wish.title,
            'author': wish.author,
            'description': wish.description,
            'whom': wish.whom
        })
        return wish_id

    def get_items(self):
        table = self.ydb_docapi_client.Table('wishes')
        response = table.scan()
        data = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

        return data

    def get_replica(self):
        table = self.ydb_docapi_client.Table('replica')
        inc = table.update_item(
            Key={
                'replica_id': 0
            },
            UpdateExpression='ADD count :val',
            ExpressionAttributeValues={":val": 1},
            ReturnValues="UPDATED_NEW"
        )
        return inc['Attributes']['count']
