# CloudServicesEngineer

- выполнить препрцесс
- установить енв в файл
- сделать export $(grep -v '^#' credentials | xargs)

- ```yc config profile list```
- ```yc config profile get default```

yc iam key create \
--service-account-id "ajejks84kk99nvp6ebdm" \
--folder-name "task" \
--output key.json

https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-quickstart#configure-provider