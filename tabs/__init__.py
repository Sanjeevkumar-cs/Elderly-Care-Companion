# tabs/__init__.py - Tabs Package Initialization
# ====================================================================
# Exports all tab creation functions
# ====================================================================

from .consultation_tab import create_consultation_tab
from .medication_tab import create_medication_tab
from .appointments_tab import create_appointments_tab
from .voice_report_tab import create_voice_report_tab

__all__ = [
    'create_consultation_tab',
    'create_medication_tab', 
    'create_appointments_tab',
    'create_voice_report_tab'
]