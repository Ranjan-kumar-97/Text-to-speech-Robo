import pyttsx3


def text_to_speech():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    name = input("Please enter your name: ")
    engine.setProperty("voice", voices[0].id)
    welcome_sound = ("Welcome", name , "i am RoboSpeaker version 1 here, to covert you text into speech")
    engine.say(welcome_sound)
    engine.runAndWait()

    while True:
        word_to_convert = input("Enter what you want me to speak or Q to quit:  ")
        if word_to_convert == "q" or word_to_convert == "Q":
            bye_sound = ("Pleasure surving you",name, "Bye Bye")
            engine.say(bye_sound)
            engine.runAndWait()
            break
        engine.say(word_to_convert)
        engine.runAndWait()
    


text_to_speech()