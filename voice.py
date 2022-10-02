import pyttsx3,datetime
import speech_recognition as sr
# from googletrans import Translator

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)


def speak(audio):
    # translater = Translator()
    # out = translater.translate(audio, dest='hi')
    # print(out)
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("How can I Help You?")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print("You Said : ",query)

    except Exception as e:
        print("Say that again please....")
        return 'None'

    return query


def directions(dir) :
    pass

def object(obj) : 
    pass


if __name__=="__main__":
    wish()
    #while True:
        #query=takeCommand().lower()
        # if
        # else : 
        #     print("Didn't recognized! Please say it again...")
        #     takeCommand()
