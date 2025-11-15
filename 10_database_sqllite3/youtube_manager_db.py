import sqlite3

conn = sqlite3.connect('youtube.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS xx_youtube_table(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM xx_youtube_table")
    videos = cursor.fetchall()
    if not videos:
        print("No videos found.")
    else:
        print("List of all videos:")
        for video in videos:
            print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}")
    
def add_video():
    name = input("Enter video name: ")
    time = input("Enter video time: ")    
    cursor.execute("INSERT INTO xx_youtube_table (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("Video added successfully!")

def update_video():
    list_all_videos()
    video_id = input("Enter video ID to update: ")
    new_name = input("Enter new video name: ")
    new_time = input("Enter new video time: ")
    cursor.execute("UPDATE xx_youtube_table SET name=?, time=? WHERE id=?", (new_name, new_time, video_id))
    conn.commit()
    print("Video updated successfully!")
    
def delete_video():
    list_all_videos()
    video_id = input("Enter video ID to delete: ")
    cursor.execute("DELETE FROM xx_youtube_table WHERE id=?", (video_id,))
    conn.commit()
    print("Video deleted successfully!")

def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("1. List All Videos ")
        print("2. Add Videos ")
        print("3. Update Videos ")
        print("4. Delete Videos ")
        print("5. Exit")
        choice = input("Enter your choice: ")        

        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("Invalid choice. Please try again.")
    conn.close()

if __name__ == '__main__':
    main()