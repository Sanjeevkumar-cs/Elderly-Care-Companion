# handlers/medication_handler.py - Medication Management Logic
# ====================================================================
# Handles adding medications, refreshing displays, and alerts
# ====================================================================

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import CURRENT_USER_ID
from database import (
    add_medication,
    get_all_medications,
    get_refill_alerts
)


def add_new_medication(med_name, pill_count, daily_dosage, refill_date):
    """Add a new medication to the database"""
    if not med_name:
        return "❌ Please enter a medication name"
    
    try:
        refill_date_str = refill_date.strip() if refill_date else None
        
        add_medication(
            user_id=CURRENT_USER_ID,
            name=med_name,
            pill_count=int(pill_count),
            daily_dosage=int(daily_dosage),
            refill_date=refill_date_str
        )
        return f"✅ Added {med_name} successfully! Click 'Refresh Medications' to see updates."
    except Exception as e:
        return f"❌ Error adding medication: {e}"


def refresh_medication_display():
    """Get current medications to display in UI"""
    try:
        medications = get_all_medications(CURRENT_USER_ID)
        
        if not medications:
            return "📋 No medications added yet. Use the form above to add medications."
        
        display_text = "📋 **YOUR CURRENT MEDICATIONS**\n\n"
        for med in medications:
            display_text += f"💊 **{med['name']}**\n"
            display_text += f"   • Pills remaining: {med['pill_count']}\n"
            display_text += f"   • Daily dosage: {med['daily_dosage']} pills/day\n"
            if med['refill_date']:
                display_text += f"   • Refill by: {med['refill_date']}\n"
            display_text += "\n"
        
        return display_text
    except Exception as e:
        return f"❌ Error loading medications: {e}"


def refresh_alerts():
    """Get current alerts"""
    try:
        return get_refill_alerts(CURRENT_USER_ID)
    except Exception as e:
        return f"❌ Error loading alerts: {e}"