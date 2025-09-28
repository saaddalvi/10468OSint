#!/usr/bin/env python3
"""
Twitter Intelligence Collector
Developer: Saad Dalvi (Roll No: 10468)
Description: Advanced Twitter/X data collection for OSINT intelligence gathering
"""

import os
import requests
from dotenv import load_dotenv

# Load environment configuration
load_dotenv()
TWITTER_API_KEY = os.getenv("TWITTER_IO_KEY")

def fetch_twitter(search_query="AI", record_limit=10):
    """
    Enhanced Twitter intelligence collection using twitterapi.io service
    Returns structured data for OSINT analysis
    """
    # Validate API credentials
    if not TWITTER_API_KEY:
        print("⚠️ Error: TWITTER_IO_KEY not configured in environment variables")
        return []
    
    # API endpoint configuration
    api_endpoint = "https://api.twitterapi.io/twitter/community/get_tweets_from_all_community"
    
    # Request parameters
    query_params = {
        "query": search_query,
        "queryType": "Latest",
        "cursor": ""
    }
    
    # Request headers with authentication
    request_headers = {
        "x-api-key": TWITTER_API_KEY,
        "Content-Type": "application/json",
        "User-Agent": "OSINT-Intelligence-System/1.0"
    }
    
    try:
        # Execute API request with timeout
        api_response = requests.get(
            api_endpoint, 
            headers=request_headers, 
            params=query_params, 
            timeout=30
        )
        
        # Validate API response
        if api_response.status_code != 200:
            print(f"🚨 Twitter API Error: HTTP {api_response.status_code} - {api_response.text[:200]}")
            return []
        
        # Parse response data
        response_data = api_response.json()
        
        # Process tweet data
        intelligence_results = []
        tweet_data = (response_data.get("statuses", [])[:record_limit] or 
                     response_data.get("data", [])[:record_limit] or 
                     response_data.get("tweets", [])[:record_limit])
        
        # Extract intelligence from tweets
        for tweet in tweet_data:
            tweet_text = tweet.get("text") or tweet.get("full_text") or ""
            username = (tweet.get("user", {}).get("screen_name", "") if 
                       isinstance(tweet.get("user"), dict) else 
                       tweet.get("screen_name", ""))
            created_time = tweet.get("created_at", "")
            tweet_identifier = tweet.get("id_str", "") or str(tweet.get("id", ""))
            
            # Structure intelligence record
            intelligence_results.append({
                "platform": "twitter",
                "user": username,
                "timestamp": created_time,
                "text": tweet_text,
                "url": f"https://twitter.com/user/status/{tweet_identifier}" if tweet_identifier else ""
            })
        
        print(f"🐦 Successfully collected {len(intelligence_results)} Twitter intelligence records")
        return intelligence_results
        
    except requests.exceptions.RequestException as request_error:
        print(f"🌐 Twitter API request failed: {request_error}")
        return []
