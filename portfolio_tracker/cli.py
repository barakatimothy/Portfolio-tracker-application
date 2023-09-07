import argparse
from database import init_db
from models import User, Portfolio, Asset

# Create a global database session
db_session = init_db('sqlite:///portfolio.db')

def create_user(args):
    """Create a new user."""
    username = args.username
    db_uri = args.db_uri

    session = init_db(db_uri)

    # Data Validation: Validate the username
    if not username:
        print("Error: Username cannot be empty.")
        return  # Exit the command

    # Check if the username already exists
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print(f"Error: Username '{username}' already exists.")
        return  # Exit the command

    # Confirmation Prompt: Ask the user for confirmation
    confirmation = input(f'Create user "{username}"? (yes/no): ')
    if confirmation.lower() != 'yes':
        print("User creation canceled.")
        return  # Exit the command

    # Create the user
    user = User(username=username)
    session.add(user)
    session.commit()
    print(f'User "{username}" created.')
    
# Define the function to create a new portfolio
def create_portfolio(args):
    user_id = args.user_id
    name = args.name
    db_uri = args.db_uri

    session = init_db(db_uri)

    # Data Validation: Validate user_id and name
    if not name:
        print("Error: Portfolio name cannot be empty.")
        return  # Exit the command

    # Check if the user exists
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print(f"Error: User with ID {user_id} does not exist.")
        return  # Exit the command

    # Confirmation Prompt: Ask the user for confirmation
    confirmation = input(f'Create portfolio "{name}" for user ID {user_id}? (yes/no): ')
    if confirmation.lower() != 'yes':
        print("Portfolio creation canceled.")
        return  # Exit the command

    # Create the portfolio
    portfolio = Portfolio(user_id=user_id, name=name)
    session.add(portfolio)
    session.commit()
    print(f'Portfolio "{name}" created for user ID {user_id}.')
    
    
# Define the function to create a new asset
def create_asset(args):
    portfolio_id = args.portfolio_id
    symbol = args.symbol
    quantity = args.quantity
    db_uri = args.db_uri

    session = init_db(db_uri)

    # Data Validation: Validate portfolio_id, symbol, and quantity
    if not symbol:
        print("Error: Asset symbol cannot be empty.")
        return  # Exit the command

    if quantity <= 0:
        print("Error: Quantity must be greater than zero.")
        return  # Exit the command

    # Check if the portfolio exists
    portfolio = session.query(Portfolio).filter_by(id=portfolio_id).first()
    if not portfolio:
        print(f"Error: Portfolio with ID {portfolio_id} does not exist.")
        return  # Exit the command

    # Confirmation Prompt: Ask the user for confirmation
    confirmation = input(f'Add asset "{symbol}" to portfolio ID {portfolio_id}? (yes/no): ')
    if confirmation.lower() != 'yes':
        print("Asset creation canceled.")
        return  # Exit the command

    # Create the asset
    asset = Asset(portfolio_id=portfolio_id, symbol=symbol, quantity=quantity)
    session.add(asset)
    session.commit()
    print(f'Asset "{symbol}" added to portfolio ID {portfolio_id}.')

def main():
    parser = argparse.ArgumentParser(description="Portfolio Tracker CLI")
    subparsers = parser.add_subparsers()

    # Create subparser for the 'create-user' command
    create_user_parser = subparsers.add_parser("create-user")
    create_user_parser.add_argument("username", type=str, help="Username")
    create_user_parser.add_argument("--db-uri", type=str, default="sqlite:///portfolio.db", help="Database URI")
    create_user_parser.set_defaults(func=create_user)

    # Create subparser for the 'create-portfolio' command
    create_portfolio_parser = subparsers.add_parser("create-portfolio")
    create_portfolio_parser.add_argument("user_id", type=int, help="User ID")
    create_portfolio_parser.add_argument("name", type=str, help="Portfolio Name")
    create_portfolio_parser.add_argument("--db-uri", type=str, default="sqlite:///portfolio.db", help="Database URI")
    create_portfolio_parser.set_defaults(func=create_portfolio)

    # Create subparser for the 'create-asset' command
    create_asset_parser = subparsers.add_parser("create-asset")
    create_asset_parser.add_argument("portfolio_id", type=int, help="Portfolio ID")
    create_asset_parser.add_argument("symbol", type=str, help="Asset Symbol")
    create_asset_parser.add_argument("quantity", type=int, help="Asset Quantity")
    create_asset_parser.add_argument("--db-uri", type=str, default="sqlite:///portfolio.db", help="Database URI")
    create_asset_parser.set_defaults(func=create_asset)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)


if __name__ == "__main__":
    main()










