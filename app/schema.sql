-- app/schema.sql

-- Table for storing product details
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    image_url TEXT NOT NULL,
    status TEXT DEFAULT 'Coming Soon'  -- You can later change this status to 'Available' when needed
);

-- Table for storing user registrations for product drop notifications
CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
