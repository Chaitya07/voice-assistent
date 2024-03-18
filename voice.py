import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen to user's voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio).lower()
        print("You said:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your voice.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# Function to speak out response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop for the voice assistant
def main():
    while True:
        user_input = listen()
        if user_input:
            if "hello" in user_input:
                speak("Hello! How can I assist you?")
            elif "bye" in user_input:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I'm still learning. Can you repeat that?")
                
if __name__ == "__main__":
    main()
