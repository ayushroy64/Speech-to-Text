import speech_recognition as SRG
import time

store = SRG.Recognizer()
with SRG.Microphone() as s:
    print("Listening...")
    audio_input = store.record(s,duration=7)
    print("Recording time: ", time.strftime("%I:%M:%S"))

    try:
        text_output = store.recognize_google(audio_input)
        print("")
        print("")
        print("---Audio converted to Text---")
        print("")
        print(text_output)
        print("")
        print("---End of Transmission---")
        print("Execution Time: ", time.strftime("%I:%M:%S"))
        time.sleep(10)
    except:
        print("Unable to process. Error")
