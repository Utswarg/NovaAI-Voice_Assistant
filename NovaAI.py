import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""  
        except sr.RequestError:
            print("Sorry, there is an issue with the speech recognition service.")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 200)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
        
        speech_input = sptext().lower()

        if "hey nova" in speech_input:
            df="Hi, How can i help you"
            speechtx(df)
            while True:
                data1 = sptext().lower()
                
                if "your name" in data1:
                    name = "You can call me nova."
                    speechtx(name)
                
                elif "how old are you" in data1:
                    age = "I am 2 years old."
                    speechtx(age)
                
                elif "my girlfriend" in data1:
                    gfnote="Of course, Jellybean is the sparkle in your world and the smile in your heart."
                    speechtx(gfnote)

                elif "her name" in data1:
                    gfnote1="I don’t know her real name, but I know your heart calls her Jellybean, and thats just perfect."
                    speechtx(gfnote1)

                elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I:%M %p")
                    speechtx(time)

                elif 'youtube' in data1:
                    webbrowser.open("https://www.youtube.com")

                elif 'wikipedia' in data1:
                    webbrowser.open("https://www.wikipedia.org")

                elif 'news' in data1:
                    note = "Till now, I don't have this update, but you can check in Times of India."
                    speechtx(note)
                    webbrowser.open("https://timesofindia.indiatimes.com")

                elif "joke" in data1:
                    joke_1 = pyjokes.get_joke(language="en", category="neutral")
                    speechtx(joke_1)

                elif "exit" in data1:
                    speechtx("Thank you!")
                    break
        else:
            print("Thanks")