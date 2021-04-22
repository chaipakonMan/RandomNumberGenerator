# a simple random number generator using speech recognition
# speech_recognition to help with speech to text
# pyttsx3 to help with text to speech
# random to help do the actual RNG
import speech_recognition as sr 
import pyttsx3 
from random import randint

def driver():
    # print("In driver")
    r = sr.Recognizer()
    exit = False
    engine = pyttsx3.init()
    err = False
    lowLim = 0
    upLim = 0

    while not exit:

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            if not err:
                engine.say('Please say start to begin random number generator and stop to exit')
                engine.runAndWait()
            else:
                engine.say('sorry, I did not catch that. Please say start to start random number generator')
                engine.runAndWait()
                err = False
            
            audio = r.listen(source)
            
            try:
                input = r.recognize_google(audio)
                # print("Said: " + input)
                if "start" in input:
                    engine.say('Please say the lower limit')
                    engine.runAndWait()
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                        try:
                            lowLim = r.recognize_google(audio)
                            # print("Said: " + lowLim)
                        except Exception as e:
                            err = True
                    engine.say('Please say the upper limit')
                    engine.runAndWait()
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                        try:
                            upLim = r.recognize_google(audio)
                            # print("Said: " + upLim)
                        except Exception as e:
                            err = True
                    # print(lowLim + ' : ' + upLim)
                    res = randint(int(lowLim), int(upLim))
                    # print(res)
                    exit = True
                    engine.say('The number generated is ' + str(res))
                    engine.runAndWait()
                elif "stop" in input:
                    exit = True
                else :
                    err = True

            except Exception as e:
                err = True
    engine.say('goodbye')
    engine.runAndWait()

driver()
