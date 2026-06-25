# Voice Assistant

## Project Overview

This project was completed as part of the Oasis Infobyte Python Programming Internship.

The aim of this project is to create a basic Python voice assistant that can listen to voice commands, process simple instructions, and respond using voice output.

The assistant can perform simple tasks such as responding to greetings, telling the time and date, opening websites, searching the web, and closing safely when the user says exit.

## Features

The voice assistant can:

1. Listen to the user's voice command using the microphone.
2. Convert the user's speech into text.
3. Respond back using voice output.
4. Respond to greetings such as `hello`.
5. Tell the current time.
6. Tell the current date.
7. Open Google.
8. Open YouTube.
9. Open GitHub.
10. Search the web based on the user's query.
11. Provide a password safety tip.
12. Handle unclear voice input.
13. Exit safely when the user says `exit` or `stop`.

## Voice Commands

The assistant currently supports these voice commands:

```text
hello
time
date
open google
open youtube
open github
search for cyber security internships
search for python tutorials
password tip
exit
stop
```

The `search for` command can be used with different search terms.

Example:

```text
search for data analyst internships
```

## Tools and Technologies Used

* Python
* VS Code
* SpeechRecognition
* PyAudio
* Windows built-in speech system
* `datetime` module
* `webbrowser` module
* `subprocess` module
* `platform` module

## How the Project Works

The project works in four main steps:

1. The assistant starts and gives a voice greeting.
2. The microphone listens for the user's command.
3. The speech recognition library converts the spoken command into text.
4. The assistant checks the command and responds using voice output.

For example:

```text
User says: hello
Assistant replies: Hello Sam. How can I help you today?
```

## Installation

Install the required packages using:

```bash
py -m pip install SpeechRecognition pyaudio
```

## Example Output

```text
Assistant: Hello Sam. I am your Python voice assistant.
Assistant: You can say hello, time, date, open Google, open YouTube, open GitHub, search for something, or exit.

Listening...
You said: hello
Assistant: Hello Sam. How can I help you today?

Listening...
You said: time
Assistant: The current time is 10:45 AM
```

## Error Handling

The assistant includes basic error handling.

If the assistant does not understand the user's speech, it responds with:

```text
Sorry, I could not understand what you said.
```

If there is a connection issue with the speech recognition service, it responds with:

```text
Sorry, there was a problem connecting to the speech recognition service.
```

If the assistant does not hear anything within the listening time, it responds with:

```text
I did not hear anything. Please try again.
```

## Files Included

```text
Voice Assistant/
├── voice_assistant.py
├── README.md
└── Screenshots/
    └── voice-assistant-voice-command-running.png
```

## Screenshot Evidence

The `Screenshots` folder contains evidence of the voice assistant running in the terminal.

The screenshot shows the assistant listening, detecting voice commands, printing what the user said, and returning responses.

## What I Learned

Through this project, I learned how to:

* Use Python to build a basic voice assistant.
* Capture voice input through a microphone.
* Convert speech into text using speech recognition.
* Use voice output to make the assistant speak back.
* Use Python functions to organise a program.
* Use conditional statements to respond to different commands.
* Use the `datetime` module to get the current time and date.
* Use the `webbrowser` module to open websites and perform web searches.
* Add basic error handling for unclear speech and connection issues.
* Build a simple user interaction system without needing a graphical interface.

## Limitations

This is a beginner-level voice assistant, so it only understands predefined commands.

It does not use advanced natural language processing, email automation, reminders, weather APIs, or smart home integrations. Those features would belong to a more advanced version of the project.

## Conclusion

This project successfully implements a basic Python voice assistant that uses voice input and voice output.

The assistant can listen to commands, respond to the user, tell the time and date, open websites, search the web, and exit safely.

This project improved my understanding of Python modules, speech recognition, voice interaction, functions, loops, and error handling.

## Author

Chukwukaima Sam
