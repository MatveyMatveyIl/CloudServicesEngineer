# CloudServicesEngineer
https://d5d73ha9tggp6r6eicml.apigw.yandexcloud.net/


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
10. внести данные aws в obj_storage.tf
    ```bash
    make create_obj_storage
    ```
    - добавить wishes_website_bucket в credentials
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
    - Поменять данные в web.yaml {APP_SERVICE_ACCOUNT_ID}, {WISHES_WEBSITE_BUCKET}

13. ```bash
    cd ../deploy
    ```
14. ```bash
    make configure_apigetway
    ```
15. внести данные в credentials
16. export $(grep -v '^#' credentials | xargs)
17. обновить переменную api в consts.js на ${WISHBE_API_GATEWAY_DOMAIN}

Эти настройки нужно провести один раз, чтобы поднять всю инфраструктуру облака.
    

## Обновление приложения
- для обновления api
  - ```bash 
    make deploy_backend
    ```
- для обновления web
  - ```bash 
    make deploy_web
    ```
