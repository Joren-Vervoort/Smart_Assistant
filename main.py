import speech_recognition as sr #Module used to recognize spoken language
import pyttsx3 #Module used to let your code talk
import pywhatkit #Module used to interact with Youtube, Whatsapp
import datetime #Module used for time and dates
import wikipedia #Module used to interact with Wikipedia

#Initalizing the recognistion and talk modules
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    
    """
    Function used to let your computer say a certain given text.
    """
    
    engine.say(text) 
    engine.runAndWait()

def take_command():
    
    """
    
    This function needs to be activated by using a certain trigger word.
    
    When the trigger word recognized, this function is used to activate 
    your computer microphone to listen, recognize what is being said and 
    restate the command without the trigger word.
    
    """

    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print("Given command:",command)
    except:
        pass
    return command

def run_alexa():
    
    """
    
    Function that performs certain tasks and/or gives back certain reactions
    when a certain word is mentioned inside the command, given after the 
    trigger word.
    
    """

    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song) #play on youtube
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') #select the current time
        print(time)
        talk('The current time is' + time)
    elif 'who is' in command: 
        search = command.replace('who is', '')
        info = wikipedia.summary(search, 1) #selects the first two lines of wikipedia about a subject
        print(info)
        talk(info)
    elif 'last words' in command:
        talk('Thank you for listening, are there any questions?')
    elif 'introduce yourself' in command:
        talk('Hi, my name is Alexa. I\'m a smart assistant, designed by Joren Vervoort. Some day, I want to be a real boy.')
    else:
        talk("Can you repeat the command please?")
    

while True: #This keeps Alexa listening after a command is executed.
    run_alexa()