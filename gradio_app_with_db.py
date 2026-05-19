# gradio_app.py - Main Entry Point for Elderly Care Companion
# ====================================================================

import gradio as gr

# Import UI components
from tabs import (
    create_consultation_tab,
    create_medication_tab,
    create_appointments_tab,
    create_voice_report_tab
)

# Import services
from voice_assistant import cleanup_old_audio_files
from database import create_tables, add_sample_data

# Import config
from config import CURRENT_USER_ID


# ============================================
# INITIALIZE DATABASE ON STARTUP
# ============================================

print("🔧 Initializing database...")
create_tables()
add_sample_data()
print("✅ Database ready!")

# Cleanup old audio files
cleanup_old_audio_files(max_files=20)


# ============================================
# CREATE THE GRADIO INTERFACE
# ============================================

with gr.Blocks(title="Elderly Care Companion", theme=gr.themes.Soft()) as app:
    
    # Header
    gr.Markdown("""
    # Elderly Care Companion
    ### Your AI-Powered Health Assistant with Voice, Vision & Medication Management
    """)
    
    # Create all tabs
    with gr.Tabs():
        create_consultation_tab()
        create_medication_tab()
        create_appointments_tab()
        create_voice_report_tab()
    
    # Footer
    gr.Markdown("""
    ---
    ### 📖 How to Use:
    1. **Consultation Tab**: Record your symptoms, upload an image, and get AI doctor advice
    2. **Medication Tab**: Add your medications with refill dates
    3. **Appointments Tab**: View your daily summary
    4. **Voice Report Tab**: ONE CLICK to hear your complete health status!
    """)


# ============================================
# LAUNCH THE APP
# ============================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 Starting Elderly Care Companion...")
    print("="*60)
    print(f"👤 Current User ID: {CURRENT_USER_ID} (John Doe)")
    print("🌐 Open your browser to: http://127.0.0.1:7860")
    print("🎙️ Voice Report tab - One click to hear complete health status!")
    print("="*60 + "\n")
    
    app.launch(debug=True)