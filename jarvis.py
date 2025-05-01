import pyttsx3  # type: ignore
import speech_recognition as sr  # type: ignore
import datetime
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set Male voice

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Wish the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis, sir. Please tell me how may I help you.")

def takeCommand():
    """Takes microphone input from the user and returns string output."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.WaitTimeoutError:
            print("Timeout. No speech detected.")
            return "None"
        except sr.UnknownValueError:
            print("Sorry, could not recognize.")
            return "None"
        except sr.RequestError:
            print("Network error.")
            return "None"
    return query

def play_movie_with_default_player(movie_path):
    """Play the movie using the default media player installed on the system."""
    try:
        if os.path.exists(movie_path):
            os.startfile(movie_path)
            speak("Playing the movie using your default media player.")
        else:
            speak("Movie file not found.")
    except Exception as e:
        print(f"Error playing movie: {e}")
        speak("Sorry, I could not play the movie.")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Wikipedia search
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=15)  # Bigger summary
                speak("According to Wikipedia...")
                print(results)
                speak(results)

                # Open full Wikipedia page in Chrome
                try:
                    webbrowser.get(using='chrome').open(f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}")
                except:
                    webbrowser.open(f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}")
                speak("I have opened the full Wikipedia page in Chrome for you.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, no page found on Wikipedia for your request.")
            except wikipedia.exceptions.DisambiguationError as e:
                options = e.options[:5]
                speak(f"Multiple results found. For example: {', '.join(options)}. Please be more specific.")
            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, I encountered a problem while searching Wikipedia.")

        # Play music
        elif 'play music' in query:
            music_path = r"C:\Users\azamm\Music\All-The-Stars-Kendrick-Lamar-SZA-(TopGhanaMusic.Com).mp3"
            if os.path.exists(music_path):
                os.startfile(music_path)
                speak("Playing All The Stars by Kendrick Lamar and SZA.")
            else:
                speak("Sorry, the music file was not found.")

        # Open Chrome and Play a Video
        elif 'play video' in query:
            speak("What video should I search?")
            video_query = takeCommand().lower()
            if video_query != "None":
                webbrowser.open(f"https://www.youtube.com/results?search_query={video_query}")
                speak(f"Playing {video_query} on YouTube.")
            else:
                speak("Sorry, I didn't catch the video name.")

        # Open Instagram
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
            speak("Opening Instagram")

        # Open GitHub
        elif 'open github' in query:
            webbrowser.open("https://github.com/")
            speak("Opening GitHub")

        # Open WhatsApp from Installed Application
        elif 'open whatsapp' in query:
            whatsapp_path = r"C:\Users\azamm\AppData\Local\WhatsApp\WhatsApp.exe"  # <- Update this path if needed
            try:
                if os.path.exists(whatsapp_path):
                    os.startfile(whatsapp_path)
                    speak("Opening WhatsApp application.")
                else:
                    speak("WhatsApp application not found on your system.")
            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, could not open WhatsApp application.")

        # Shutdown PC
        elif 'shutdown' in query:
            speak("Are you sure you want to shutdown the computer? Please say yes or no.")
            confirm = takeCommand().lower()
            if 'yes' in confirm:
                speak("Shutting down the system.")
                os.system('shutdown /s /t 5')
            else:
                speak("Shutdown canceled.")

        # Restart PC
        elif 'restart' in query:
            speak("Are you sure you want to restart the computer? Please say yes or no.")
            confirm = takeCommand().lower()
            if 'yes' in confirm:
                speak("Restarting the system.")
                os.system('shutdown /r /t 5')
            else:
                speak("Restart canceled.")

        # Play specific movie
        elif 'play movie' in query:
            movie_path = r"C:\Users\azamm\Downloads\www.CineVez.io - Pushpa 2 The Rule Reloaded (2024) 1080p Telugu TRUE WEB-DL - AVC - (DD+5.1 - 640kbps  & AAC) - 4.8GB.mkv"
            play_movie_with_default_player(movie_path)

        # Stop (but continue listening)
        elif 'stop' in query:
            speak("Okay, I will pause for now. You can tell me the next command.")
            continue  # Continue listening for next command

        # Exit the assistant
        elif 'exit' in query or 'bye' in query:
            speak("Goodbye sir! Have a nice day.")
            break






