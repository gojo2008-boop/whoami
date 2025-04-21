from flask import Flask
from app.database import init_db  # Import init_db to initialize the databases

def create_app():
    app = Flask(__name__)

    app.secret_key = 'superSecretSessionKeyChangeThis'  # Add this line


    # Set up configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # Main database for users
    app.config['SQLALCHEMY_BINDS'] = {
        'product_db': 'sqlite:///product_db.sqlite3'  # Second database for products
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database (this will create both the user and product tables)
    init_db(app)

    from app.routes import main
    app.register_blueprint(main)

    return app















