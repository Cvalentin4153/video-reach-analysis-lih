# Import necessary libraries
import requests  # For making HTTP requests to the YouTube API
import sys       # For writing error messages to stderr
from api_key import api_key # For API key

def get_video_data(video_id):
    """
    Fetches video data (snippet and statistics) from the YouTube Data API v3.

    Args:
        video_id (str): The ID of the YouTube video.

    Returns:
        dict: A dictionary containing video details (videoId, title, publishedAt,
              viewCount, likeCount, commentCount) if successful, otherwise None.
    """
    # YouTube Data API v3 endpoint for videos
    url = 'https://www.googleapis.com/youtube/v3/videos'
    # API key for accessing the YouTube Data API.
    # IMPORTANT: It's generally not recommended to hardcode API keys directly in the script.
    # Consider using environment variables or a configuration file for better security.

    # Parameters for the API request
    params = {
        "part": "snippet,statistics",  # Requesting both snippet (title, description, etc.) and statistics (views, likes, etc.)
        "id": video_id,                # The ID of the video to fetch data for
        "key": api_key                 # The API key
    }

    # Make the GET request to the YouTube API
    response = requests.get(url, params=params)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code != 200:
        # Print an error message to standard error if the request failed
        print(f"Error {response.status_code} for video {video_id}", file=sys.stderr)
        return None  # Return None to indicate failure

    # Parse the JSON response from the API
    data = response.json()

    # Extract the 'items' list from the response data. Default to an empty list if 'items' is not found.
    items = data.get("items", [])

    # Check if the 'items' list is empty (meaning no data was returned for the video_id)
    if not items:
        # Print an error message, including any error message from the API response if available
        error_message = data.get('error', {}).get('message', '')
        print(f"No data for video {video_id}: {error_message}", file=sys.stderr)
        return None  # Return None to indicate failure

    # For debugging or informational purposes, print the number of items returned.
    # Typically, for a single video ID, this should be 1.
    print("\nNumber of items returned:", len(items))

    # Get the first item from the list (assuming only one video's data is returned for a single ID)
    item = items[0]
    # Extract the 'snippet' part of the video data
    snippet = item["snippet"]
    # Extract the 'statistics' part of the video data
    stats = item["statistics"]

    # Construct a dictionary with the desired video information
    # .get() is used with a default value to prevent KeyError if a field is missing
    # and to ensure consistent data types (e.g., int for counts).
    return {
        "videoId": item["id"],                                  # Video ID
        "title": snippet.get("title", ""),                      # Video title, default to empty string if not present
        "publishedAt": snippet.get("publishedAt", ""),          # Video publication date, default to empty string
        "viewCount": int(stats.get("viewCount", 0)),            # View count, default to 0 and cast to int
        "likeCount": int(stats.get("likeCount", 0)),            # Like count, default to 0 and cast to int
        "commentCount": int(stats.get("commentCount", 0)),      # Comment count, default to 0 and cast to int
    }
