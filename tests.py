import pytest
from pathlib import Path
from unittest.mock import patch
from click.testing import CliRunner
from main import create_app


@pytest.fixture(autouse=True)
def cleanup(tmp_path, monkeypatch):
    # Run each test inside a temp directory so generated folders don't pollute the repo
    monkeypatch.chdir(tmp_path)


def run_app(project_name, backend, frontend, database):
    """
    Helper that runs create_app with mocked InquirerPy prompts.
    Instead of showing an interactive UI, the prompts just return the values we pass in.
    """
    runner = CliRunner()
    with patch("main.inquirer.select") as mock_select, \
         patch("main.inquirer.checkbox") as mock_checkbox:

        # select() is called twice: once for backend, once for frontend
        mock_select.return_value.execute.side_effect = [backend, frontend]
        # checkbox() is called once for database — returns a list
        mock_checkbox.return_value.execute.return_value = database

        return runner.invoke(create_app, [project_name])


def test_python_no_db_no_frontend():
    result = run_app("myapp", "python", "None", [])

    project = Path("myapp")
    assert project.exists(), result.output
    assert (project / "backend" / "main.py").exists()
    assert (project / "README.md").exists()
    assert (project / ".gitignore").exists()
    assert (project / "requirements.txt").exists()
    assert (project / "Dockerfile").exists()
    assert not (project / "db").exists()
    assert not (project / "frontend").exists()


def test_go_with_postgres():
    result = run_app("goapp", "go", "None", ["Postgres"])

    project = Path("goapp")
    assert project.exists(), result.output
    assert (project / "backend" / "main.go").exists()
    assert (project / "db" / "postgres.go").exists()
    assert (project / "go.mod").exists()
    assert (project / "Dockerfile").exists()


def test_duplicate_project_name():
    # Create it once
    run_app("dupapp", "python", "None", [])
    # Try to create it again — should fail gracefully
    result = run_app("dupapp", "python", "None", [])

    assert "already exists" in result.output


def test_typescript_with_react_frontend():
    result = run_app("tsapp", "ts", "React", [])

    project = Path("tsapp")
    assert project.exists(), result.output
    assert (project / "backend" / "main.ts").exists()
    assert (project / "frontend" / "App.jsx").exists()
    assert (project / "package.json").exists()
