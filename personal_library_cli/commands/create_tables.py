import click
from lib.db.models import engine, Base
from lib.db.seed import run_seed

@click.command("create-tables", help="Create tables, optionally resetting and seeding the DB.")
@click.option("--reset/--no-reset", default=True, help="Drop existing tables before creating new ones.")
@click.option("--seed", is_flag=True, help="Also populate the tables with sample data.")
def create_tables(reset, seed):
    if reset:
        click.echo("Dropping all existing tables...", err=True)
        Base.metadata.drop_all(engine)
    else:
        click.echo("Skipping drop (keeping existing tables)...")

    click.echo("Creating tables...")
    Base.metadata.create_all(engine)

    if seed:
        click.echo("Seeding initial data...")
        run_seed()
        click.echo("Database seeded successfully.")
    else:
        click.echo("Tables created (no seed).")
