import click
from pathlib import Path
import languages

@click.command()
@click.argument('name')
# --backend takes a value like "go", "java", "ts", "python" — default is python
@click.option("--backend", default="python", help="Language for the backend: go, java, ts, python")
def create_app(name, backend):
    # Build the folder path from the project name the user gave
    folder = Path(name)

    if folder.exists():
        click.echo(f"File: {name} already exists")
        return

    # Uses a map each language name to its generator function in languages.py
    generators = {
        "go": languages.generate_go,
        "java": languages.generate_java,
        "ts": languages.generate_typescript,
        "python": languages.generate_python,
    }

    # checks if the users input has an actuall backend in the map if not returns
    if backend not in generators:
        click.echo(f"Unknown backend: {backend}. Choose from: go, java, ts, python")
        return

    # Call the matching generator function to get the file content as a string
    content = generators[backend]()

    # Map each language to its correct file extension
    extensions = {
        "go": "go",
        "java": "java",
        "ts": "ts",
        "python": "py",
    }
    ext = extensions[backend]

    # Create the project folder
    folder.mkdir()

    # Write the generated code into a file with the correct extension
    (folder / f"main.{ext}").write_text(content)

    (folder / "README.md").write_text(
        f"# {name}\nCreated with --backend {backend}"
    )

    click.echo(f"Created project: {name} with {backend} backend")

if __name__ == '__main__':
    create_app()
