import speech_recognition 

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something: ")
    audio = recognizer.listen(source) 

words = recognizer.recognize_google(audio, language = 'en') 
ll = True
if "hello" in words:
    print("hello to you to")
else:
    print("hello world")    

    