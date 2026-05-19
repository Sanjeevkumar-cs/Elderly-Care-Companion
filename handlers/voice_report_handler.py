# handlers/voice_report_handler.py - Voice Report Generation Logic
# ====================================================================

import sys
import os
import traceback

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import CURRENT_USER_ID
from database import (
    get_all_medications,
    get_refill_alerts,
    get_daily_summary,
    get_medication_status_report,
    get_upcoming_appointments
)
from voice_assistant import text_to_speech_gtts


def generate_voice_report():
    """Generate complete voice report"""
    try:
        print("📝 Generating complete health report...")
        
        # Fetch all data
        medications = get_all_medications(CURRENT_USER_ID)
        alerts = get_refill_alerts(CURRENT_USER_ID)
        daily_summary = get_daily_summary(CURRENT_USER_ID)
        appointments = get_upcoming_appointments(CURRENT_USER_ID)
        
        # Build complete text
        complete_text = "Hello. Here is your complete health report. "
        
        # Add medication status
        if medications:
            complete_text += f"You have {len(medications)} medications in your list. "
            for med in medications:
                days_left = med['pill_count'] // med['daily_dosage'] if med['daily_dosage'] > 0 else 0
                complete_text += f"{med['name']} has {med['pill_count']} pills remaining. "
                complete_text += f"You take {med['daily_dosage']} pill per day. "
                if days_left > 0:
                    complete_text += f"This will last about {days_left} days. "
                if med['refill_date']:
                    complete_text += f"Refill is needed by {med['refill_date']}. "
        else:
            complete_text += "You have no medications in your list. "
        
        # Add alerts
        if "REFILL OVERDUE" in alerts or "Low stock" in alerts:
            complete_text += "Here are your alerts. "
            clean_alerts = alerts.replace("⚠️ MEDICATION ALERTS:", "")
            clean_alerts = clean_alerts.replace("🔴", "")
            clean_alerts = clean_alerts.replace("🟡", "")
            clean_alerts = clean_alerts.replace("🟠", "")
            complete_text += clean_alerts
        elif "All medications have sufficient stock" in alerts:
            complete_text += "Good news. All medications have sufficient stock. "
        
        # Add daily summary
        complete_text += "Your daily summary. "
        if "No medications scheduled" not in daily_summary:
            schedule_text = daily_summary.replace("📋 **DAILY SUMMARY**", "")
            schedule_text = schedule_text.replace("💊 TODAY'S MEDICATIONS:", "Today's medications include")
            complete_text += schedule_text
        else:
            complete_text += "No medications scheduled for today. "
        
        # Add appointments
        if appointments:
            complete_text += f"You have {len(appointments)} upcoming appointments. "
            for apt in appointments:
                complete_text += f"Appointment with Dr {apt['doctor_name']} on {apt['date']} at {apt['time']}. "
        else:
            complete_text += "You have no upcoming appointments. "
        
        complete_text += "Take care of yourself. Consult your doctor if you have any concerns."
        
        print(f"✅ Report generated: {len(complete_text)} characters")
        
        # Generate voice
        audio_file = text_to_speech_gtts(complete_text, "complete_health_report.mp3")
        
        return audio_file
        
    except Exception as e:
        print(f"❌ Error generating voice report: {e}")
        traceback.print_exc()
        return None


def get_text_preview():
    """Get text preview for display"""
    try:
        medications = get_all_medications(CURRENT_USER_ID)
        alerts = get_refill_alerts(CURRENT_USER_ID)
        summary = get_daily_summary(CURRENT_USER_ID)
        appointments = get_upcoming_appointments(CURRENT_USER_ID)
        
        preview = f"""
=== YOUR COMPLETE HEALTH REPORT ===

📋 MEDICATIONS:
{len(medications)} medication(s) in your list.

{''.join([f'• {m["name"]}: {m["pill_count"]} pills left, {m["daily_dosage"]}/day\n' for m in medications])}

⚠️ ALERTS:
{alerts}

📅 DAILY SUMMARY:
{summary}

📅 APPOINTMENTS:
{len(appointments)} upcoming appointment(s)
{''.join([f'• Dr. {a["doctor_name"]} on {a["date"]} at {a["time"]}\n' for a in appointments])}
"""
        return preview
    except Exception as e:
        return f"Error loading preview: {e}"