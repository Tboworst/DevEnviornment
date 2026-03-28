from InquirerPy import inquirer
import click
from pathlib import Path
import languages
import databases
import others
import dockergeneration

@click.command()
@click.argument("name")
def create_app(name):
    # Build the folder path from the project name the user gave
    backend = inquirer.select(
        message="Select a backend language:",
        choices=["go", "python", "java", "ts"]
    ).execute()

    frontend = inquirer.select(
        message="Select a frontend framework (or None to skip):",
        choices=["None", "React", "Vue", "Svelte", "HTML"]
    ).execute()
    
    database = inquirer.checkbox(
        message= "Select your database:",
        choices= ["Postgres","Sqlite"]
    ).execute()

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

    databas = {
        "Postgres": databases.generate_postgres,
        "Sqlite" : databases.generate_Sqlite
    }

    # checks if the users input has an actuall backend in the map if not returns
    if backend not in generators:
        click.echo(f"Unknown backend: {backend}. Choose from: go, java, ts, python")
        return

    # Call the matching generator function to get the file content as a string,\
    #must put parantheses at the end b/c when using map we cannot put function so the paranthese allows whats called to bea function u 
    content = generators[backend]()

    # Map each language to its correct file extension
    extensions = {
        "go": "go",
        "java": "java",
        "ts": "ts",
        "python": "py",
    }
    #saved insde a varaible so that it can be used in the f string 
    ext = extensions[backend]

    

    # Map each language to its gitignore generator
    gitignores = {
        "go": others.generate_gitignore_go,
        "java": others.generate_gitignore_java,
        "ts": others.generate_gitignore_ts,
        "python": others.generate_gitignore_python,
    }

    # Map each language to its dependencies file generator
    deps_generators = {
        "go": others.generate_deps_go,
        "java": others.generate_deps_java,
        "ts": others.generate_deps_ts,
        "python": others.generate_deps_python,
    }

    # Map each language to its Dockerfile generator — now using dockergeneration.py
    dockerfiles = {
        "go": dockergeneration.generate_dockerfile_go,
        "java": dockergeneration.generate_dockerfile_java,
        "ts": dockergeneration.generate_dockerfile_ts,
        "python": dockergeneration.generate_dockerfile_python,
    }

    # Map each language to its dependencies filename
    deps_filenames = {
        "go": "go.mod",
        "java": "pom.xml",
        "ts": "package.json",
        "python": "requirements.txt",
    }

    # Maps each frontend choice to its generator function and output filename
    frontends = {
        "React":  (others.generate_react,  "App.jsx"),
        "Vue":    (others.generate_vue,    "App.vue"),
        "Svelte": (others.generate_svelte, "App.svelte"),
        "HTML":   (others.generate_html,   "index.html"),
    }

    # Create the project folder and subfolders
    folder.mkdir()
    backend_folder = folder / "backend"
    backend_folder.mkdir()

    # Write the main backend file inside backend/
    (backend_folder / f"main.{ext}").write_text(content)

    # Write database files inside db/ — only create the folder if a db was selected
    if database:
        db_folder = folder / "db"
        db_folder.mkdir()
        for db in database:
            db_content = databas[db]()
            (db_folder / f"{db.lower()}.{ext}").write_text(db_content)

    # Write the README with project details
    (folder / "README.md").write_text(others.generate_readme(name, backend, ext, database))

    # Write the .gitignore for the selected language
    (folder / ".gitignore").write_text(gitignores[backend]())

    # Write the dependencies file — pass name so module/package name matches the project
    deps_file = deps_filenames[backend]
    (folder / deps_file).write_text(deps_generators[backend](name))

    # Write the Dockerfile — pass name so the binary/jar name matches the project
    (folder / "Dockerfile").write_text(dockerfiles[backend](name))

    # If the user picked a frontend, create a frontend/ subfolder and write the file
    if frontend != "None":
        frontend_folder = folder / "frontend"
        frontend_folder.mkdir()
        generator_fn, filename = frontends[frontend]
        (frontend_folder / filename).write_text(generator_fn())

    # Print a summary of everything that was created
    summary_lines = [
        f"  backend/main.{ext}",
    ]
    if database:
        for db in database:
            summary_lines.append(f"  db/{db.lower()}.{ext}")
    if frontend != "None":
        _, filename = frontends[frontend]
        summary_lines.append(f"  frontend/{filename}")
    summary_lines += [
        "  README.md",
        "  .gitignore",
        f"  {deps_file}",
        "  Dockerfile",
    ]

    click.echo(f"\nCreated: {name}/")
    for line in summary_lines:
        click.echo(line)




if __name__ == '__main__':
    create_app()
