"""
MongoDB Connection Setup Helper
This script helps you configure your MongoDB connection
"""

import pymongo
from bson.objectid import ObjectId

def test_connection(connection_string):
    """Test if MongoDB connection works"""
    try:
        client = pymongo.MongoClient(
            connection_string,
            tlsAllowInvalidCertificates=True,
            serverSelectionTimeoutMS=5000
        )

        # Test connection
        client.admin.command('ping')
        print("✓ Connection successful!")

        # Get database info
        db = client["ytmanager"]
        collection = db["videos"]
        count = collection.count_documents({})

        print(f"✓ Database: ytmanager")
        print(f"✓ Collection: videos")
        print(f"✓ Current video count: {count}")

        return True

    except Exception as e:
        print(f"✗ Connection failed: {e}")
        return False

def add_sample_data(connection_string):
    """Add sample videos for testing"""
    try:
        client = pymongo.MongoClient(
            connection_string,
            tlsAllowInvalidCertificates=True,
            serverSelectionTimeoutMS=5000
        )

        db = client["ytmanager"]
        collection = db["videos"]

        sample_videos = [
            {"name": "Python Basics Tutorial", "time": "15:30"},
            {"name": "MongoDB CRUD Operations", "time": "22:45"},
            {"name": "Building REST APIs", "time": "35:20"}
        ]

        result = collection.insert_many(sample_videos)
        print(f"✓ Added {len(result.inserted_ids)} sample videos!")

        for idx, video in enumerate(sample_videos, 1):
            print(f"  {idx}. {video['name']} - {video['time']}")

        return True

    except Exception as e:
        print(f"✗ Error adding sample data: {e}")
        return False

def main():
    print("=" * 60)
    print("MongoDB Connection Setup Helper")
    print("=" * 60)

    print("\n1. Get your MongoDB connection string from:")
    print("   https://cloud.mongodb.com/")
    print("   → Your Cluster → Connect → Connect your application")
    print("\n2. Format should be:")
    print("   mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/")

    print("\n" + "=" * 60)
    connection_string = input("Enter your MongoDB connection string: ").strip()

    if not connection_string.startswith("mongodb"):
        print("✗ Invalid connection string. Must start with 'mongodb://' or 'mongodb+srv://'")
        return

    print("\n" + "=" * 60)
    print("Testing connection...")
    print("=" * 60)

    if test_connection(connection_string):
        print("\n" + "=" * 60)
        add_sample = input("Do you want to add sample videos? (y/n): ").strip().lower()

        if add_sample == 'y':
            print("\nAdding sample data...")
            add_sample_data(connection_string)

        print("\n" + "=" * 60)
        print("✓ Setup complete!")
        print("\nNext steps:")
        print("1. Open youtube_manager_mongodb.py")
        print("2. Replace line 10 with your connection string:")
        print(f'   "{connection_string}",')
        print("3. Run: python youtube_manager_mongodb.py")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("Setup failed. Please check:")
        print("1. Your internet connection")
        print("2. Username and password are correct")
        print("3. Your IP is whitelisted in MongoDB Atlas")
        print("   (Network Access → Add IP Address → Allow from Anywhere)")
        print("=" * 60)

if __name__ == "__main__":
    main()
