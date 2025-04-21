from app import create_app
from app.database import db, User

app = create_app()

with app.app_context():
    # Query the users table
    users = User.query.all()

    # Print all users
    for user in users:
        print(f"Name: {user.name}, Email: {user.email}")
