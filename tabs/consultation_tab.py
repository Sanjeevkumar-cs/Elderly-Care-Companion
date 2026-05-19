# tabs/consultation_tab.py - AI Doctor Consultation Tab UI
# ====================================================================
# UI components for the AI doctor consultation tab
# ====================================================================

import gradio as gr
from handlers.consultation_handler import process_consultation


def create_consultation_tab():
    """Create the AI Doctor Consultation tab"""
    
    with gr.TabItem("🩺 AI Doctor Consultation"):
        with gr.Row():
            with gr.Column():
                gr.Markdown("### 🎤 Speak Your Symptoms")
                audio_input = gr.Audio(
                    sources=["microphone"], 
                    type="filepath", 
                    label="Click microphone to record"
                )
                
                gr.Markdown("### 📸 Upload Image (Optional)")
                image_input = gr.Image(
                    type="filepath", 
                    label="Upload skin condition image"
                )
                
                submit_btn = gr.Button("🩺 Get AI Doctor Advice", variant="primary")
            
            with gr.Column():
                gr.Markdown("### 📝 Consultation Results")
                transcript_output = gr.Textbox(
                    label="What you said (Speech to Text)", 
                    lines=3
                )
                doctor_output = gr.Textbox(
                    label="Doctor's Response", 
                    lines=15
                )
                audio_output = gr.Audio(
                    label="Doctor's Voice Response", 
                    type="filepath"
                )
        
        # Connect the button
        submit_btn.click(
            fn=process_consultation,
            inputs=[audio_input, image_input],
            outputs=[transcript_output, doctor_output, audio_output]
        )
    
    return audio_input, image_input, submit_btn, transcript_output, doctor_output, audio_output