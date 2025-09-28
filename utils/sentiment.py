#!/usr/bin/env python3
"""
Sentiment Analysis Intelligence Module
Developer: Saad Dalvi (Roll No: 10468)  
Description: Advanced sentiment analysis for OSINT intelligence data
"""

from textblob import TextBlob

def perform_sentiment_analysis(intelligence_data):
    """
    Enhanced sentiment analysis processor for intelligence records
    Analyzes emotional tone: Positive, Negative, or Neutral classification
    """
    if not intelligence_data or len(intelligence_data) == 0:
        return []

    processed_count = 0
    
    for record in intelligence_data:
        text_content = record.get("text", "")
        
        if text_content and text_content.strip():
            # Perform sentiment analysis using TextBlob
            sentiment_blob = TextBlob(text_content)
            polarity_score = sentiment_blob.sentiment.polarity  # Range: -1.0 to 1.0
            
            # Enhanced sentiment classification with adjusted thresholds
            if polarity_score > 0.15:
                sentiment_classification = "Positive"
            elif polarity_score < -0.15:
                sentiment_classification = "Negative" 
            else:
                sentiment_classification = "Neutral"
                
            processed_count += 1
        else:
            sentiment_classification = "Neutral"  # Default for empty content
        
        record["sentiment"] = sentiment_classification
    
    print(f"📊 Completed sentiment analysis on {processed_count} records")
    return intelligence_data

