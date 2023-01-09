locals {
  database_name = "wish-database"
}

resource "yandex_ydb_database_serverless" "wish_db" {
  name      = local.database_name
  folder_id = local.folder_id
}

output "wish_database_document_api_endpoint" {
  value = yandex_ydb_database_serverless.wish_db.document_api_endpoint
}

output "wish_database_path" {
  value = yandex_ydb_database_serverless.wish_db.database_path
}