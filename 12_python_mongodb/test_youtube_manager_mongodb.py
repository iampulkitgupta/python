import pytest
from unittest.mock import MagicMock, patch, call
from bson.objectid import ObjectId
import youtube_manager_mongodb as yt_manager


@pytest.fixture
def mock_collection():
    """Fixture to create a mock MongoDB collection"""
    with patch('youtube_manager_mongodb.collection') as mock_coll:
        yield mock_coll


@pytest.fixture
def sample_videos():
    """Fixture with sample video data"""
    return [
        {"_id": ObjectId("507f1f77bcf86cd799439011"), "name": "Python Tutorial", "time": "10:30"},
        {"_id": ObjectId("507f1f77bcf86cd799439012"), "name": "MongoDB Basics", "time": "15:45"},
        {"_id": ObjectId("507f1f77bcf86cd799439013"), "name": "Testing Guide", "time": "20:00"}
    ]


class TestListAllVideos:
    """Test cases for list_all_videos function"""

    def test_list_empty_videos(self, mock_collection, capsys):
        """Test listing videos when database is empty"""
        mock_collection.find.return_value = []

        yt_manager.list_all_videos()

        mock_collection.find.assert_called_once()
        captured = capsys.readouterr()
        assert captured.out == ""

    def test_list_single_video(self, mock_collection, sample_videos, capsys):
        """Test listing a single video"""
        mock_collection.find.return_value = [sample_videos[0]]

        yt_manager.list_all_videos()

        mock_collection.find.assert_called_once()
        captured = capsys.readouterr()
        assert "Python Tutorial" in captured.out
        assert "10:30" in captured.out

    def test_list_multiple_videos(self, mock_collection, sample_videos, capsys):
        """Test listing multiple videos"""
        mock_collection.find.return_value = sample_videos

        yt_manager.list_all_videos()

        mock_collection.find.assert_called_once()
        captured = capsys.readouterr()
        assert "Python Tutorial" in captured.out
        assert "MongoDB Basics" in captured.out
        assert "Testing Guide" in captured.out


class TestAddVideo:
    """Test cases for add_video function"""

    def test_add_video_success(self, mock_collection):
        """Test successfully adding a video"""
        name = "New Python Course"
        time = "25:30"

        yt_manager.add_video(name, time)

        mock_collection.insert_one.assert_called_once()
        call_args = mock_collection.insert_one.call_args[0][0]
        assert call_args["name"] == name
        assert call_args["time"] == time

    def test_add_video_with_special_characters(self, mock_collection):
        """Test adding video with special characters in name"""
        name = "C++ & Python: Advanced #1"
        time = "30:15"

        yt_manager.add_video(name, time)

        mock_collection.insert_one.assert_called_once()
        call_args = mock_collection.insert_one.call_args[0][0]
        assert call_args["name"] == name
        assert call_args["time"] == time

    def test_add_video_with_empty_name(self, mock_collection):
        """Test adding video with empty name"""
        name = ""
        time = "10:00"

        yt_manager.add_video(name, time)

        mock_collection.insert_one.assert_called_once()
        call_args = mock_collection.insert_one.call_args[0][0]
        assert call_args["name"] == ""
        assert call_args["time"] == time

    def test_add_video_with_various_time_formats(self, mock_collection):
        """Test adding videos with different time formats"""
        test_cases = [
            ("Video 1", "10:30"),
            ("Video 2", "1:05:30"),
            ("Video 3", "5:00"),
            ("Video 4", "60 minutes")
        ]

        for name, time in test_cases:
            mock_collection.reset_mock()
            yt_manager.add_video(name, time)
            mock_collection.insert_one.assert_called_once()
            call_args = mock_collection.insert_one.call_args[0][0]
            assert call_args["time"] == time


class TestUpdateVideo:
    """Test cases for update_video function"""

    def test_update_video_success(self, mock_collection):
        """Test successfully updating a video"""
        video_id = ObjectId("507f1f77bcf86cd799439011")
        new_name = "Updated Python Tutorial"
        new_time = "12:00"

        mock_collection.find.return_value = []

        yt_manager.update_video(video_id, new_name, new_time)

        mock_collection.update_one.assert_called_once_with(
            {"_id": video_id},
            {"$set": {"name": new_name, "time": new_time}}
        )

    def test_update_video_only_name(self, mock_collection):
        """Test updating only the video name"""
        video_id = ObjectId("507f1f77bcf86cd799439011")
        new_name = "New Name"
        old_time = "10:30"

        mock_collection.find.return_value = []

        yt_manager.update_video(video_id, new_name, old_time)

        mock_collection.update_one.assert_called_once()
        call_args = mock_collection.update_one.call_args[0]
        assert call_args[1]["$set"]["name"] == new_name

    def test_update_video_only_time(self, mock_collection):
        """Test updating only the video time"""
        video_id = ObjectId("507f1f77bcf86cd799439011")
        old_name = "Python Tutorial"
        new_time = "20:00"

        mock_collection.find.return_value = []

        yt_manager.update_video(video_id, old_name, new_time)

        mock_collection.update_one.assert_called_once()
        call_args = mock_collection.update_one.call_args[0]
        assert call_args[1]["$set"]["time"] == new_time

    def test_update_nonexistent_video(self, mock_collection):
        """Test updating a video that doesn't exist"""
        video_id = ObjectId("507f1f77bcf86cd799439099")
        new_name = "Updated Name"
        new_time = "15:00"

        mock_collection.find.return_value = []
        mock_collection.update_one.return_value = MagicMock(matched_count=0)

        # Should not raise exception, MongoDB returns matched_count=0
        yt_manager.update_video(video_id, new_name, new_time)

        mock_collection.update_one.assert_called_once()


class TestDeleteVideo:
    """Test cases for delete_video function"""

    def test_delete_video_success(self, mock_collection):
        """Test successfully deleting a video"""
        video_id = ObjectId("507f1f77bcf86cd799439011")

        mock_collection.find.return_value = []
        mock_collection.delete_one.return_value = MagicMock(deleted_count=1)

        yt_manager.delete_video(video_id)

        mock_collection.delete_one.assert_called_once_with({"_id": video_id})

    def test_delete_nonexistent_video(self, mock_collection):
        """Test deleting a video that doesn't exist"""
        video_id = ObjectId("507f1f77bcf86cd799439099")

        mock_collection.find.return_value = []
        mock_collection.delete_one.return_value = MagicMock(deleted_count=0)

        # Should not raise exception, MongoDB returns deleted_count=0
        yt_manager.delete_video(video_id)

        mock_collection.delete_one.assert_called_once_with({"_id": video_id})

    def test_delete_video_calls_list_all(self, mock_collection):
        """Test that delete_video calls list_all_videos before deletion"""
        video_id = ObjectId("507f1f77bcf86cd799439011")

        mock_collection.find.return_value = []

        yt_manager.delete_video(video_id)

        # Verify list_all_videos was called (via collection.find)
        mock_collection.find.assert_called()
        mock_collection.delete_one.assert_called_once()


class TestMainFunction:
    """Test cases for main menu function"""

    @patch('builtins.input')
    def test_main_exit_immediately(self, mock_input, mock_collection):
        """Test exiting the application immediately"""
        mock_input.return_value = "5"

        yt_manager.main()

        mock_input.assert_called_once()

    @patch('builtins.input')
    def test_main_list_videos(self, mock_input, mock_collection):
        """Test selecting list videos option"""
        mock_input.side_effect = ["1", "5"]
        mock_collection.find.return_value = []

        yt_manager.main()

        mock_collection.find.assert_called()

    @patch('builtins.input')
    def test_main_add_video(self, mock_input, mock_collection):
        """Test selecting add video option"""
        mock_input.side_effect = ["2", "Test Video", "10:30", "5"]

        yt_manager.main()

        mock_collection.insert_one.assert_called_once()
        call_args = mock_collection.insert_one.call_args[0][0]
        assert call_args["name"] == "Test Video"
        assert call_args["time"] == "10:30"

    @patch('builtins.input')
    def test_main_update_video(self, mock_input, mock_collection):
        """Test selecting update video option"""
        video_id = "507f1f77bcf86cd799439011"
        mock_input.side_effect = ["3", video_id, "Updated Name", "20:00", "5"]
        mock_collection.find.return_value = []

        yt_manager.main()

        mock_collection.update_one.assert_called_once()

    @patch('builtins.input')
    def test_main_delete_video(self, mock_input, mock_collection):
        """Test selecting delete video option"""
        video_id = "507f1f77bcf86cd799439011"
        mock_input.side_effect = ["4", video_id, "5"]
        mock_collection.find.return_value = []

        yt_manager.main()

        mock_collection.delete_one.assert_called_once()

    @patch('builtins.input')
    def test_main_invalid_choice(self, mock_input, mock_collection, capsys):
        """Test entering an invalid menu choice"""
        mock_input.side_effect = ["9", "5"]

        yt_manager.main()

        captured = capsys.readouterr()
        assert "Invalid choice" in captured.out

    @patch('builtins.input')
    def test_main_multiple_operations(self, mock_input, mock_collection):
        """Test performing multiple operations in sequence"""
        mock_input.side_effect = [
            "2", "Video 1", "10:00",  # Add video
            "1",                        # List videos
            "2", "Video 2", "15:00",   # Add another video
            "5"                         # Exit
        ]
        mock_collection.find.return_value = []

        yt_manager.main()

        assert mock_collection.insert_one.call_count == 2
        mock_collection.find.assert_called()


class TestEdgeCases:
    """Test edge cases and error scenarios"""

    def test_add_video_with_long_name(self, mock_collection):
        """Test adding video with very long name"""
        long_name = "A" * 1000
        time = "10:30"

        yt_manager.add_video(long_name, time)

        mock_collection.insert_one.assert_called_once()
        call_args = mock_collection.insert_one.call_args[0][0]
        assert len(call_args["name"]) == 1000

    def test_update_with_unicode_characters(self, mock_collection):
        """Test updating video with unicode characters"""
        video_id = ObjectId("507f1f77bcf86cd799439011")
        name_unicode = "Python 教程 🐍"
        time = "10:30"

        mock_collection.find.return_value = []

        yt_manager.update_video(video_id, name_unicode, time)

        mock_collection.update_one.assert_called_once()
        call_args = mock_collection.update_one.call_args[0]
        assert call_args[1]["$set"]["name"] == name_unicode

    def test_add_video_with_newlines(self, mock_collection):
        """Test adding video with newlines in name"""
        name = "Line 1\nLine 2"
        time = "10:30"

        yt_manager.add_video(name, time)

        mock_collection.insert_one.assert_called_once()
        call_args = mock_collection.insert_one.call_args[0][0]
        assert "\n" in call_args["name"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
