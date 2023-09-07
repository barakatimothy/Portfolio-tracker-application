# Portfolio Tracker CLI

The Portfolio Tracker CLI is a Python command-line application that allows you to manage your investment portfolios and assets. You can create users, portfolios, and assets, making it easy to keep track of your financial holdings.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use the Portfolio Tracker CLI, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone git@github.com:barakatimothy/Portfolio-tracker-application.git
   cd your-repo
   ```


## Usage
The Portfolio Tracker CLI provides several commands for managing users, portfolios, and assets. You can view available commands and their options using the --help option:

 ```bash
   python3 portfolio_tracker/cli.py --help
 ```
To get help on a specific command, run:

 ```bash
   python3 portfolio_tracker/cli.py command-name --help
   ```
## Commands
create-user: Create a new user.
create-portfolio: Create a new portfolio for an existing user.
create-asset: Create a new asset and add it to an existing portfolio.
list-users: List all users.
list-portfolios: List all portfolios.
list-assets: List all assets.
update-portfolio: Update an existing portfolio's name.
update-asset: Update an existing asset's symbol or quantity.
delete-portfolio: Delete an existing portfolio and its associated assets.
delete-asset: Delete an existing asset.

Examples
Here are some examples of how to use the Portfolio Tracker CLI:

Create a new user:

 ```bash
    python3 portfolio_tracker/cli.py create-user "john_doe"
 ```
Create a new portfolio:

 ```bash
    python3 portfolio_tracker/cli.py create-portfolio 1 "My Portfolio"
 ```
Create a new asset:

 ```bash
    python3 portfolio_tracker/cli.py create-asset 1 "AAPL" 10
 ```
List all portfolios:

 ```bash
    python3 portfolio_tracker/cli.py list-portfolios
 ```
Update a portfolio name:

 ```bash
   python3 portfolio_tracker/cli.py update-portfolio 1 "Updated Portfolio Name"
 ```
## Troubleshooting
If you encounter any issues or errors while using the CLI, please check the Troubleshooting section in this README for possible solutions.

## Contributing
If you would like to contribute to this project, please follow the guidelines in CONTRIBUTING.md.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



