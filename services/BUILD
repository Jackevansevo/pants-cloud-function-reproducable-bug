python_sources()

pex_binary(
    name="flask",
    entry_point="flask",
    args=["--app=services.app"],
    dependencies=[
        "./app.py",
        "//:reqs0#python-dotenv",
        "//:reqs0#flask-shell-ipython",
        "//:reqs0#pdbpp",
    ],
)

pex_binary(
    name="gunicorn",
    entry_point="gunicorn",
    args=["services.app:create_app()"],
    dependencies=["./app.py"],
    execution_mode="venv",
)


docker_image(
    name="app",
    instructions=[
        "FROM python:3.11.9-slim",
        "COPY services/gunicorn.pex /bin/app",
        "ENTRYPOINT app",
    ],
)
