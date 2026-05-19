# tabs/medication_tab.py - Medication Manager Tab UI
# ====================================================================
# UI components for medication management
# ====================================================================

import gradio as gr
from handlers.medication_handler import (
    add_new_medication,
    refresh_medication_display,
    refresh_alerts
)


def create_medication_tab():
    """Create the Medication Manager tab"""
    
    with gr.TabItem("💊 Medication Manager"):
        gr.Markdown("### Add New Medication")
        
        with gr.Row():
            with gr.Column():
                med_name = gr.Textbox(
                    label="💊 Medication Name", 
                    placeholder="e.g., Paracetamol, Aspirin"
                )
                
                pill_count = gr.Number(
                    label="💊 Number of Pills", 
                    value=30, 
                    precision=0,
                    minimum=0
                )
                
                daily_dosage = gr.Number(
                    label="📅 Daily Dosage (pills/day)", 
                    value=1, 
                    precision=0,
                    minimum=1
                )
                
                refill_date = gr.Textbox(
                    label="📅 Refill Date", 
                    placeholder="2026-06-15",
                    info="Format: YYYY-MM-DD (Year-Month-Day)"
                )
                
                add_med_btn = gr.Button("➕ Add Medication", variant="primary")
                add_result = gr.Textbox(label="Status", lines=2, interactive=False)
        
        gr.Markdown("---")
        gr.Markdown("### 📋 Your Current Medications")
        
        refresh_btn = gr.Button("🔄 Refresh Medications", variant="secondary")
        medication_display = gr.Textbox(label="Medications", lines=10, interactive=False)
        
        gr.Markdown("---")
        gr.Markdown("### ⚠️ Refill Alerts")
        alerts_display = gr.Textbox(label="Alerts", lines=5, interactive=False)
        
        # Connect button functions
        add_med_btn.click(
            add_new_medication, 
            [med_name, pill_count, daily_dosage, refill_date], 
            [add_result]
        )
        refresh_btn.click(refresh_medication_display, outputs=[medication_display])
        refresh_btn.click(refresh_alerts, outputs=[alerts_display])
    
    return med_name, pill_count, daily_dosage, refill_date, add_med_btn, add_result, refresh_btn, medication_display, alerts_display