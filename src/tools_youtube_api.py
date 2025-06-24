import os
import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv
import markdown

# Load environment variables from .env file

async def search_youtube_videos(query, max_results=1):
    load_dotenv()

    """
    Searches for YouTube videos based on a query.

    Args:
        query (str): The search term.
        max_results (int): The maximum number of results to return.

    Returns:
        None. Prints the search results.
    """
    # --- Step 1: Get API key ---
    # It's recommended to use an environment variable for the API key.
    # You can also replace os.environ.get("YOUTUBE_API_KEY") with your raw API key string
    # for a quick test, but this is not recommended for production code.
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        print("Error: Please set the YOUTUBE_API_KEY environment variable.")
        return

    # --- Step 2: Build the YouTube API Service ---
    api_service_name = "youtube"
    api_version = "v3"

    try:
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=api_key)

        # --- Step 3: Make the API Request ---
        request = youtube.search().list(
            q=query,
            part="snippet",  # Specifies the resource properties to include
            maxResults=max_results,
            type="video"  # We only want to search for videos
        )

        # --- Step 4: Execute the Request and Process the Response ---
        response = request.execute()

        print(f"--- Search Results for '{query}' ---")
        for item in response.get("items", []):
            video_title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            print(f"Title: {video_title}")
            print(f"URL: {video_url}\n")
            return video_url

    except googleapiclient.errors.HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    # Based on your interests, here are some example queries.
    # You can change the search_query to whatever you like.

    # search_query = "Formula 1 highlights"
    search_query = "Dubai T100 highlights"
    # search_query = "python for quantitative finance"

    search_youtube_videos(search_query, max_results=1)