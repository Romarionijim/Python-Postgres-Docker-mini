CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    product_name VARCHAR(100) NOT NULL,
    order_date DATE
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

INSERT INTO users (username, email) VALUES
    ('user1', 'user1@example.com'),
    ('user2', 'user2@example.com');

INSERT INTO orders (user_id, product_name, order_date) VALUES
    (1, 'Product A', '2023-01-01'),
    (2, 'Product B', '2023-01-02');

INSERT INTO products (product_name, price) VALUES
    ('Product A', 19.99),
    ('Product B', 29.99);