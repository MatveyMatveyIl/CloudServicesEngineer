locals {
  api_gateway_name = "wishesbe-api-gateway"
}

resource "yandex_api_gateway" "wishesbe_api_gateway" {
  name      = local.api_gateway_name
  folder_id = local.folder_id
  spec      = file("../api/api.yaml")
}

output "wishbe_api_gateway_domain" {
  value = "https://${yandex_api_gateway.wishesbe_api_gateway.domain}"
}