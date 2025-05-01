# Jarvis-voice-assistant

Jarvis Voice Assistant is a Python-based virtual desktop assistant inspired by the fictional AI from Iron Man. It can perform a wide range of tasks using voice commands, such as searching Wikipedia, playing music, opening websites, controlling applications, and more.

✨ Features
✅ Greet user based on time of day
✅ Wikipedia search with summaries
✅ Play local music files
✅ Search and play videos on YouTube
✅ Open websites like Instagram, GitHub, Stack Overflow
✅ Launch WhatsApp desktop
✅ Shutdown or restart computer
✅ Play specific local movie files
✅ Voice interaction with natural English commands
✅ Extendable for new features and APIs

📸 Demo
Greet the user:
“Good Morning! I am Jarvis, sir. Please tell me how may I help you.”

Wikipedia search:
“Wikipedia Albert Einstein” → summary + opens Wikipedia page

Play music:
“Play music” → plays random or specified local song

Open apps/sites:
“Open Instagram”, “Open GitHub”, “Open WhatsApp”

Shutdown/restart:
“Shutdown”, “Restart”

🛠️ Technologies & Libraries
Python 3.8+

pyttsx3 — text-to-speech (offline)

SpeechRecognition — speech-to-text

Wikipedia — Wikipedia data fetch

webbrowser — open sites in browser

os — system-level commands

datetime — time and date handling

⚙️ System Requirements
OS: Windows 7 or above

RAM: 4 GB or more

Hard Drive: ~250 MB free

Processor: Intel Dual Core or better

Python: 3.8+

Visual Studio Code or similar IDE

🚀 Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/jarvis-voice-assistant.git
cd jarvis-voice-assistant
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/Scripts/activate  # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the assistant:

bash
Copy
Edit
python jarvis.py
🗂 Example Commands
Command	Action
Wikipedia Albert Einstein	Get summary and open page
Play music	Play random local song
Play video Despacito	Search and play on YouTube
Open Instagram	Open Instagram website
Shutdown	Shut down the computer (after confirm)
Restart	Restart the computer (after confirm)

🌍 Future Scope
Smart home integration (MQTT, IoT)

Mobile app with React Native

Weather forecasting and reminders

Multilingual support

Integration with AI chat (GPT) for conversation
