import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
)
""")

cur.execute("DELETE FROM books")

books = [
    (1, "Data Science Basics", "Education", 1450, 8),
    (2, "Clean Code", "Programming", 1200, 6),
    (3, "The Silent Patient", "Fiction", 1350, 2),
    (4, "Python Basics", "Programming", 950, 10),
    (5, "Harry Potter", "Fiction", 1100, 3),
    (6, "Database Systems", "Education", 1600, 7),
    (7, "Atomic Habits", "Self Help", 900, 4),
    (8, "The Alchemist", "Fiction", 800, 6)
]

cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?)", books)

conn.commit()

# Query 1
print("Books above Rs.1000 (sorted):")
cur.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC
""")

for row in cur.fetchall():
    print(row)

# Query 2
print("\nBook titles using alias:")
cur.execute("""
SELECT title AS book_title
FROM books
""")

for row in cur.fetchall():
    print(row)

# Query 3
print("\nLow-stock Fiction books:")
cur.execute("""
SELECT title, genre, price, stock
FROM books
WHERE genre = 'Fiction' AND stock < 5
""")

for row in cur.fetchall():
    print(row)

conn.close()