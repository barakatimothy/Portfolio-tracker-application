# portfolio_tracker/cli.py
import click
from portfolio_tracker.database import init_db
from portfolio_tracker.models import User, Portfolio, Asset

@click.group()
def cli():
    pass

@cli.command()
@click.option('--db-uri', default='sqlite:///portfolio.db', help='Database URI')
def init_db(db_uri):
    """Initialize the database."""
    init_db(db_uri)
    click.echo('Database initialized.')


# Create a new user
@cli.command()
@click.argument('username')
@click.option('--db-uri', default='sqlite:///portfolio.db', help='Database URI')
def create_user(username, db_uri):
    """Create a new user."""
    session = init_db(db_uri)

    # Data Validation: Validate the username
    if not username:
        click.echo("Error: Username cannot be empty.")
        return  # Exit the command

    # Check if the username already exists
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        click.echo(f"Error: Username '{username}' already exists.")
        return  # Exit the command

    # Confirmation Prompt: Ask the user for confirmation
    confirmation = click.confirm(f'Create user "{username}"?')
    if not confirmation:
        click.echo("User creation canceled.")
        return  # Exit the command

    # Create the user
    user = User(username=username)
    session.add(user)
    session.commit()
    click.echo(f'User "{username}" created.')



    
# Create a new portfolio
@cli.command()
@click.argument('user_id', type=int)
@click.argument('name')
@click.option('--db-uri', default='sqlite:///portfolio.db', help='Database URI')
def create_portfolio(user_id, name, db_uri):
    """Create a new portfolio."""
    session = init_db(db_uri)

    # Data Validation: Validate user_id and name
    if not name:
        click.echo("Error: Portfolio name cannot be empty.")
        return  # Exit the command

    # Check if the user exists
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        click.echo(f"Error: User with ID {user_id} does not exist.")
        return  # Exit the command

    # Confirmation Prompt: Ask the user for confirmation
    confirmation = click.confirm(f'Create portfolio "{name}" for user ID {user_id}?')
    if not confirmation:
        click.echo("Portfolio creation canceled.")
        return  # Exit the command

    # Create the portfolio
    portfolio = Portfolio(user_id=user_id, name=name)
    session.add(portfolio)
    session.commit()
    click.echo(f'Portfolio "{name}" created for user ID {user_id}.')




# Create a new asset
@cli.command()
@click.argument('portfolio_id', type=int)
@click.argument('symbol')
@click.argument('quantity', type=int)
@click.option('--db-uri', default='sqlite:///portfolio.db', help='Database URI')
def create_asset(portfolio_id, symbol, quantity, db_uri):
    """Create a new asset."""
    session = init_db(db_uri)

    # Data Validation: Validate portfolio_id, symbol, and quantity
    if not symbol:
        click.echo("Error: Asset symbol cannot be empty.")
        return  # Exit the command

    if quantity <= 0:
        click.echo("Error: Quantity must be greater than zero.")
        return  # Exit the command

    # Check if the portfolio exists
    portfolio = session.query(Portfolio).filter_by(id=portfolio_id).first()
    if not portfolio:
        click.echo(f"Error: Portfolio with ID {portfolio_id} does not exist.")
        return  # Exit the command

    # Confirmation Prompt: Ask the user for confirmation
    confirmation = click.confirm(f'Add asset "{symbol}" to portfolio ID {portfolio_id}?')
    if not confirmation:
        click.echo("Asset creation canceled.")
        return  # Exit the command

    # Create the asset
    asset = Asset(portfolio_id=portfolio_id, symbol=symbol, quantity=quantity)
    session.add(asset)
    session.commit()
    click.echo(f'Asset "{symbol}" added to portfolio ID {portfolio_id}.')



if __name__ == '__main__':
    cli()
