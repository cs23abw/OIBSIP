import datetime
import webbrowser
import subprocess
import platform
import speech_recognition as sr


def speak(message):
    """
    This function prints the assistant response and speaks it out loud.
    On Windows, it uses the built-in Windows speech system.
    """
    print("Assistant:", message)

    if platform.system() == "Windows":
        safe_message = message.replace("'", "''")

        powershell_command = (
            "Add-Type -AssemblyName System.Speech; "
            f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{safe_message}')"
        )

        subprocess.run(
            ["powershell", "-Command", powershell_command],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    else:
        print("Voice output is currently set up for Windows.")


def listen_command():
    """
    This function listens to the user's voice command and converts it into text.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command

    except sr.UnknownValueError:
        speak("Sorry, I could not understand what you said.")
        return ""

    except sr.RequestError:
        speak("Sorry, there was a problem connecting to the speech recognition service.")
        return ""

    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please try again.")
        return ""

def run_assistant():
    speak("Hello Sam. I am your Python voice assistant.")
    speak("You can say hello, time, date, open Google, open YouTube, open GitHub, search for something, or exit.")

    while True:
        command = listen_command()

        if "hello" in command:
            speak("Hello Sam. How can I help you today?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
            speak(f"Today's date is {current_date}")

        elif "open google" in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif "open github" in command:
            speak("Opening GitHub.")
            webbrowser.open("https://github.com")

        elif "search for" in command:
            search_query = command.replace("search for", "").strip()

            if search_query:
                speak(f"Searching the web for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            else:
                speak("Please say what you want me to search for.")

        elif "password tip" in command:
            speak("Use strong passwords with uppercase letters, lowercase letters, numbers, and symbols.")

        elif "exit" in command or "stop" in command:
            speak("Goodbye. The assistant is now closing.")
            break

        elif command == "":
            continue

        else:
            speak("Sorry, I do not understand that command yet.")


run_assistant()