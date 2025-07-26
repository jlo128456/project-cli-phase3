import click
from lib.db.models import Base, engine
from lib.db.seed import run_seed

def create_tables():
    reset = click.confirm("Reset existing tables?", default=True)
    seed = click.confirm("Seed with sample data?", default=False)

    if reset:
        click.echo("Dropping existing tables...")
        Base.metadata.drop_all(engine)
    
    click.echo("Creating tables...")
    Base.metadata.create_all(engine)

    if seed:
        run_seed()
        click.echo("Database seeded.")
    else:
        click.echo("Tables created without seeding.")

    click.prompt("\nPress Enter to return to the Main Menu", prompt_suffix='', default='', show_default=False)
