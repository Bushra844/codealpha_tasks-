import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
try:
        audio = recognizer.listen(source)  # Captures your voice
        command = recognizer.recognize_google(audio)
        command = command.lower()  # Convert to lowercase for easy matching
        print("You said:", command)  # Print recognized text

        # Process commands
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")  # Get time in HH:MM AM/PM format
            print("Current time is:", current_time)

        elif "open google please" in command:
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")

        elif "exit" in command or "stop" in command:
            print("Goodbye!")
            exit()

try:
    # Speech recognition code here
except sr.UnknownValueError as e:
    print(f"Sorry, I couldn't understand what you said. Error: {e}")
except sr.RequestError as e:
    print(f"Could not connect to the speech recognition service. Error: {e}")
else:
    print("I did not understand that.")

