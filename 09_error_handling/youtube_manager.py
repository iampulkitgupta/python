

def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    while True:
        print("\n Youtube Manager | Choose a option ")
        print("1. List a youtube  videos ")
        print("2. Add a youtube  video ")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video ")
        print("5. Exit the app")    
        choice = input ("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos("videos")
            case '2':
                add_video("video")
            case '3':
                update_video("video")
            case '4':
                delete_video("video")
            case '5':
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

