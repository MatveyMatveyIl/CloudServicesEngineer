locals {
    rep_name = "wish_api"
}

resource "yandex_container_registry" "default" {
  name      = "default"
  folder_id = local.folder_id
}

resource "yandex_container_repository" "api_rep" {
  name = "${yandex_container_registry.default.id}/${local.rep_name}"
}


output "wish_api_repository_name" {
  value = "cr.yandex/${yandex_container_repository.api_rep.name}"
}