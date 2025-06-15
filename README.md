# SunnyDoll Voice Demo Suite

This project demonstrates how to integrate Text-to-Speech (TTS) and Automatic Speech Recognition (ASR) using various tools like Google gTTS, Amazon Polly, and OpenAI's Whisper. It's designed as a backend prototype for the SunnyDoll AI assistant.

## Features

- 🎙️ Text-to-speech using:
  - Google gTTS
  - Amazon Polly (multiple voices including English and Mandarin)
- 🧠 Speech-to-text using Whisper
- 🔁 Combined demo options for TTS exploration
- 🗂️ Scripted audio input and transcription storage

## Repository Structure

```bash
.
├── tts.py                             # Text-to-speech with Google gTTS
├── transcribe.py                      # Audio transcription with Whisper
├── polly_demo.py                      # Simple Amazon Polly voice synthesis
├── combined_tts_with_options.py       # Interactive TTS menu (gTTS and Polly)
├── combined_tts_demo_default_polly.py # Default Polly-based demo
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/SunnyDoll.git
cd SunnyDoll
```

### 2. Install Requirements
```bash
pip install gTTS boto3 playsound openai-whisper
```

Also, ensure you have ffmpeg installed and available in your system path (for Whisper).

### 3. Configure AWS Credentials
Run the following to set up access for Amazon Polly:

```bash
aws configure
```

You must provide:
- Access key ID
- Secret access key
- Region (e.g., `us-east-1`)

### 4. Run Demos

#### gTTS demo:
```bash
python tts.py
```

#### Polly demo:
```bash
python polly_demo.py
```

#### Transcription (ASR):
```bash
python transcribe.py
```

#### Interactive demo:
```bash
python combined_tts_with_options.py
```

## Notes

- Ensure your audio files (e.g., `sample.mp3`) are placed in the correct directory when running `transcribe.py`.
- For ASR, Whisper's `medium` model is used by default for balanced speed and accuracy.

## License

MIT License. For educational and research purposes.
