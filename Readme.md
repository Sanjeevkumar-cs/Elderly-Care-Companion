Elderly Care Companion

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-4.x-orange.svg)](https://gradio.app/)
[![Groq](https://img.shields.io/badge/Groq-API-purple.svg)](https://groq.com/)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-blue.svg)](https://elevenlabs.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **An AI-Powered Health Assistant for Elderly Care with Voice, Vision & Medication Management**

---

## 📖 Table of Contents

- [ Features](#features)
- [ Project Structure](#project-structure)
- [ Configuration](#configuration)
- [ Usage Guide](#usage-guide)
- [ Database Schema](#database-schema)
- [ Tech Stack](#tech-stack)
- [ Troubleshooting](#troubleshooting)
- [ Roadmap](#roadmap)
- [ Disclaimer](#disclaimer)
- [ License](#license)
- [ Acknowledgments](#acknowledgments)
- [ Contact](#contact)

---

## Features

| Feature                | Description                             | Status |
| ---------------------- | --------------------------------------- | ------ |
| 🎤 Voice Input         | Record symptoms using microphone        | ✅     |
| 🖼️ Image Analysis      | Upload skin/rash images for AI analysis | ✅     |
| 🩺 AI Doctor           | Llama 4 provides medical insights       | ✅     |
| 🔊 Doctor Voice        | ElevenLabs realistic voice response     | ✅     |
| 💊 Medication Tracking | Add, edit, delete medications           | ✅     |
| ⚠️ Refill Alerts       | Smart alerts for low stock & overdue    | ✅     |
| 📅 Daily Summary       | Today's medications & appointments      | ✅     |
| 🎙️ Voice Health Report | One-click complete health status        | ✅     |
| 💾 Persistent Storage  | SQLite database                         | ✅     |

---

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/AI-Doctor-with-Vision-and-Voice.git
cd AI-Doctor-with-Vision-and-Voice

# Install dependencies
pip install groq gradio speechrecognition pydub gtts elevenlabs python-dotenv

# Or use pipenv
pip install pipenv
pipenv install
pipenv shell
```

---

### Configuration

Create a `.env` file in the root directory:

```env
GROQ_API_KEY="your_groq_api_key_here"
ELEVENLABS_API_KEY="your_elevenlabs_api_key_here"
```

### Run the App

```bash
python gradio_app_with_db.py
```

Open your browser to: `http://127.0.0.1:7860`

---

## Project Structure

```
AI-Doctor-with-Vision-and-Voice/
│
├── 📁 database/              # Database package (6 tables)
├── 📁 handlers/              # Business logic
├── 📁 tabs/                  # UI components
├── 📁 audio_cache/           # Generated voice files
│
├── 📄 gradio_app_with_db.py  # MAIN ENTRY POINT
├── 📄 config.py              # Configuration
├── 📄 voice_assistant.py     # gTTS voice functions
│
├── 📄 brain_of_the_doctor.py # AI vision & LLM
├── 📄 voice_of_the_patient.py # Speech-to-text
├── 📄 voice_of_the_doctor.py # Text-to-speech
│
└── 📄 .env                   # API keys (create this)
```

## Configuration

### `config.py` Settings

```python


# User Configuration
CURRENT_USER_ID = 1

# AI Models
DOCTOR_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
STT_MODEL = "whisper-large-v3"

# Voice Settings (slow=True is better for elderly)
VOICE_SPEED_SLOW = True
VOICE_LANGUAGE = "en"
```

## Usage Guide

### Tab 1: 🩺 AI Doctor Consultation

1. Click microphone → speak your symptoms
2. Upload image (optional - skin/rash photos)
3. Click "Get AI Doctor Advice"
4. Listen to voice response

### Tab 2: 💊 Medication Manager

1. Enter medication name, pill count, daily dosage
2. Add refill date: `YYYY-MM-DD` (e.g., `2026-06-15`)
3. Click "Add Medication"
4. Click "Refresh" to see updated list

### Tab 3: 📅 Appointments & Reminders

- View daily medication schedule
- Check refill alerts
- Track upcoming appointments

### Tab 4: 🔊 Voice Report

- **One click** to hear complete health status
- Audio plays automatically
- Text preview for reading along

---

## Database Schema

| Table                  | Description                                 |
| ---------------------- | ------------------------------------------- |
| `users`                | Patient information                         |
| `medications`          | Medications with pill counts & refill dates |
| `medication_schedule`  | Daily schedule & taken status               |
| `appointments`         | Doctor appointments                         |
| `conversation_history` | AI doctor interactions                      |
| `metrics`              | Adherence rates & analytics                 |

> View/edit database with [DB Browser for SQLite](https://sqlitebrowser.org/)

---

## Tech Stack

| Category             | Technology              |
| -------------------- | ----------------------- |
| **LLM**              | Groq (Llama 4)          |
| **Vision**           | Groq (Llama 4 Vision)   |
| **STT**              | Groq (Whisper-large-v3) |
| **TTS (Doctor)**     | ElevenLabs              |
| **TTS (Summary)**    | gTTS (Google)           |
| **UI**               | Gradio                  |
| **Database**         | SQLite                  |
| **Audio Processing** | pydub, ffmpeg           |

---

## Troubleshooting

| Issue                                | Solution                                       |
| ------------------------------------ | ---------------------------------------------- |
| `ImportError: cannot import name...` | Check `__init__.py` files have correct exports |
| `strptime() argument must be str`    | Run `python fix_database_dates.py`             |
| Voice not playing                    | Check speaker volume & browser autoplay        |
| 401 API error                        | Verify API keys in `.env` file                 |
| Database locked                      | Close DB Browser, restart app                  |

### Quick Fixes

```bash
# Fix database date issues
python fix_database_dates.py

# Clear pipenv cache
pipenv --clear
pipenv install

# Run with debug
python gradio_app_with_db.py
```

---

## Roadmap

### Short-term

- [ ] Calendar date picker for refill dates
- [ ] Multi-language support (Hindi, regional)
- [ ] Export health reports as PDF
- [ ] Voice speed control slider

### Long-term

- [ ] Offline mode (local LLM with Ollama)
- [ ] IoT integration (smart pill dispensers)
- [ ] Caregiver dashboard
- [ ] Mobile app (React Native)

## Disclaimer

> **IMPORTANT: This project is for EDUCATIONAL PURPOSES ONLY**
>
> - ❌ NOT a certified medical device
> - ❌ NOT a replacement for professional medical advice
> - ❌ NOT approved for clinical diagnosis
>
> **Always consult a qualified healthcare professional for medical concerns.**

---

## License

MIT License - Free for educational and personal use.

## Acknowledgments

- [Groq](https://groq.com/) - LLM and STT APIs
- [ElevenLabs](https://elevenlabs.io/) - Text-to-speech
- [Google gTTS](https://gtts.readthedocs.io/) - Free voice synthesis
- [Gradio](https://gradio.app/) - Web interface
- [SQLite](https://sqlite.org/) - Database

---

## Contact

Open an issue on GitHub for questions or contributions.

---

**Made with ❤️ for elderly care** | [Report Bug](https://github.com/yourusername/AI-Doctor-with-Vision-and-Voice/issues) | [Request Feature](https://github.com/yourusername/AI-Doctor-with-Vision-and-Voice/issues)
