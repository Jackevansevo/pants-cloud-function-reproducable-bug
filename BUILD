python_requirement(
    name="setuptools",
    requirements=["setuptools"],
)

python_requirements(
    name="reqs0",
    source="pyproject.toml",
    overrides={
        "sqlalchemy": {"dependencies": [":reqs0#psycopg"]},
	"functions_framework": {"dependencies": [":setuptools"]}
    },
)
