# Инструкция

1. cd deploy
2. provider.tf вставить нужные данные
3. make init
4. make preparation
5. внести нужные кредиты в енв
6. export $(grep -v '^#' credentials | xargs)
7. выдать права для sa make
8. в файле access_key данные для aws
9. aws configure - ввести данные из файла https://cloud.yandex.ru/docs/ydb/docapi/tools/aws-setup
10. поменять данные в api.yaml
11. make configure_be_gateway
12. для деплоя бэка make backend_deploy


