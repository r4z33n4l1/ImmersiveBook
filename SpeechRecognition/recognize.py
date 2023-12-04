import speech_recognition as sr
import whisper
from SpeechRecognition.find_mic import list_microphones

def save_audio_to_file(audio_data, filename="voice.wav"):
    """
    Saves audio data to a WAV file.

    Args:
    audio_data: The audio data to save.
    filename (str): The filename to save the audio data to.
    """
    with open(filename, "wb") as f:
        f.write(audio_data.get_wav_data())

def load_whisper_model():
    """
    Loads the Whisper model.

    Returns:
    The loaded Whisper model or None if loading fails.
    """
    try:
        return whisper.load_model("base")
    except Exception as e:
        print(f"Failed to load Whisper model: {e}")
        return None

def capture_audio(mic_index):
    """
    Captures audio from the specified microphone.

    Args:
    mic_index (int): The index of the microphone to use.

    Returns:
    The captured audio data or None if capturing fails.
    """
    r = sr.Recognizer()
    with sr.Microphone(device_index=mic_index) as source:
        print("Say something!")
        try:
            return r.listen(source)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return None

def transcribe_audio(model, audio_data):
    """
    Transcribes audio data using the Whisper model.

    Args:
    model: The Whisper model to use for transcription.
    audio_data: The audio data to transcribe.

    Returns:
    The transcribed text or None if transcription fails.
    """
    try:
        save_audio_to_file(audio_data)
        return model.transcribe("voice.wav")["text"]
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return None


def transcribe_speech(mic_index=None):
    """
    Captures and transcribes speech from a microphone.

    Args:
    mic_index (int, optional): The index of the microphone to use.

    Returns:
    The transcribed text or None if an error occurs.
    """
    if mic_index is None:
        print("Available microphones:")
        list_microphones()
        mic_index = int(input("Enter the index of the microphone you want to use: "))

    model = load_whisper_model()
    if not model:
        return None

    audio = capture_audio(mic_index)
    if not audio:
        return None

    return transcribe_audio(model, audio)

# Main program execution
if __name__ == "__main__":
    transcription = transcribe_speech()
    if transcription:
        print("Transcription:")
        print(transcription)
    else:
        print("No transcription was produced.")
