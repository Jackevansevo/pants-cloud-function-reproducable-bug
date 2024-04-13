# Reproduce bug

    pants package functions:cloud_function

```
ProcessExecutionFailure: Process 'Build python_google_cloud_function artifact for functions:cloud_function' failed with exit code 1.
stdout:

stderr:
Failed to resolve requirements from PEX environment @ /tmp/pants-sandbox-pyrYT1/faas_repository.pex.
Needed cp311-cp311-linux_x86_64 compatible dependencies for:
 1: greenlet!=0.4.17; platform_machine == "aarch64" or (platform_machine == "ppc64le" or (platform_machine == "x86_64" or (platform_machine == "amd64" or (platform_machine == "AMD64" or (platform_machine == "win32" or platform_machine == "WIN32")))))
    Required by:
      SQLAlchemy 2.0.29
    But this pex had no ProjectName(raw='greenlet', validated=False, normalized='greenlet') distributions.
```

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
