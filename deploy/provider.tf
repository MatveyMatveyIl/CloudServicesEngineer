terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token     = local.token
  cloud_id  = local.cloud_id
  folder_id = local.folder_id
  zone      = local.zone
}


locals {
  token      = "y0_AgAAAABkukKLAATuwQAAAADQHfuJ3uMAeFnuRNiSTu-6So0H7UxhnHY"
  cloud_id   = "b1gnl9lju0pb9teqm9bc"
  folder_id  = "b1glgksk5r3280agln0r"
  zone       = "ru-central1-a"
}