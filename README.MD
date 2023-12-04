# Book Audio Playback Application

## Description
This application provides an immersive reading experience by playing audio files corresponding to specific pages of a book. Users can control playback through voice commands, allowing them to pause, play, or skip to the next page. The application calculates the user's reading speed to synchronize audio playback with their reading pace.

**Note:** Currently, this application is only compatible with Windows operating systems.

## Setup and Installation

### Prerequisites
- Python 3.x
- Windows Operating System

### Creating a Virtual Environment
1. **Create a Virtual Environment:**
   Navigate to your project directory and run:
   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment:**

     ```bash
     .\venv\Scripts\activate
     ```

### Installing Dependencies

Install all required packages using the following command:

```bash
pip install -r requirements.txt
```

## Configuration

### Finding Your Microphone Index

1. Run the following script to list all available microphones:
   ```bash
   python SpeechRecognition\list_microphones.py
   ```

2. Identify the index of the microphone you intend to use. Ensure that this microphone does not pick up the playback audio to avoid feedback issues.
in `main.py`, set the `MIC_INDEX` variable to the index of your microphone.

## Usage

To start the application, run the `main.py` script:

```bash
python main.py
```

Follow the on-screen instructions to interact with the application. You can control the audio playback of your chosen book using voice commands.

## Voice Commands

- **Pause:** Temporarily halts the audio playback.
- **Play:** Resumes the audio playback from where it was paused.
- **Next:** Skips to the audio of the next page.
- **Stop:** Stops the audio playback and exits the program.


## Adding a New Book
Make changes to files inside `storage/` to add a new book to the application.