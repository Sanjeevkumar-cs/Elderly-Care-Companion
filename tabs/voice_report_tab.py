# tabs/voice_report_tab.py - Voice Report Tab UI
# ====================================================================

import gradio as gr
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from handlers.voice_report_handler import generate_voice_report, get_text_preview


def create_voice_report_tab():
    """Create the Voice Report tab"""
    
    with gr.TabItem("🔊 Voice Report"):
        gr.Markdown("""
        ## 🎙️ Complete Health Report
        ### One Click - Listen to Everything
        
        This report includes:
        - ✅ All your medications with stock status
        - ✅ Refill alerts and overdue medications
        - ✅ Today's medication schedule
        - ✅ Upcoming appointments
        """)
        
        gr.Markdown("---")
        
        with gr.Row():
            with gr.Column():
                # Big, clear button for elderly users
                voice_report_btn = gr.Button(
                    "🔊 READ COMPLETE HEALTH REPORT", 
                    variant="primary", 
                    size="lg"
                )
                
                gr.Markdown("""
                💡 **How to use:**
                1. Click the big button above
                2. Wait a few seconds for voice generation
                3. Audio will play automatically
                4. You can also download the audio file
                """)
            
            with gr.Column():
                voice_audio_output = gr.Audio(
                    label="🎵 Voice Report", 
                    type="filepath",
                    autoplay=True,
                    interactive=True
                )
        
        gr.Markdown("---")
        gr.Markdown("### 📝 Text Preview (Read Along)")
        text_preview = gr.Textbox(
            label="What will be spoken",
            lines=10,
            interactive=False,
            placeholder="Click the button above to generate the voice report..."
        )
        
        # Connect the button
        voice_report_btn.click(
            fn=generate_voice_report,
            outputs=[voice_audio_output]
        )
        
        voice_report_btn.click(
            fn=get_text_preview,
            outputs=[text_preview]
        )
    
    return voice_report_btn, voice_audio_output, text_preview