locals {
  website_bucket_name = "wishes-website-bucket"
}

resource "yandex_storage_bucket" "wishes_website_bucket" {
  bucket     = local.website_bucket_name
  access_key = ""
  secret_key = ""
}

output "wishes_website_bucket" {
  value = yandex_storage_bucket.wishes_website_bucket.bucket
}