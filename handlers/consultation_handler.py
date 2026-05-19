# handlers/consultation_handler.py - AI Doctor Consultation Logic
# ====================================================================
# Handles voice and image processing for AI doctor consultation
# ====================================================================

import os
import sys
import traceback

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import CURRENT_USER_ID, SYSTEM_PROMPT, DOCTOR_MODEL, STT_MODEL
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs
from database import (
    save_conversation,
    get_daily_summary,
    get_refill_alerts,
    get_upcoming_appointments
)


def process_consultation(audio_filepath, image_filepath):
    """
    Process patient's voice and image, get AI doctor response,
    save to database, and return medication summary too!
    """
    
    # Step 1: Convert speech to text
    if audio_filepath and os.path.exists(audio_filepath):
        speech_to_text_output = transcribe_with_groq(
            model=STT_MODEL, 
            file_path=audio_filepath
        )
    else:
        speech_to_text_output = "No audio provided. Please record your symptoms."
    
    # Step 2: Get AI doctor response
    if image_filepath and os.path.exists(image_filepath):
        try:
            doctor_response = analyze_image_with_query(
                query=SYSTEM_PROMPT + " " + speech_to_text_output, 
                encoded_image=encode_image(image_filepath), 
                model=DOCTOR_MODEL
            )
            image_analyzed = True
        except Exception as e:
            doctor_response = f"Error analyzing image: {str(e)}"
            image_analyzed = False
    else:
        doctor_response = "No image provided for me to analyze. Please describe your symptoms."
        image_analyzed = False
    
    # Step 3: Save conversation to database
    try:
        save_conversation(
            user_id=CURRENT_USER_ID,
            patient_question=speech_to_text_output,
            doctor_response=doctor_response,
            image_analyzed=image_analyzed
        )
    except Exception as e:
        print(f"Warning: Could not save conversation - {e}")
    
    # Step 4: Get medication summary and alerts
    try:
        medication_summary = get_daily_summary(CURRENT_USER_ID)
        refill_alerts = get_refill_alerts(CURRENT_USER_ID)
        upcoming_appointments = get_upcoming_appointments(CURRENT_USER_ID)
    except Exception as e:
        medication_summary = "Unable to load medication data"
        refill_alerts = "Unable to load alerts"
        upcoming_appointments = []
    
    # Format appointments
    appointments_text = "📅 **UPCOMING APPOINTMENTS**\n"
    if upcoming_appointments:
        for apt in upcoming_appointments:
            appointments_text += f"  • Dr. {apt['doctor_name']} on {apt['date']} at {apt['time']}\n"
    else:
        appointments_text += "  No upcoming appointments\n"
    
    # Combine all information
    full_response = f"""
🏥 **AI DOCTOR RESPONSE:**
{doctor_response}

---

{medication_summary}

---

{appointments_text}

---

{refill_alerts}
"""
    
    # Step 5: Convert doctor's response to speech
    output_audio_path = "final.mp3"
    
    if doctor_response and doctor_response != "No image provided for me to analyze. Please describe your symptoms.":
        try:
            print(f"🔊 Generating doctor voice...")
            text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath=output_audio_path)
            print(f"✅ Doctor voice generated")
        except Exception as e:
            print(f"⚠️ Voice generation failed: {e}")
            output_audio_path = None
    else:
        output_audio_path = None
    
    return speech_to_text_output, full_response, output_audio_path