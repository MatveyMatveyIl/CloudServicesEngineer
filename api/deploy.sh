#!/bin/sh

version=$(cat version.txt | awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}')

$(echo $version > version.txt)

docker buildx build --platform linux/amd64 -f ./Dockerfile -t ${WISH_API_REPOSITORY_NAME}:${version} .
docker push ${WISH_API_REPOSITORY_NAME}:${version}

aws_key_id=$(cat ~/.aws/credentials | awk '{for (I=1;I<NF;I++) if ($I == "=") print $(I+1)}' | head -n 1);
aws_secret=$(cat ~/.aws/credentials | awk '{for (I=1;I<NF;I++) if ($I == "=") print $(I+1)}' | tail -n 1);

yc sls container revisions deploy \
    --container-id ${WISH_API_CONTAINER_ID} \
	--folder-id ${FOLDER_ID} \
	--memory 512M \
	--cores 1 \
	--execution-timeout 5s \
	--concurrency 4 \
	--environment WISH_DATABASE_DOCUMENT_API_ENDPOINT=${WISH_DATABASE_DOCUMENT_API_ENDPOINT},AWS_KEY_ID=${aws_key_id},AWS_SECRET=${aws_secret},VERSION=${version}\
	--service-account-id ${APP_SERVICE_ACCOUNT_ID} \
	--image ${WISH_API_REPOSITORY_NAME}:${version}