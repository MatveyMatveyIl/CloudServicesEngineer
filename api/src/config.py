from pydantic import BaseSettings


class Settings(BaseSettings):
    port: int = 8080
    host: str = '127.0.0.1'
    wish_database_document_api_endpoint: str
    region: str = 'ru-central1'
    aws_key_id: str = None
    aws_secret: str = None
    version: str = '0.0.1'
