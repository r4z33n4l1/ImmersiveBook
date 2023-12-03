import time

def calculate_reading_speed():
    """
    Calculates the user's reading speed in words per minute (WPM).

    The function presents a sample text for the user to read, measures the time taken to read,
    and calculates the reading speed based on the word count of the sample text.

    Returns:
    float: The calculated reading speed in words per minute.
    """
    # Sample text for the user to read
    sample_text = (
        "Alice was beginning to get very tired of sitting by her sister on the bank, "
        "and of having nothing to do: once or twice she had peeped into the book her sister was reading, "
        "but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice "
        "'without pictures or conversation?'"
    )
    word_count = len(sample_text.split())

    # Instruct the user
    print("You will now read a passage to determine your reading speed.")
    print("Press Enter when you are ready to start reading.")
    input()  # Wait for user to press Enter

    # Start timing
    start_time = time.time()

    # Display the passage for the user to read
    print(sample_text)
    input()  # Wait for user to press Enter

    # End timing
    end_time = time.time()

    # Calculate reading time in minutes
    reading_time_minutes = (end_time - start_time) / 60

    # Calculate words per minute
    wpm = word_count / reading_time_minutes

    return wpm

# Example usage
if __name__ == "__main__":
    average_wpm = calculate_reading_speed()
    print(f"Your average reading speed is {average_wpm:.2f} words per minute.")
