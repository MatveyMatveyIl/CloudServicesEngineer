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




# Инструкция

## До начала работы
### установить 
1. YCL (https://cloud.yandex.ru/docs/cli/operations/install-cli#interactive)
2. aws CLI 
3. docker 
4. Terraform 
5. python 
6. bash
7. make

## Создание инфраструктуры
1. подготовить профиль Яндекс.Облако
2. подготовить данные:
   - cloud_id
   - folder_id
   - OAuth-токен(https://cloud.yandex.ru/docs/iam/concepts/authorization/oauth-token)
3. ```bash 
   cd deploy
   ```
4. provider.tf вставить данные из шага 2
5. ```bash 
   make init
   ```
   - обратите внимание, что появляется файл credentials
   - выдаются права на выполнение скриптов(желательно иметь OS Linux/macOS)

6. ```bash
   make preparation
   ```
   - на каждом шаге ввести yes
   - в конце вывода будут данные, которые нужно вставить в credentials

7. ```bash
   export $(grep -v '^#' credentials | xargs)
   ```
8. ```bash
   make sa_permissions
   ```
   - Выдаем права сервисному аккаунта
   - Появится файл access_key
9. ```bash
   aws configure
   ```
   - ввести данные из access_key
10. внести данные в obj_storage.tf + make create_obj_storage
11. ```bash 
    cd ../api
    ```
    - Поменять данные в api.yaml ${APP_SERVICE_ACCOUNT_ID}, ${WISH_API_CONTAINER_ID}
    - ```bash
      python3 /src/initTable.py
      ```
12. ```bash
    cd ../frontend
    ```
    - Поменять данные в web.yaml

13. ```bash
    cd ../deploy
    ```
14. ```bash
    make configure_apigetway
    ```
15. внести данные в cred + export $(grep -v '^#' credentials | xargs)
    

## Обновление приложения
- для обновления api
  - ```bash 
    make deploy_backend
    ```
- для обновления web
  - ```bash 
    make deploy_web
    ```