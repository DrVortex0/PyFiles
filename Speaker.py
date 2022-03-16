import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('voice', '''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0''')
engine.say('Hello. You can realize the next operations.')
engine.runAndWait()

def calculator():
    engine = pyttsx3.init()
    engine.setProperty('voice', '''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0 ''')
    engine.say('Option One: Addition. Option two: Subtraction')
    engine.say('Option Three: multiplication. Option four: division')
    engine.say('Tell me the number of the option you want to calculate.')
    engine.runAndWait()
    try:
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            print('Speak Anything: ')
            audio = r.listen(source)
        try:
            op = int(r.recognize_google(audio))
            print('You said: {}'.format(int(op)))
        except:
            engine.say('Sorry could not hear')
    except ValueError:
            engine.say('I only allow numers.')
            engine.runAndWait()
    else:
        try:
            engine.say('Please, tell me your first number')
            engine.runAndWait()
            r = sr.Recognizer() 
            with sr.Microphone() as source:
                print('Speak Anything: ')
                audio = r.listen(source)
            try:
                x = int(r.recognize_google(audio))
                print('You said: {}'.format(int(x)))
            except:
                engine.say('Sorry could not hear')
                
            engine.say('Please, tell me your second number')
            engine.runAndWait()
            r = sr.Recognizer() 
            with sr.Microphone() as source:
                print('Speak Anything: ')
                audio = r.listen(source)
            try:
                y = int(r.recognize_google(audio))
                print('You said: {}'.format(int(y)))
            except:
                engine.say('Sorry could not hear')
        except ValueError:
            engine.say('I only allow numbers')
            engine.runAndWait()
        else:
            if op == 1:
                engine.say("The result is: " + str(x+y))
                engine.runAndWait()
                print('The result is: ', str(x+y))
            elif op == 2:
                engine.say("The result is: " + str(x-y))
                engine.runAndWait()
                print('The result is: ', str(x-y))
            elif op == 3:
                engine.say("The result is: " + str(x*y))
                engine.runAndWait()
                print('The result is: ', str(x*y))
            elif op == 4:
                if y == 0:
                    engine.say("Sorry, I can't do that.")
                    engine.runAndWait()
                else:
                    engine.say("The result is: " + str(x/y))
                    engine.runAndWait()
                    print('The result is: ', str(x/y))
            else:
                    engine.say("No valid option. Try again")
                    engine.runAndWait()       
def restart():
    engine = pyttsx3.init()
    engine.setProperty('voice', '''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0''')
    engine.say('Do you want calculate something else?')
    engine.runAndWait()
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print('Speak Anything: ')
        audio = r.listen(source)
    try:
        restart = r.recognize_google(audio)
        print('You said: {}'.format(restart))
    except:
        engine.say('Sorry could not hear')
    if restart == "yes" or restart == "Yes" or restart == "YES":
        calculator()
        restart()
    elif restart == "no" or restart == "No" or restart == "NO":
        engine.say('Have a nice day!')
        engine.runAndWait()
    else:
        restart()  
        
calculator()
restart()