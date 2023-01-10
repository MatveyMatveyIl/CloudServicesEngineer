#!/bin/sh

version=$(cat version.txt | awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}')

$(echo $version > version.txt)

code=$(cat index.js | tail -n +2)
echo 'const webVersion=' \"${version}\" > index.js
echo $code >> index.js

aws --endpoint-url=https://storage.yandexcloud.net s3 cp index.html  s3://${WISHES_WEBSITE_BUCKET}
aws --endpoint-url=https://storage.yandexcloud.net s3 cp index.js   s3://${WISHES_WEBSITE_BUCKET}
