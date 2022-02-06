import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import smtplib


listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        hour >= 18 and hour < 24
        speak("Good Evening!")

    speak("I am cisco Sir. Please tell me how may I help you")



def talk(text):
    engine.say(text)
    engine.runAndWait()




def take_command():
    try:
        with sr.Microphone() as source:
            print("listening..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "Alexa" in command:
                command = command.replace('Alexa', '')
                print(command)


    except:
        pass
    return command


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 533)
    server.ehlo()
    server.starttls()
    server.login('golaaksh0@gmail.com', '8667610611')
    server.sendmail('golaaksh0@gmail.com', to, content)
    server.close()

def run_Alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        print(time)
        talk('current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have some work')
    elif 'are you single' in command:
        talk ('I am in a relationship with wifi, sorry')
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'thank you' in command:
        talk('i am hey always for you sir ..')
    elif 'bye' in command:
        talk('bye Akash sir , have a nice day ..')
    elif 'hello Alexa' in command:
        talk('Hello sir,may i help you sir ..')
        print(talk)
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        talk('sir , what should i search in google')
        cm = take_command().lower()
        webbrowser.open(f"{cm}")

    elif 'open stackoverflow' in command:
        webbrowser.open("stackoverflow.com")
    elif 'open facebook' in command:
        webbrowser.open("facebook")
    elif 'open instagram' in command:
        webbrowser.open("instagram")
    elif 'send' in command:
        talk("message send ")
        pywhatkit.sendwhatmsg("+91 9841535705", 'hello ', 0, 0)
    elif 'email to mummy' in command:
        try:
            talk("What should I say?")
            content = take_command().lower()
            to = "sanjanagola929@gmail.com"
            sendEmail(to, content)
            talk("Email has been sent!")
        except Exception as e:
            print(e)
            talk("Sorry sir. I am not able to send this email")
    else:
        talk('please say the command again..')

while True:
    run_Alexa()