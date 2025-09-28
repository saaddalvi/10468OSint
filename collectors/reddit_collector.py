#!/usr/bin/env python3
"""
Reddit Intelligence Collector  
Developer: Saad Dalvi (Roll No: 10468)
Description: Advanced Reddit data harvesting for OSINT intelligence operations
"""

import praw, os 
from dotenv import load_dotenv 

# Load environment configuration
load_dotenv() 

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_ID") 
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_SECRET") 

# Initialize Reddit API client
reddit_client = praw.Reddit(
    client_id=REDDIT_CLIENT_ID, 
    client_secret=REDDIT_CLIENT_SECRET, 
    user_agent="OSINT_Intelligence_System_v1.0_SaadDalvi"
) 

def fetch_reddit(target_subreddit="technology", post_limit=20): 
    """
    Advanced Reddit intelligence collection from specified subreddits
    Returns structured data for comprehensive OSINT analysis
    """
    intelligence_data = [] 
    
    try:
        # Collect hot posts from target subreddit
        subreddit_instance = reddit_client.subreddit(target_subreddit)
        hot_posts = subreddit_instance.hot(limit=post_limit)
        
        for post in hot_posts:  
            # Extract comprehensive post data
            post_content = f"{post.title} {post.selftext}".strip()
            post_author = str(post.author) if post.author else "deleted_user"
            post_created = str(post.created_utc)
            post_permalink = f"https://reddit.com{post.permalink}"
            
            # Structure intelligence record
            intelligence_record = {
                "platform": "reddit", 
                "user": post_author, 
                "timestamp": post_created, 
                "text": post_content,
                "url": post_permalink
            }
            
            intelligence_data.append(intelligence_record)
        
        print(f"🔴 Successfully collected {len(intelligence_data)} Reddit intelligence records from r/{target_subreddit}")
        return intelligence_data
    
    except Exception as collection_error:
        print(f"⚠️ Error during Reddit intelligence collection: {collection_error}")
        return [] 

