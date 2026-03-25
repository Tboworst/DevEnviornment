import click
from pathlib import Path


@click.command()
@click.argument('name')
@click.option("--db",default=None,help = "Includes the db setup")
@click.option("--backend",is_flag=True,help="Creates backend")
def create_app(name,db,backend):
    # create a Path object from name
    folder = Path(name)

    if folder.exists():
        click.echo(f" File:{name} alrady exisits")
        return
    # create the folder
    folder.mkdir()
    # create an empty main.py inside the folder
    #creating files inside of a folder, call folder name with / wand name of folder(these 2 are guaranteed in the file so hard coded)
    (folder/"main.py").write_text(
        f"""def main():
    print("Welcome to {name}!")

if __name__ == "__main__":
    main()
"""
    )

    (folder/"README.md").write_text(
        #This is the starter will update later 
        f"Created project that .."
    )
    click.echo(f"Created the file:{name} succesfully")
    
    if db == "go":
        pass


if __name__ == '__main__':
    create_app()



