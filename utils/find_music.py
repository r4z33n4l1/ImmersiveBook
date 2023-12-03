import json
import os
import logging

def find_audio_for_page(book_name, page_number):
    """
    Finds the audio track for a given book and page number.

    Parameters:
    book_name (str): The name of the book.
    page_number (int): The page number to find the audio for.

    Returns:
    str: The audio file associated with the given page number, or None if not found.
    """
    try:
        # Validate parameters
        if not isinstance(book_name, str) or not isinstance(page_number, int):
            logging.error("Invalid book name or page number.")
            return None

        # Construct the path to the JSON file relative to this script
        json_file = os.path.join(os.path.dirname(__file__), '..', 'storage', 'book_music.json')

        # Load the book data from the JSON file
        with open(json_file, 'r') as file:
            books_data = json.load(file)

        # Search for the audio track
        for range_info in books_data.get(book_name, []):
            if range_info['start'] <= page_number <= range_info['end']:
                return range_info['audio']
        return None
    except FileNotFoundError:
        logging.error(f"The file {json_file} was not found.")
        return None
    except json.JSONDecodeError:
        logging.error(f"The file {json_file} is not a valid JSON file.")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    audio_file = find_audio_for_page("test", 5)
    if audio_file:
        print(f"Audio file for page: {audio_file}")
    else:
        print("Audio file not found.")
