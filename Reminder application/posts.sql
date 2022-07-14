DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    info TEXT
);

INSERT INTO posts (title, info) VALUES (
    'Wash the car',
    'Also wash the inside of the machine!'
);
INSERT INTO posts (title, info) VALUES (
    'Go to the supermarket',
    'Remember to buy detergent!'
);
INSERT INTO posts (title, info) VALUES (
    'Make dinner for your parents',
    'Do the cleaning too'
);