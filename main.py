#!/usr/bin/env python3
"""
OSINT Social Media Intelligence System
Developer: Saad Dalvi
Roll Number: 10468
Description: Advanif __name__ == "__main__":
    print("🔍 OSINT Intelligence System - Developed by Saad Dalvi (10468)")
    execute_intelligence_pipeline(100)
    print("\n📊 Recent Intelligence Records:")
    display_intelligence_records(display_limit=20)SINT pipeline for multi-platform social media intelligence gathering
"""

# Platform Data Collectors
from collectors.twitter_collector import fetch_twitter 
from collectors.reddit_collector import fetch_reddit 
from collectors.facebook_collector import fetch_facebook 
from collectors.instagram_collector import fetch_instagram
from collectors.tiktok_collector import fetch_tiktok 
from collectors.linkedin_collector import fetch_linkedin 
from collectors.telegram_collector import fetch_telegram 
#from collectors.discord_collector import messages 
from collectors.mastodon_collector import fetch_mastodon 
from collectors.github_collector import fetch_github 
from collectors.quora_collector import fetch_quora 
from collectors.vk_collector import fetch_vk 
from collectors.snapchat_collector import fetch_snapchat 

# Data Processing Utilities
from utils.cleaners import sanitize_text_content, apply_english_filter 
from utils.database import store_intelligence_data 
from utils.sentiment import perform_sentiment_analysis

# System Libraries
from pathlib import Path
import sqlite3
from tabulate import tabulate

# Intelligence Database Configuration
BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "data" / "saad_osint_intelligence.db"  # Personalized database name

def standardize_data_schema(data_item, source_platform):
    """Transform collected data into standardized intelligence schema"""
    if not data_item:
        return None
    
    # Standardize field mapping for consistent data structure
    standardized_record = {
        "platform": source_platform,
        "user": data_item.get("user") or data_item.get("username") or "Unknown_User",
        "timestamp": data_item.get("timestamp") or data_item.get("date") or data_item.get("created_at"),
        "text": data_item.get("text") or data_item.get("caption") or data_item.get("description") or "",
        "url": data_item.get("url") or data_item.get("link") or "",
        "sentiment": None  # To be populated during sentiment analysis phase
    }
    
    return standardized_record

def display_intelligence_records(table_name="social_media_posts", display_limit=10):
    """Display stored intelligence records in formatted table - Saad Dalvi's System"""
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    try:
        cursor.execute(f"SELECT platform, user, sentiment, substr(text, 1, 50) as text_preview FROM {table_name} LIMIT {display_limit}")
        records = cursor.fetchall()
        if not records:
            print(f"📊 No intelligence records found in table '{table_name}'.")
            return
        
        # Extract column headers
        column_headers = ["Platform", "User", "Sentiment", "Text Preview"]
        
        # Display formatted table
        print("🔍 OSINT Intelligence Records:")
        print(tabulate(records, headers=column_headers, tablefmt="grid"))
        
    except sqlite3.Error as db_error:
        print(f"🚨 Database access error: {db_error}")
    finally:
        connection.close()

def execute_intelligence_pipeline(target_records=100):
    """Main intelligence gathering pipeline - Saad Dalvi's OSINT System"""
    collected_data = []

    # Platform configuration with search parameters
    intelligence_sources = [
        ("Twitter", fetch_twitter, ("AI", 10)),
        ("Reddit", fetch_reddit, ("technology", 10)),
        ("Facebook", fetch_facebook, ("cnn", 5)),
        ("Instagram", fetch_instagram, ("gaming", 5)),
        ("TikTok", fetch_tiktok, ("cybersecurity", 5)),
        ("Mastodon", fetch_mastodon, ("ai", 5)),
        ("GitHub", fetch_github, ("leak", 5)),
        ("Snapchat", fetch_snapchat, ("mrbeast",))
    ]

    print(f"🚀 Initiating OSINT intelligence collection for {target_records} records...")

    # Execute data collection from each intelligence source
    for platform_name, fetch_func, args in intelligence_sources:
        try:
            print(f"🔄 Attempting to collect data from {platform_name}...")
            platform_data = fetch_func(*args)
            if platform_data:
                normalized = [standardize_data_schema(d, platform_name) for d in platform_data if d]
                collected_data.extend(normalized)
                print(f"✅ Successfully collected {len(platform_data)} records from {platform_name}")
            else:
                print(f"⚠️ No data returned from {platform_name}")
        except Exception as e:
            print(f"❌ Error accessing {platform_name}: {e}")

        # Limit collection to target record count
        if len(collected_data) >= target_records:
            collected_data = collected_data[:target_records]
            break

    print(f"📊 Successfully collected {len(collected_data)} records. Processing and enriching data...")

    # Apply text cleaning and normalization
    for record in collected_data:
        if record.get("text"):
            record["text"] = sanitize_text_content(record["text"])

    # Apply English language filtering
    collected_data = apply_english_filter(collected_data)

    # Ensure final dataset matches target size
    collected_data = collected_data[:target_records]

    # Apply sentiment analysis intelligence
    collected_data = perform_sentiment_analysis(collected_data)

    # Store processed intelligence in database
    store_intelligence_data(collected_data, DB_PATH)
    print(f"✅ Successfully stored {len(collected_data)} intelligence records in database")

if __name__ == "__main__":
    print("🔍 OSINT Intelligence System - Developed by Saad Dalvi (10468)")
    execute_intelligence_pipeline(100)
    print("\n� Recent Intelligence Records:")
    display_intelligence_records(display_limit=20)

