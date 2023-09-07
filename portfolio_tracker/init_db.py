from database import init_db

if __name__ == '__main__':
    db_uri = "sqlite:///portfolio.db"  
    init_db(db_uri)
    print("Database initialized.")
