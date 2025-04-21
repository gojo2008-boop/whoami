from app import create_app  # Import the create_app function from app/__init__.py

app = create_app()  # Call the function to create the Flask app instance

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



