# **OSINT Social Media Intelligence System**

**Author:** Saad Dalvi (Roll No: 10468)

A comprehensive Open Source Intelligence (OSINT) system designed for collecting, processing, and analyzing social media data across multiple platforms. This intelligent pipeline automatically harvests content from various social networks, applies advanced data cleaning techniques, performs sentiment analysis, and maintains structured database storage for analytical purposes.


# **📋 Table of Contents**

Overview

Features

Supported Platforms

Installation

Configuration

Usage


# **🌟 System Overview**

The OSINT Social Media Intelligence System serves researchers, cybersecurity analysts, and intelligence professionals requiring comprehensive social media monitoring capabilities. This unified platform aggregates data from diverse sources, processes information through a sophisticated pipeline, and delivers structured, actionable intelligence data.


# **✨ Core Features**

🌐 **Multi-Platform Integration**: Seamlessly collect data from 10+ social media platforms

🧹 **Advanced Data Processing**: Automated URL extraction, symbol filtering, and content normalization

🌍 **Language Intelligence**: Smart content filtering with language detection (English-focused)

📊 **Sentiment Intelligence**: Comprehensive sentiment analysis powered by TextBlob

💾 **Persistent Storage**: Robust SQLite database implementation for data retention

🛡️ **Error Resilience**: Advanced error handling with graceful fallback mechanisms

🔧 **Modular Design**: Flexible architecture supporting easy platform additions and feature extensions


# **📱 Supported Platforms**

✅ Twitter (via RapidAPI)

✅ Reddit (via PRAW)

✅ Facebook (via Graph API/RapidAPI)

✅ Instagram (via Instagrapi)

✅ TikTok (via RapidAPI)

✅ Mastodon (via Mastodon.py)

✅ GitHub (via GitHub API)

✅ Snapchat (via RapidAPI)


# **🔧 Installation**

Prerequisites
Python 3.8+

pip (Python package manager)

API keys for various services (see Configuration)

Step-by-Step Installation
1.Clone the repository
git clone https://github.com/yourusername/osint-pipeline.git
cd osint-pipeline

2.Create a virtual environment
python -m venv osint_env
source osint_env/bin/activate  # On Windows: osint_env\Scripts\activate

3.Install dependencies
pip install -r requirements.txt


# **⚙️ Configuration**
Environment Variables
Create a .env file in the root directory with the following variables:

## **RapidAPI Keys**

TIKTOK_KEY=your_tiktok_api_key_here

SNAPCHAT_KEY=your_snapchat_api_key_here

FACEBOOK_ACCESS_TOKEN=your_facebook_key_here

INSTAGRAM_KEY=your_instagram_key_here

TWITTER_KEY=your_twitter_key_here

## **Reddit API**

REDDIT_CLIENT_ID=your_reddit_client_id

REDDIT_CLIENT_SECRET=your_reddit_client_secret

REDDIT_USER_AGENT=your_reddit_user_agent

## **GitHub API**

GITHUB_TOKEN=your_github_token_here

## **Mastodon API**

MATODON_TOKEN=your_mastodon_token_here


# **🚀 Usage**

Run the complete pipeline:

python main.py
