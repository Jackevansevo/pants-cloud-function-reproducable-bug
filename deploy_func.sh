#/bin/bash
set -eou pipefail

pants package functions:gcf
pushd dist/functions/gcf.pex
jq '.requirements | .[]' PEX-INFO -r > requirements.txt
echo 'from functions.main import handler' > main.py

cat <<EOT >> .gcloudignore
__main__.py
__pex__
PEX-INFO
.deps
.bootstrap
EOT

gcloud functions deploy \
	--allow-unauthenticated \
	--entry-point=handler \
	--gen2 \
	--region=europe-west2 \
	--runtime=python312 \
	--set-env-vars=DB_HOST=/cloudsql/example-419500:europe-west2:example \
	--set-secrets=DB_PASSWORD=projects/1024641440084/secrets/DB_PASSWORD:latest \
	--trigger-http \
	example

popd
