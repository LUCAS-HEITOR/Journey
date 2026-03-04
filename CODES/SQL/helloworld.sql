-- Hello World in SQL
-- This is a simple SQL demonstration

-- Select a simple message
SELECT 'Hello, World!' AS greeting;

-- Create a simple table
CREATE TABLE IF NOT EXISTS hello_world (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert a hello world message
INSERT INTO hello_world (message) VALUES ('Hello, World!');

-- Display all messages
SELECT * FROM hello_world;

-- Drop the table (uncomment to use)
-- DROP TABLE hello_world;

--PlaceHolder -- AI