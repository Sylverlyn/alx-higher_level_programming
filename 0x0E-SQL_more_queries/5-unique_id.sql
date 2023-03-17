-- creates the table unique_id
-- asigns id a default number

CREATE TABLE
IF NOT EXITS unique_id(
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256) NOT NULL
  );
