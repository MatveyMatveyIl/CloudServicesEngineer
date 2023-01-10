locals {
  website_gateway_name = "wishes-website-gateway"
}

resource "yandex_api_gateway" "wishes_website_gateway" {
  name      = local.website_gateway_name
  folder_id = local.folder_id
  spec      = file("../front/website.yaml")
}

output "wishes_website_gateway_domain" {
  value = "https://${yandex_api_gateway.wishes_website_gateway.domain}"
}