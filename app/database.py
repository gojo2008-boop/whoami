from flask_sqlalchemy import SQLAlchemy

# Initialize the db object
db = SQLAlchemy()

# User Model (for registration)
class User(db.Model):
    __tablename__ = 'users'  # Table name for the user database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}, {self.email}>'

# Product Model (for products)
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    image_filename = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}, ${self.price}>'


# Initialize the db (this will set up both databases)
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Creates all tables (both user and product tables)







