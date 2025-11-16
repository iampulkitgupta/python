import pymongo
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure, OperationFailure

# MongoDB connection with proper error handling
try:
    connection_string = "mongodb+srv://pulkitnoida_db_user:IBBsPQkxYK6hR16i@cluster0.rqo1tzu.mongodb.net/?appName=Cluster0"

    client = pymongo.MongoClient(
        connection_string,
        tlsAllowInvalidCertificates=True,
        serverSelectionTimeoutMS=10000
    )

    # Test the connection
    client.admin.command('ping')
    print("✓ Successfully connected to MongoDB!")

    db = client["ytmanager"]
    collection = db["videos"]

except ConnectionFailure as e:
    print(f"\n✗ Failed to connect to MongoDB")
    print(f"Error message: {e}")
    print("\nPossible issues:")
    print("1. Check your MongoDB Atlas connection string")
    print("2. Verify username and password are correct")
    print("3. Check if your IP address is whitelisted in MongoDB Atlas")
    print("4. Verify network connectivity")
    exit(1)
except OperationFailure as e:
    print(f"\n✗ MongoDB operation failed")
    print(f"Error message: {e}")
    print("\nPossible issues:")
    print("1. Authentication failed - check username/password")
    print("2. Insufficient permissions")
    exit(1)
except Exception as e:
    print(f"\n✗ Unexpected error occurred")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
    exit(1)

def list_all_videos():
    try:
        videos = list(collection.find())

        if not videos:
            print("\n📋 No videos found in the database.")
            return []

        print("\n" + "="*60)
        print("📹 VIDEO LIST")
        print("="*60)
        for idx, video in enumerate(videos, 1):
            print(f"\n{idx}. ID: {video['_id']}")
            print(f"   Name: {video.get('name', 'N/A')}")
            print(f"   Time: {video.get('time', 'N/A')}")
        print("="*60)
        return videos
    except Exception as e:
        print(f"✗ Error listing videos: {e}")
        return []

def add_video(name, time):
    try:
        if not name or not time:
            print("✗ Error: Name and time cannot be empty.")
            return False

        video = {"name": name, "time": time}
        result = collection.insert_one(video)
        print(f"✓ Video added successfully! ID: {result.inserted_id}")
        return True
    except Exception as e:
        print(f"✗ Error adding video: {e}")
        return False

def update_video(video_id, name, time):
    try:
        # Convert string ID to ObjectId
        try:
            obj_id = ObjectId(video_id)
        except Exception as e:
            print(f"✗ Invalid video ID format: {video_id}")
            return False

        if not name or not time:
            print("✗ Error: Name and time cannot be empty.")
            return False

        result = collection.update_one(
            {"_id": obj_id},
            {"$set": {"name": name, "time": time}}
        )

        if result.matched_count == 0:
            print(f"✗ No video found with ID: {video_id}")
            return False
        else:
            print(f"✓ Video updated successfully!")
            return True
    except Exception as e:
        print(f"✗ Error updating video: {e}")
        return False

def delete_video(video_id):
    try:
        # Convert string ID to ObjectId
        try:
            obj_id = ObjectId(video_id)
        except Exception as e:
            print(f"✗ Invalid video ID format: {video_id}")
            return False

        result = collection.delete_one({"_id": obj_id})

        if result.deleted_count == 0:
            print(f"✗ No video found with ID: {video_id}")
            return False
        else:
            print(f"✓ Video deleted successfully!")
            return True
    except Exception as e:
        print(f"✗ Error deleting video: {e}")
        return False

def main():
    while True:
        print("\n" + "="*60)
        print("📺 YOUTUBE MANAGER APP")
        print("="*60)
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        print("="*60)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            list_all_videos()

        elif choice == "2":
            name = input("Enter video name: ").strip()
            time = input("Enter video time (e.g., 10:30): ").strip()
            add_video(name, time)

        elif choice == "3":
            videos = list_all_videos()
            if videos:
                video_id = input("\nEnter the video ID to update: ").strip()
                name = input("Enter new video name: ").strip()
                time = input("Enter new video time: ").strip()
                update_video(video_id, name, time)

        elif choice == "4":
            videos = list_all_videos()
            if videos:
                video_id = input("\nEnter the video ID to delete: ").strip()
                confirm = input(f"Are you sure you want to delete video {video_id}? (y/n): ").strip().lower()
                if confirm == 'y':
                    delete_video(video_id)
                else:
                    print("✗ Deletion cancelled.")

        elif choice == "5":
            print("\n👋 Thank you for using YouTube Manager! Goodbye!")
            break

        else:
            print("✗ Invalid choice. Please enter a number between 1 and 5.")



if __name__ == "__main__":
    main()