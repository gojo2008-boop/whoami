from app import create_app
from app.database import db, Product

# Create the app and open a context
app = create_app()

with app.app_context():
    # Define all products
    products = [
        Product(
            name="Flame of Life Hoodie",
            description= "The Flame of Life Hoodie ignites your style with a design that symbolizes inner strength and the unyielding spirit to push forward. Its bold, fiery design and premium fabric promise comfort while reflecting the burning passion we all carry deep within.",
            image_filename="hoodie.png",
            price="Coming Soon"
        ),
        Product(
            name="Tree of Life Button-Up",
            description=" This button-up shirt brings the symbol of life’s continuity to the forefront with its detailed design, weaving a timeless connection between nature's intricate systems and modern style. The flowing tree branches capture both life’s fragility and its strength, making this piece not just clothing, but an artful statement.",
            image_filename="shirt.jpg",
            price="Coming Soon"
        ),
        Product(
            name="Deadly Sins Crewneck",
            description="The Deadly Sins Crewneck dives deep into the complexities of human nature, encapsulating the seven deadly sins with a twist of edgy, contemporary style. Wear it to reflect the darker side of existence, yet embrace the elegance in chaos.",
            image_filename="Crewneck1.png",
            price="Coming Soon"
        ),
        Product(
            name="Hate but Love More Crewneck",
            description="A paradox in fashion, the Hate but Love More Crewneck challenges perceptions of duality. This piece speaks to the power of love in the face of adversity, offering comfort, warmth, and a statement that love triumphs above all.",
            image_filename="CrFinal.png",
            price="Coming Soon"
        ),
        Product(
            name="All-Seeing Jorts",
            description=" The Allseeing Jorts represent a unique blend of boldness and introspection, offering a powerful statement about perception and self-awareness. With these jorts, every glance is a reminder of your ability to see beyond the surface and embrace deeper understanding.",
            image_filename="JortFinal.png",
            price="Coming Soon"
        ),
        Product(
            name="Puzzle Piece Trousers",
            description="The Puzzle Piece Trousers represent the complexity and interconnectedness of life, with each piece fitting together to form a harmonious whole. These trousers blend tailored elegance with a playful edge, making them an ideal choice for those who embrace individuality and cohesion.",
            image_filename="trousers.png",
            price="Coming Soon"
        ),
        Product(
            name="Hate but Love More Beanie",
            description="The Hate but Love More Beanie is a symbol of resilience, warmth, and love. A cozy piece that offers both comfort and style, it encourages us to love more in a world that can sometimes be filled with hate, all while keeping you effortlessly fashionable.",
            image_filename="Beanie.png",
            price="Coming Soon"
        )
    ]

    # Add all products to the session
    db.session.add_all(products)

    # Commit the changes to the database
    db.session.commit()

    print("Products added!")
