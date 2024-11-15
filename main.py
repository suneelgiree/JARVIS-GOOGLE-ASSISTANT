import speech_recognition as sr
import webbrowser
import pyttsx3
import sys

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

# Function to convert speech to text
def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

def main():
    speak("Initializing the JARVIS...")

    # Listen for the wake word "JARVIS"
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise once
        print("Listening... Say 'JARVIS' to wake me up.")
        
        while True:
            try:
                # Capture audio inside the 'with' statement block
                audio = recognizer.listen(source, timeout=5)  
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                print("You said: " + text)

                # Check if the user said "JARVIS"
                if 'JARVIS' in text.upper():
                    speak("JARVIS is activated. What can I help you with?")
                    print("JARVIS activated. Please say your query.")
                    
                    # Now listen for the actual query after "JARVIS"
                    audio = recognizer.listen(source, timeout=5)
                    query = recognizer.recognize_google(audio)
                    print(f"Query: {query}")
                    
                    # Check if the user said "exit" or "goodbye" to terminate the program
                    if 'exit' in query.lower() or 'goodbye' in query.lower():
                        speak("Goodbye. Shutting down now.")
                        print("Exiting the program.")
                        sys.exit()  # Exit the loop and end the program

                    if query:
                        speak("Yes, I am searching for that now.")
                        # Open Google Chrome and search for the user's query
                        webbrowser.open_new_tab("https://www.google.com/search?q=" + query)
                        speak("I've opened Google Chrome and searched for " + query)

                    else:
                        speak("I didn't catch that. Please repeat your query.")
                else:
                    print("Say 'JARVIS' to wake me up.")
            
            except sr.UnknownValueError:
                print("I couldn't understand you. Please try again.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except KeyboardInterrupt:
                print("Exiting the program.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()


    
