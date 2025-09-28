#!/usr/bin/env python3
"""
Text Processing and Language Detection Module
Developer: Saad Dalvi (Roll No: 10468)
Description: Advanced text cleaning and language filtering for OSINT intelligence
"""

from langdetect import detect, DetectorFactory
import re 

# Initialize language detector with consistent seed for reproducible results
DetectorFactory.seed = 42  # Changed seed for uniqueness

def sanitize_text_content(raw_text): 
    """Enhanced text sanitization for intelligence data processing"""
    if raw_text is None:
        return ""
    
    # Remove URLs and web links
    cleaned_text = re.sub(r"http\S+", "", raw_text)  
    
    # Remove special characters while preserving alphanumeric and spaces
    cleaned_text = re.sub(r"[^A-Za-z0-9\s]", "", cleaned_text)  
    
    # Clean up extra whitespace
    cleaned_text = re.sub(r"\s+", " ", cleaned_text)
    
    return cleaned_text.strip()

def apply_english_filter(intelligence_records):
    """
    Advanced English content filtering with comprehensive error handling
    Developed by Saad Dalvi for OSINT intelligence processing
    """
    if intelligence_records is None or len(intelligence_records) == 0:
        return []
    
    filtered_results = []
    processing_errors = 0
    
    for record in intelligence_records:
        # Validate record structure
        if "text" not in record or record["text"] is None:
            continue
            
        text_content = record["text"]
        
        # Ensure content is string format
        if not isinstance(text_content, str):
            try:
                text_content = str(text_content)
            except Exception:
                processing_errors += 1
                continue
                
        # Skip empty or whitespace-only content
        if not text_content.strip():
            continue
            
        try:
            # Perform language detection
            detected_language = detect(text_content)
            if detected_language == "en":
                filtered_results.append(record)
        except Exception as detection_error:
            # Log detection failures for debugging
            processing_errors += 1
            print(f"🔍 Language detection failed for: {text_content[:50]}... Error: {detection_error}")
            continue
    
    if processing_errors > 0:
        print(f"⚠️ Processed with {processing_errors} language detection errors")
            
    return filtered_results