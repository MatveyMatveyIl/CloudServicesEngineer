#!/bin/sh

yc resource-manager folder add-access-binding ${FOLDER_ID} --role ydb.admin --subject serviceAccount:${APP_SERVICE_ACCOUNT_ID}
yc resource-manager folder add-access-binding ${FOLDER_ID} --role container-registry.images.puller --subject serviceAccount:${APP_SERVICE_ACCOUNT_ID}
yc resource-manager folder add-access-binding ${FOLDER_ID} --role serverless.containers.invoker --subject serviceAccount:${APP_SERVICE_ACCOUNT_ID}
yc resource-manager folder add-access-binding ${FOLDER_ID} --role storage.editor --subject serviceAccount:${APP_SERVICE_ACCOUNT_ID}
yc resource-manager folder add-access-binding ${FOLDER_ID} --role yds.admin --subject serviceAccount:${APP_SERVICE_ACCOUNT_ID}
