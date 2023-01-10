from pydantic import BaseSettings


class Settings(BaseSettings):
    port: int = 8080
    host: str = '127.0.0.1'
    wish_database_document_api_endpoint: str = "https://docapi.serverless.yandexcloud.net/ru-central1/b1gnl9lju0pb9teqm9bc/etngt8umlml966r2obvc"
    region: str = 'ru-central1'
    aws_key_id: str = None
    aws_secret: str = None
    version: str = '0.0.1'
