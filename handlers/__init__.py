# handlers/__init__.py - Handlers Package Initialization
# ====================================================================
# Exports all handler functions
# ====================================================================

from .consultation_handler import process_consultation
from .medication_handler import add_new_medication, refresh_medication_display, refresh_alerts
from .voice_report_handler import generate_voice_report, get_text_preview

__all__ = [
    'process_consultation',
    'add_new_medication',
    'refresh_medication_display', 
    'refresh_alerts',
    'generate_voice_report',
    'get_text_preview'
]