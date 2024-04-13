python_sources()

python_google_cloud_function(
    name="cloud_function",
    runtime="python311",
    handler="main.py:handler",
    type="http",
)

pex_binary(
    name="function",
    entry_point="functions_framework",
    args=["--source=functions/main.py", "--target=handler", "--debug"],
    dependencies=[
        "./main.py",
        "//:reqs0#python-dotenv",
        "//:reqs0#pdbpp",
    ],
)

pex_binary(
    name="gcf",
    entry_point="main.py",
    layout="loose",
)
