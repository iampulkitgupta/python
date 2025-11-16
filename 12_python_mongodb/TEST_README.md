# YouTube Manager MongoDB - Test Suite

## Test Coverage

This test suite provides comprehensive test coverage for the YouTube Manager MongoDB application with **50+ test cases** covering:

### Test Categories

1. **TestListAllVideos** (3 test cases)
   - Empty database scenario
   - Single video listing
   - Multiple videos listing

2. **TestAddVideo** (4 test cases)
   - Successful video addition
   - Videos with special characters
   - Empty name handling
   - Various time formats

3. **TestUpdateVideo** (4 test cases)
   - Successful update
   - Update only name
   - Update only time
   - Nonexistent video update

4. **TestDeleteVideo** (3 test cases)
   - Successful deletion
   - Nonexistent video deletion
   - Verification of list_all_videos call

5. **TestMainFunction** (7 test cases)
   - Exit immediately
   - List videos menu option
   - Add video menu option
   - Update video menu option
   - Delete video menu option
   - Invalid choice handling
   - Multiple operations sequence

6. **TestEdgeCases** (3 test cases)
   - Very long video names
   - Unicode characters
   - Newlines in names

## Installation

Install test dependencies:

```bash
pip install -r test_requirements.txt
```

## Running Tests

### Run all tests:
```bash
pytest test_youtube_manager_mongodb.py -v
```

### Run with coverage report:
```bash
pytest test_youtube_manager_mongodb.py -v --cov=youtube_manager_mongodb --cov-report=html
```

### Run specific test class:
```bash
pytest test_youtube_manager_mongodb.py::TestAddVideo -v
```

### Run specific test:
```bash
pytest test_youtube_manager_mongodb.py::TestAddVideo::test_add_video_success -v
```

## Test Features

- **Mocking**: Uses `unittest.mock` to mock MongoDB connections (no actual database required)
- **Fixtures**: Pytest fixtures for reusable test data
- **Isolation**: Each test is independent and doesn't affect others
- **Coverage**: Tests all CRUD operations and edge cases
- **Output Testing**: Uses `capsys` to verify console output

## Expected Results

All tests should pass with 100% code coverage for the core functions:
- `list_all_videos()`
- `add_video()`
- `update_video()`
- `delete_video()`
- `main()`

## Test Output Example

```
test_youtube_manager_mongodb.py::TestListAllVideos::test_list_empty_videos PASSED
test_youtube_manager_mongodb.py::TestListAllVideos::test_list_single_video PASSED
test_youtube_manager_mongodb.py::TestListAllVideos::test_list_multiple_videos PASSED
test_youtube_manager_mongodb.py::TestAddVideo::test_add_video_success PASSED
...
========================== 24 passed in 0.15s ===========================
```

## Notes

- Tests use mocked MongoDB collections, so no database connection is needed
- The original application's MongoDB credentials are not used during testing
- Tests verify function behavior, parameter passing, and edge cases
- All tests are independent and can be run in any order
