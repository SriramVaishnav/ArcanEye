from Gui import Ui_MainWindow
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import sys
import psutil
import webbrowser
import wikipedia
import pyjokes
import playsound
import os
import datetime
import pywhatkit
from pywikihow import search_wikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)


def Speak(Text):
    print("   ")
    print(f": {Text}")
    engine.say(Text)
    print("    ")
    engine.runAndWait()


class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def takecommand(self): 
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source,0,4)

        try:
            print("Recognizing..")
            query = r.recognize_google(audio,language="en-in")
            print(f"You Said : {query}")

        except:
            return ""

        query = str(query)
        return query.lower()

    def Task_Gui(self):

        Speak("Hello I Am arcane Sir")
        Speak("Welcome Back Sir")

        while True:

            self.query = self.takecommand()

            if 'hello' in self.query:
                Speak("Hello Sir , I Am arcane .")
                Speak("Your Personal AI Assistant!")
                Speak("How May I Help You?")

            elif 'no' in self.query:
                Speak("Ok Sir")

            elif 'how much power left' in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                Speak(f"Sir our system have {percentage} percentage battery left ")

            elif 'how are you' in self.query:
                Speak("I Am Fine Sir!")
                Speak("Whats About YOU?")

            elif 'you need a break' in self.query:
                Speak("Ok Sir , You Can Call Me Anytime !")
                Speak("Just Say Wake Up arcane!")
                break

            elif 'youtube search' in self.query:
                Speak("OK sir , This Is What I found For Your Search!")
                query = query.replace("arcane","")
                query = query.replace("youtube search","")
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(web)
                Speak("Done Sir!")

            elif 'website' in self.query:
                Speak("Ok Sir , Launching.....")
                query = query.replace("arcane","")
                query = query.replace("website","")
                query = query.replace(" ","")
                web1 = query.replace("open","")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                Speak("Launched!")

            elif 'maps' in self.query:
                web = 'https://www.google.co.in/maps?ucbcb=1'
                webbrowser.open(web)
                Speak("Done Sir!")
                
            elif 'chrome' in self.query:
                name= self.takecommand()
                query=os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
                Speak("opening chrome")
                
            # elif 'arcane'in self.query:
            #     name=self.takecommand()
            #     web="https://www.+name"
            #     webbrowser.open(web)
                
            elif 'wikipedia' in self.query:
                Speak("Searching Wikipedia.....")
                query = query.replace("arcane","")
                query = query.replace("wikipedia","")
                wiki = wikipedia.summary(query,2)
                Speak(f"According To Wikipedia : {wiki}")

            elif 'joke' in self.query:
                get = pyjokes.get_joke()
                Speak(get)

            elif 'repeat my word' in self.query:
                Speak("Speak Sir!")
                jj = self.takecommand()
                Speak(f"You Said : {jj}")

            elif 'alarm' in self.query:
                Speak("Enter The Time !")
                time = input(": Enter The Time :")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")

                    if now == time:
                        Speak("Time To Wake Up Sir!")
                        playsound('iron.mp3')
                        Speak("Alarm Closed!")

                    elif now>time:
                        break
            
            elif 'remember that' in self.query:
                remeberMsg = query.replace("remember that","")
                remeberMsg = remeberMsg.replace("arcane","")
                Speak("You Tell Me To Remind You That :"+remeberMsg)
                remeber = open('data.txt','w')
                remeber.write(remeberMsg)
                remeber.close()

            elif 'what do you remember' in self.query:
                remeber = open('data.txt','r')
                Speak("You Tell Me That" + remeber.read())

            elif 'google search' in self.query:
                import wikipedia as googleScrap
                query = query.replace("arcane","")
                query = query.replace("google search","")
                query = query.replace("google","")
                Speak("This Is What I Found On The Web!")
                pywhatkit.search(query)

                try:
                    result = googleScrap.summary(query,2)
                    Speak(result)

                except:
                    Speak("No Speakable Data Available!")

            elif 'how to' in self.query:
                Speak("Getting Data From The Internet !")
                op = query.replace("arcane","")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                Speak(how_to_func[0].summary)

startFunctions = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.arcane_ui = Ui_MainWindow()
        self.arcane_ui.setupUi(self)
        self.arcane_ui.pushButton.clicked.connect(self.close)
        self.arcane_ui.pushButton_2.clicked.connect(self.startFunc)

    def startFunc(self):

        self.arcane_ui.movies_2 = QtGui.QMovie("A:\Abhay\arcane with gui-20221001T054653Z-001\arcane with gui\voice.gif")
        self.arcane_ui.label_2.setMovie(self.arcane_ui.movies_2)
        self.arcane_ui.movies_2.start()


        self.arcane_ui.movies_6 = QtGui.QMovie("A:\Abhay\arcane with gui-20221001T054653Z-001\arcane with gui\initial.gif")
        self.arcane_ui.label_6.setMovie(self.arcane_ui.movies_6)
        self.arcane_ui.movies_6.start()

        self.arcane_ui.movies_7 = QtGui.QMovie("A:\Abhay\arcane with gui-20221001T054653Z-001\arcane with gui\Hero_Template.gif")
        self.arcane_ui.label_7.setMovie(self.arcane_ui.movies_7)
        self.arcane_ui.movies_7.start()

        startFunctions.start()

Gui_App = QApplication(sys.argv)
Gui_arcane = Gui_Start()
Gui_arcane.show()
exit(Gui_App.exec_())