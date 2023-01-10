init: create_env_file
	chmod +x ./sa_roles.sh
	chmod +x ../api/deploy.sh
	terraform init
destroy:
	terraform destroy
preparation: create_sa create_db create_registry configure_docker create_sls_container
configure_apigetway: configure_be_gateway configure_fe_gateway

create_obj_storage:
	terraform apply -target=yandex_storage_bucket.wishes_website_bucket
create_env_file:
	cat credentials.example > credentials
create_sa:
	terraform apply -target=yandex_iam_service_account.app_service_account
create_db:
	terraform apply -target=yandex_ydb_database_serverless.wish_db
create_registry:
	terraform apply -target=yandex_container_registry.default
	terraform apply -target=yandex_container_repository.api_rep
configure_docker:
	yc container registry configure-docker
create_sls_container:
	yc sls container create --name wish-api-container --folder-id ${FOLDER_ID}

configure_be_gateway:
	terraform apply -target=yandex_api_gateway.wishesbe_api_gateway
configure_fe_gateway:
	terraform apply -target=yandex_api_gateway.wishes_website_gateway


sa_permissions: get_roles get_access-key

get_roles:
	./sa_roles.sh
get_access-key:
	yc iam access-key create --service-account-id ${APP_SERVICE_ACCOUNT_ID} > access_key


deploy_backend:
	cd ../api && ./deploy.sh cd ../deploy;

deploy_web:
	cd ../front && ./deploy.sh cd ../deploy;

data:
	export $(grep -v '^#' credentials | xargs)

unset_env:
	unset $(grep -v '^#' credentials | sed -E 's/(.*)=.*/\1/' | xargs)