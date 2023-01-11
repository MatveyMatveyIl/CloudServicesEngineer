npm version patch
npm run build

aws --endpoint-url=https://storage.yandexcloud.net s3 cp --recursive build s3://${WISHES_WEBSITE_BUCKET}
