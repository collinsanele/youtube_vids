#The code is in the video description
import pyttsx3

def speak_text(text="I will speak this text", voice="male"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voice.lower() == "male":
        engine.setProperty('voice', voices[0].id)
    elif voice.lower() == "female":
        engine.setProperty('voice', voices[1].id)
    else:
        raise Exception("voice param must either be 'male' or 'female' ")
    engine.say(text)
    engine.runAndWait()

#run in the terminal with 'python text2speech.py'

if __name__ == "__main__":
    speak_text(text="Do not believe every coding video", voice="male")
