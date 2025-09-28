#!/usr/bin/env python3
"""
Database Management Module for OSINT Intelligence Storage
Developer: Saad Dalvi (Roll No: 10468)
Description: Advanced SQLite database operations for intelligence data persistence
"""

import sqlite3
from pathlib import Path

def store_intelligence_data(intelligence_records, database_path):
    """
    Advanced database storage system for OSINT intelligence records.
    Ensures robust data persistence with comprehensive error handling.
    """
    # Ensure database directory structure exists
    db_directory = Path(database_path).parent
    db_directory.mkdir(parents=True, exist_ok=True)

    # Define intelligence database schema
    intelligence_columns = ["platform", "user", "timestamp", "text", "url", "sentiment"]
    
    try:
        # Establish database connection
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        
        # Create intelligence table with enhanced schema
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS social_media_posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                user TEXT,
                timestamp TEXT,
                text TEXT,
                url TEXT,
                sentiment TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Insert intelligence records with data validation
        successful_inserts = 0
        for record in intelligence_records:
            record_values = [record.get(col, "") for col in intelligence_columns]
            cursor.execute(f"""
               INSERT INTO social_media_posts ({', '.join(intelligence_columns)})
               VALUES ({', '.join('?' for _ in intelligence_columns)})
            """, record_values)
            successful_inserts += 1

        # Commit transaction
        connection.commit()
        print(f"✅ Successfully stored {successful_inserts} intelligence records in database")
        
    except sqlite3.Error as database_error:
        print(f"🚨 Database operation error: {database_error}")
    except Exception as general_error:
        print(f"🚨 Unexpected error during database storage: {general_error}")
    finally:
        if connection:
            connection.close()
