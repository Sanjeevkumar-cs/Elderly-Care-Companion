# fix_database_dates.py
# Run this file ONCE to fix integer dates in your database
# Place this file in the same folder as gradio_app_with_db.py

import sqlite3
from pathlib import Path
from datetime import datetime

# Path to your database
DB_PATH = Path("database") / "elderly_care.db"

def fix_refill_dates():
    """Convert integer timestamps to string dates in the database"""
    
    if not DB_PATH.exists():
        print(f"❌ Database not found at: {DB_PATH}")
        return
    
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get all medications
    cursor.execute("SELECT user_id, name, refill_date FROM medications")
    rows = cursor.fetchall()
    
    fixed_count = 0
    skipped_count = 0
    
    for row in rows:
        user_id = row['user_id']
        name = row['name']
        refill_date = row['refill_date']
        
        # Skip if None
        if refill_date is None:
            skipped_count += 1
            continue
        
        # Check if it's an integer (timestamp)
        if isinstance(refill_date, int):
            # Convert timestamp to date string
            date_str = datetime.fromtimestamp(refill_date).strftime('%Y-%m-%d')
            cursor.execute(
                "UPDATE medications SET refill_date = ? WHERE user_id = ? AND name = ?",
                (date_str, user_id, name)
            )
            print(f"✅ Fixed: {name} | {refill_date} -> {date_str}")
            fixed_count += 1
        else:
            print(f"ℹ️ Already string: {name} | {refill_date}")
            skipped_count += 1
    
    conn.commit()
    conn.close()
    
    print("\n" + "="*50)
    print("FIX COMPLETE")
    print("="*50)
    print(f"✅ Fixed: {fixed_count} medication(s)")
    print(f"ℹ️  Skipped: {skipped_count} medication(s)")
    print("="*50)

def verify_fix():
    """Verify that dates are now strings"""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, refill_date, typeof(refill_date) as type FROM medications")
    rows = cursor.fetchall()
    
    print("\n📋 VERIFICATION:")
    print("-"*40)
    for row in rows:
        print(f"  {row['name']}: {row['refill_date']} (type: {row['type']})")
    
    conn.close()

if __name__ == "__main__":
    print("="*50)
    print("🔧 FIXING DATABASE DATES")
    print("="*50)
    fix_refill_dates()
    verify_fix()
    print("\n✅ Now run: python gradio_app_with_db.py")