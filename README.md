# Create virtualenv

    rm -rf dist/export/python/virtualenvs && pants export --resolve=python-default

    source dist/export/python/virtualenvs/python-default/3*/bin/activate

# Start a local postgres DB

    docker run --rm -d --network host -e POSTGRES_PASSWORD=postgres postgres

# Connect to remote DB

Run cloud-sql-proxy on port 5431 (so it doens't conflict with any local postgres)

    cloud-sql-proxy example-419500:europe-west2:example --port 5431

    PGPASSWORD=$(gcloud secrets versions access 1 --secret=DB_PASSWORD) pgcli -u postgres -h localhost -p 5431 example

You can check whether the remote DB is up to date with:

    DB_PASSWORD=$(gcloud secrets versions access 1 --secret=DB_PASSWORD) DB_PORT=5431 pants run :flask -- db check
