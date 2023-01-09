locals {
  service_account_name = "app-service-account"
}

resource "yandex_iam_service_account" "app_service_account" {
  name        =  local.service_account_name
}


output "app_service_account_id" {
  value = yandex_iam_service_account.app_service_account.id
}