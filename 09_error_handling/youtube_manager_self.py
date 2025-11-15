
import json

def load_data():
    try:
        with open('youtube_file.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(videos):
    with open('youtube_file.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")


def add_video(video):
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    video.append({'name': name, 'time': time})    
    save_data(video)

def update_video(video):
    list_all_videos(video)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(video):
        name = input("Enter the video name: ")
        time = input("Enter the video time: ")
        video[index-1] = {'name': name, 'time': time}
        save_data(video)
    else:
        print("Invalid video number")



def delete_video(video):
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(video):
        del video[index-1]
        save_data(video)
    else:
        print("Invalid video number")


def main():
    videos = load_data()
    while True:        
        # print(videos)
        print("\n Youtube Manager | Choose an option ")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter the choice: ")        

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Option. Please try again.")

if __name__ == "__main__":
    main()