import json
import os

def load_word_counts(filename="book_page.json"):
    """
    Loads the word count data for books from a JSON file.

    Args:
    filename (str): The name of the JSON file containing the word count data.

    Returns:
    dict: A dictionary with book names as keys and their page-to-word count mappings as values.
    """
    try:
        # Construct the full file path relative to this script
        base_dir = os.path.dirname(__file__)
        full_path = os.path.join(base_dir, '..', 'storage', filename)

        with open(full_path, 'r') as file:
            word_counts = json.load(file)
        return word_counts
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' contains invalid JSON.")
        return {}

# Example usage
if __name__ == "__main__":
    word_counts = load_word_counts()
    print(word_counts)
