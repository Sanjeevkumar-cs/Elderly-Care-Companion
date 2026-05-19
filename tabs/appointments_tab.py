# tabs/appointments_tab.py - Appointments & Reminders Tab UI
# ====================================================================
# UI components for appointments and daily summary
# ====================================================================

import gradio as gr
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import CURRENT_USER_ID
from database import get_daily_summary, get_refill_alerts


def create_appointments_tab():
    """Create the Appointments & Reminders tab"""
    
    with gr.TabItem("📅 Appointments & Reminders"):
        gr.Markdown("### 📋 Daily Summary")
        summary_display = gr.Textbox(label="Today's Summary", lines=15, interactive=False)
        refresh_summary_btn = gr.Button("🔄 Refresh Summary", variant="secondary")
        
        gr.Markdown("---")
        gr.Markdown("### ⚠️ All Refill Alerts")
        all_alerts_display = gr.Textbox(label="Refill Alerts", lines=10, interactive=False)
        
        def get_daily_summary_safe():
            try:
                return get_daily_summary(CURRENT_USER_ID)
            except Exception as e:
                return f"Error loading summary: {e}"
        
        def get_refill_alerts_safe():
            try:
                return get_refill_alerts(CURRENT_USER_ID)
            except Exception as e:
                return f"Error loading alerts: {e}"
        
        refresh_summary_btn.click(get_daily_summary_safe, outputs=[summary_display])
        refresh_summary_btn.click(get_refill_alerts_safe, outputs=[all_alerts_display])
    
    return summary_display, refresh_summary_btn, all_alerts_display