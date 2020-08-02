import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Something : ')
    audio = rec.listen(source)

    try:
        text = rec.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print('Sorry could not recognize your voice')