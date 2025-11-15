import sqlite3
import os

# Remove old database if it exists to start fresh
if os.path.exists('youtube.db'):
    os.remove('youtube.db')
    print("Removed old database file")

conn = sqlite3.connect('youtube.db')
cursor = conn.cursor()

# Create table with AUTOINCREMENT
cursor.execute('''
    CREATE TABLE IF NOT EXISTS xx_youtube_table(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

# Add test data
test_videos = [
    ("Python Tutorial", "10:30"),
    ("Django Basics", "15:45"),
    ("SQLite Database", "08:20"),
    ("Web Development", "12:00")
]

print("\nAdding test videos...")
for name, time in test_videos:
    cursor.execute("INSERT INTO xx_youtube_table (name, time) VALUES (?, ?)", (name, time))
    print(f"Added: {name} - {time}")

conn.commit()

# Verify the data
print("\n" + "="*50)
print("All videos in database:")
print("="*50)
cursor.execute("SELECT * FROM xx_youtube_table")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Time: {row[2]}")

conn.close()
print("\n✓ Test completed successfully!")
