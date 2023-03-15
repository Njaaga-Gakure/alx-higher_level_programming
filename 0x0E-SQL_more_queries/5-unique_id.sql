-- creates a table
-- id column of the table has a default value
-- the id must be unique
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
