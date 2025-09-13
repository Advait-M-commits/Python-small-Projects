import os
import re
import requests
import praw
from urllib.parse import urlparse
from datetime import datetime
import time


CLIENT_ID = "7H8aa1TlwYjZQIlLuapWLg"
CLIENT_SECRET = "MD9AAEGVAxtK4TKrmV7gpsWO23BhJQ"
USER_AGENT = "r/IndianTeenagers"


SUBREDDIT_NAME = "IndianTeenagers"
SORT_METHOD = "hot"          
TIME_PERIOD = "day"          
MAX_POSTS = 50               
OUTPUT_FOLDER = "downloaded_memes"


SUPPORTED_IMAGE_TYPES = (".jpg", ".jpeg", ".png", ".webp", ".gif")

def create_safe_filename(reddit_title: str, post_id: str) -> str:
    clean_title = re.sub(r'[\\/*?:"<>|\[\]{}]', "", reddit_title)
    clean_title = re.sub(r'\s+', '_', clean_title.strip())
    clean_title = clean_title[:150]
    return f"{clean_title}_{post_id}"

def download_image(image_url: str, save_path: str, title: str) -> bool:
    print(f"Downloading: {title[:60]}{'...' if len(title) > 60 else ''}")
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MemeBot/1.0)',
            'Accept': 'image/*'
        }
        
        response = requests.get(image_url, stream=True, timeout=30, headers=headers)
        response.raise_for_status()
        
        content_type = response.headers.get('content-type', '').lower()
        if not content_type.startswith('image/'):
            print(f"Warning: URL doesn't seem to be an image ({content_type})")
        
        total_size = 0
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    total_size += len(chunk)
        
        if total_size < 1024:
            size_str = f"{total_size}B"
        elif total_size < 1024 * 1024:
            size_str = f"{total_size/1024:.1f}KB"
        else:
            size_str = f"{total_size/(1024*1024):.1f}MB"
            
        print(f"Success! Saved {size_str}")
        return True
        
    except requests.exceptions.Timeout:
        print("Download timed out - skipping this one")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Network error: {str(e)[:100]}...")
        return False
    except IOError as e:
        print(f"File save error: {str(e)[:100]}...")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)[:100]}...")
        return False

def setup_reddit_connection():
    print("Connecting to Reddit...")
    
    if CLIENT_ID == "YOUR_CLIENT_ID" or CLIENT_SECRET == "YOUR_CLIENT_SECRET":
        print("Error: Please update CLIENT_ID and CLIENT_SECRET with your Reddit API credentials")
        print("Get them from: https://www.reddit.com/prefs/apps")
        return None
    
    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT
        )
        
        reddit.user.me()
        print("Reddit connection successful!")
        return reddit
        
    except praw.exceptions.ResponseException as e:
        print(f"Reddit API error: {e}")
        print("Check your CLIENT_ID and CLIENT_SECRET")
        return None
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def get_posts_from_subreddit(reddit, subreddit_name: str, sort_method: str, time_period: str, limit: int):
    print(f"Getting {limit} {sort_method} posts from r/{subreddit_name}...")
    
    try:
        subreddit = reddit.subreddit(subreddit_name)
        
        if sort_method.lower() == "hot":
            posts = subreddit.hot(limit=limit)
        elif sort_method.lower() == "new":
            posts = subreddit.new(limit=limit)
        elif sort_method.lower() == "top":
            posts = subreddit.top(time_filter=time_period, limit=limit)
        elif sort_method.lower() == "rising":
            posts = subreddit.rising(limit=limit)
        else:
            print(f"Unknown sort method '{sort_method}', using 'hot' instead")
            posts = subreddit.hot(limit=limit)
            
        return posts
        
    except Exception as e:
        print(f"Error accessing subreddit: {e}")
        return None

def extract_image_url(post):
    post_url = post.url
    parsed_url = urlparse(post_url)
    file_extension = os.path.splitext(parsed_url.path)[1].lower()
    
    if file_extension in SUPPORTED_IMAGE_TYPES:
        return post_url, file_extension
    
    if hasattr(post, "preview") and "images" in post.preview:
        try:
            image_data = post.preview["images"][0]
            if "source" in image_data:
                preview_url = image_data["source"]["url"]
                preview_url = preview_url.replace("&amp;", "&")
                
                preview_extension = os.path.splitext(urlparse(preview_url).path)[1].lower()
                if not preview_extension:
                    preview_extension = ".jpg"
                    
                return preview_url, preview_extension
        except (KeyError, IndexError):
            pass
    
    return None, None

def main():
    print("Memes Scraper Starting!")
    print("=" * 50)
    
    print(f"Setting up output folder: {OUTPUT_FOLDER}")
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    reddit = setup_reddit_connection()
    if not reddit:
        print("Can't continue without Reddit connection. Exiting...")
        return
    
    posts = get_posts_from_subreddit(reddit, SUBREDDIT_NAME, SORT_METHOD, TIME_PERIOD, MAX_POSTS)
    if not posts:
        print("Couldn't fetch posts. Exiting...")
        return
    
    print("\nStarting to process posts...")
    print("-" * 30)
    
    successful_downloads = 0
    skipped_posts = 0
    processed_posts = 0
    
    start_time = time.time()
    
    for post in posts:
        processed_posts += 1
        
        if post.stickied:
            print(f"Skipping pinned post: {post.title[:50]}...")
            skipped_posts += 1
            continue
        
        image_url, file_extension = extract_image_url(post)
        
        if not image_url:
            print(f"No image found in: {post.title[:50]}...")
            skipped_posts += 1
            continue
        
        safe_title = create_safe_filename(post.title, post.id)
        filename = f"{safe_title}{file_extension}"
        file_path = os.path.join(OUTPUT_FOLDER, filename)
        
        if os.path.exists(file_path):
            print(f"Already exists: {post.title[:50]}...")
            skipped_posts += 1
            continue
        
        if download_image(image_url, file_path, post.title):
            successful_downloads += 1
            print(f"Score: {post.score} | Comments: {post.num_comments}")
        else:
            skipped_posts += 1
            if os.path.exists(file_path):
                os.remove(file_path)
        
        print()
        time.sleep(0.5)
    
    elapsed_time = time.time() - start_time
    print("=" * 50)
    print("SCRAPING COMPLETE!")
    print(f"Results Summary:")
    print(f"Posts processed: {processed_posts}")
    print(f"Images downloaded: {successful_downloads}")
    print(f"Posts skipped: {skipped_posts}")
    print(f"Success rate: {(successful_downloads/processed_posts)*100:.1f}%")
    print(f"Time taken: {elapsed_time:.1f} seconds")
    print(f"Files saved to: {os.path.abspath(OUTPUT_FOLDER)}")
    
    if successful_downloads > 0:
        print(f"\nEnjoy your {successful_downloads} fresh Indian dank memes!")
    else:
        print(f"\nNo memes downloaded this time. Try adjusting your settings!")

if __name__ == "__main__":
    main()