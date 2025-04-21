from flask import Blueprint, render_template, request, redirect, url_for
from app.database import db, User, Product  # Import both User and Product models

main = Blueprint('main', __name__)

# Home route
@main.route('/')
def home():
    # Fetch all products from the database (from the 'product_db')
    products = Product.query.all()
    return render_template('home.html', products=products)

# About page route
@main.route('/about')
def about():
    return render_template('about.html')

# Explore page route
@main.route('/explore')
def explore():
    return render_template('explore.html')

# Contact page route
@main.route('/contact')
def contact():
    return render_template('contact.html')

# Collection page route
@main.route('/collection')
def collection():
    # Fetch all products from the database
    products = Product.query.all()  # This grabs all products from the Product table
    return render_template('collection.html', products=products)

# Product page route
@main.route('/product/<product_id>')
def product(product_id):
    # Fetch the product by its ID
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)  # Pass the product object to the template


# Register page route
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Check if the email is already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return 'Email already registered', 400

        # Create a new user entry
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.thank_you'))  # Redirect to a "Thank You" page after submission

    return render_template('register.html')  # Render the registration form

# Thank You page route
@main.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')  # Redirect to the thank-you page after registration













