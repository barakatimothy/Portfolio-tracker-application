// script.js

document.addEventListener('DOMContentLoaded', function() {
    // Function to handle user creation form submission
    document.getElementById('createUserForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        const formData = new FormData(this);
        const username = formData.get('username');

        createUser(username);
    });

    // Function to handle portfolio creation form submission
    document.getElementById('createPortfolioForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        const formData = new FormData(this);
        const userId = formData.get('userId');
        const portfolioName = formData.get('portfolioName');

        createPortfolio(userId, portfolioName);
    });

    // Function to handle asset creation form submission
    document.getElementById('createAssetForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        const formData = new FormData(this);
        const portfolioId = formData.get('portfolioId');
        const assetSymbol = formData.get('assetSymbol');
        const assetQuantity = formData.get('assetQuantity');

        createAsset(portfolioId, assetSymbol, assetQuantity);
    });
});

// Function to create a user
function createUser(username) {
    fetch('/create-user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username })
    })
    .then(response => {
        if (response.ok) {
            alert('User created successfully');
        } else {
            alert('Failed to create user');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to create a portfolio
function createPortfolio(userId, portfolioName) {
    fetch('/create-portfolio', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ userId: userId, name: portfolioName })
    })
    .then(response => {
        if (response.ok) {
            alert('Portfolio created successfully');
        } else {
            alert('Failed to create portfolio');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to create an asset
function createAsset(portfolioId, assetSymbol, assetQuantity) {
    fetch('/create-asset', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ portfolioId: portfolioId, symbol: assetSymbol, quantity: assetQuantity })
    })
    .then(response => {
        if (response.ok) {
            alert('Asset added successfully');
        } else {
            alert('Failed to add asset');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
