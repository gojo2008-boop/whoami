from app import create_app
from app.database import db, Product

# Create the app and open an application context
app = create_app()

with app.app_context():
    # Delete all records in the Product table
    db.session.query(Product).delete()

    # Commit the changes to the database
    db.session.commit()

    print("All products have been deleted!")

