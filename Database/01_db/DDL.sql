CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);

ALTER TABLE contacts RENAME TO new_contacts;

ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;

ALTER TABLE new_contacts DROP COLUMN address;

DROP TABLE new_contacts;