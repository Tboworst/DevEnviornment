from InquirerPy import inquirer
import click
from pathlib import Path
import languages
import databases



def create_app(name, backend):
    # Build the folder path from the project name the user gave
    backend = inquirer.select(
        message= "Select a backend language:",
        choices=["go","python","java","Typescript"]
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
        "PostGres": databases.generate_postgres,
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

    

    # Create the project folder
    folder.mkdir()

    # Write the generated code into a file with the correct extension
    (folder / f"main.{ext}").write_text(content)

    (folder / "README.md").write_text(
        f"# {name}\nCreated with  {backend}"
    )

    click.echo(f"Created project: {name} with {backend} backend")




if __name__ == '__main__':
    create_app()
