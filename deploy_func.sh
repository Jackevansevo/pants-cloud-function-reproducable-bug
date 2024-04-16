#/bin/bash
set -eou pipefail

pants package functions:cloud_function
gsutil cp dist/functions/cloud_function.zip gs://gcf-v2-sources-1024641440084-southamerica-east1/function-example.zip

gcloud functions deploy \
	--allow-unauthenticated \
	--entry-point=handler \
	--gen2 \
	--region=southamerica-east1 \
	--runtime=python311 \
	--set-env-vars=DB_HOST=/cloudsql/example-419500:europe-west2:example \
	--set-secrets=DB_PASSWORD=projects/1024641440084/secrets/DB_PASSWORD:latest \
	--trigger-http \
	--source=gs://gcf-v2-sources-1024641440084-southamerica-east1/function-example.zip \
	function-example

gcloud run services update \
	--set-cloudsql-instances=example-419500:europe-west2:example \
	--region=southamerica-east1 \
	function-example
