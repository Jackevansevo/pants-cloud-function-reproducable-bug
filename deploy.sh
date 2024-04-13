#/bin/bash
set -eou pipefail

echo "Building"
time pants package services:app
docker tag app europe-west2-docker.pkg.dev/example-419500/images/app
time docker push europe-west2-docker.pkg.dev/example-419500/images/app

echo "Running migrations"
cloud-sql-proxy example-419500:europe-west2:example --port 5431 &
PROXY_PID=$!
time DB_PASSWORD=$(gcloud secrets versions access 1 --secret=DB_PASSWORD) DB_PORT=5431 pants run services:flask -- db upgrade

echo "Deploying"
time gcloud run deploy \
	--image=europe-west2-docker.pkg.dev/example-419500/images/app \
	--set-cloudsql-instances=example-419500:europe-west2:example \
	--set-env-vars=DB_HOST=/cloudsql/example-419500:europe-west2:example \
	--set-secrets=DB_PASSWORD=projects/1024641440084/secrets/DB_PASSWORD:latest \
	app

kill $PROXY_PID
