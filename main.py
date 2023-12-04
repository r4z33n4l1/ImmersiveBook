from SpeechRecognition.recognize import transcribe_speech
from utils.find_music import find_audio_for_page
from utils.get_wordcount import load_word_counts
from utils.get_readingspeed import calculate_reading_speed
from just_playback import Playback
from word2number import w2n
import os
import time

MIC_INDEX = 2

def get_book_and_page():
    """
    Captures and processes speech to extract book name and page number.

    Returns:
    tuple: A tuple containing the book name and page number.
    """
    result = transcribe_speech(mic_index=MIC_INDEX).rstrip('.').lower()
    print("Detected Sentence: ", result)
    words = result.split()
    words[-1] = w2n.word_to_num(words[-1]) if words[-1].isalpha() else words[-1]
    book_name = ' '.join(words[:-1])
    page_number = int(words[-1])
    print(f"Book Name: {book_name}, Page Number: {page_number}")
    return book_name, page_number

def handle_playback_commands(playback, current_page):
    """
    Handles playback commands like play, pause, next, and stop.

    Args:
    playback: The Playback object for audio control.
    current_page (int): The current page number being read.

    Returns:
    bool: True if the program should continue, False if it should stop.
    """
    command = transcribe_speech(mic_index=MIC_INDEX).lower().strip()
    print(f"Command received: {command}")
    if "pause" in command:
        playback.pause()
        print(f"Paused at Page {current_page}")
    elif "play" in command:
        playback.resume()
        print(f"Resuming Page {current_page}")
    elif "next" in command:
        return True
    elif "stop" in command:
        playback.stop()
        print("Stopping playback and exiting program.")
        return False
    return True

def process_book_reading(book_name, start_page, word_counts, user_reading_speed):
    """
    Processes the book reading by playing audio for each page and handling user commands.

    Args:
    book_name (str): The name of the book being read.
    start_page (int): The starting page number.
    word_counts (dict): A dictionary containing word counts for each page of the book.
    user_reading_speed (float): The user's reading speed in words per minute.
    """
    current_page = start_page
    last_page = max(map(int, word_counts.get(book_name, {}).keys()))
    playback = Playback()

    while current_page <= last_page:
        audio_file = find_audio_for_page(book_name, current_page)
        if audio_file:
            audio_file_path = os.path.join('storage/music_files', audio_file)
            playback.load_file(audio_file_path)
            playback.play()
            print(f"Playing Page {current_page} of {last_page}")

        time_to_read = (word_counts.get(book_name, {}).get(str(current_page), 0) / user_reading_speed) * 60
        print(f"Time to read: {time_to_read:.2f} seconds")
        start_time = time.time()
        elapsed_time = 0

        while elapsed_time < time_to_read:
            if playback.active:
                command = transcribe_speech(mic_index=MIC_INDEX).lower().strip()
                print(f"Command received: {command}")
                if "pause" in command:
                    playback.pause()
                    pause_start_time = time.time()
                    print(f"Paused at Page {current_page}")
                elif "play" in command:
                    playback.resume()
                    elapsed_time += time.time() - pause_start_time  # Update elapsed time
                    print(f"Resuming Page {current_page}")
                elif "next" in command:
                    break
                elif "stop" in command:
                    playback.stop()
                    print("Stopping playback and exiting program.")
                    return  # Terminate the entire program

            time.sleep(1)  # Wait for a second before checking again
            elapsed_time = time.time() - start_time

        current_page += 1
    playback.stop()
    print("End of the book reached.")

if __name__ == "__main__":
    word_counts = load_word_counts()
    book_name, start_page = get_book_and_page()
    user_reading_speed = calculate_reading_speed()
    process_book_reading(book_name, start_page, word_counts, user_reading_speed)
