import pyttsx3


def text_to_speech():
    v = input ("Please enter F for Female voice or M for male voice:  ").lower()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if v == 'm':
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)
    name = input("Please enter your name: ")
    welcome_sound = ("Welcome", name , "i am RoboSpeaker version 1 here, to covert you text into speech")
    engine.say(welcome_sound)
    engine.runAndWait()

    while True:
        word_to_convert = input("Enter what you want me to speak or Q to quit:  ")
        if word_to_convert == "q" or word_to_convert == "Q":
            bye_sound = ("Pleasure serving you",name, "Bye Bye")
            engine.say(bye_sound)
            engine.runAndWait()
            break
        engine.say(word_to_convert)
        engine.runAndWait()
    


text_to_speech()