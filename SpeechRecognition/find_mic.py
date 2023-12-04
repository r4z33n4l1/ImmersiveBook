import speech_recognition as sr

def list_microphones():
    mic_list = sr.Microphone.list_microphone_names()
    for index, name in enumerate(mic_list):
        print(f"{index}: {name}")

if __name__ == '__main__':
    list_microphones()