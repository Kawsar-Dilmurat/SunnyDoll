import boto3
from gtts import gTTS
from playsound import playsound

# Function: Use gTTS (Google Text-to-Speech) to synthesize and play voice
def run_gtts_demo():
    text = "Hello, I am your SunnyDoll assistant. How's your day going?"
    tts = gTTS(text=text, lang="en")
    tts.save("gtts_output.mp3")
    print("gTTS audio saved as gtts_output.mp3")
    playsound("gtts_output.mp3")

# Function: Use Amazon Polly to synthesize and play voice
def run_polly_demo():
    polly = boto3.client('polly', region_name='us-east-1')
    response = polly.synthesize_speech(
        Text="Hello, I am Ivy, your SunnyDoll assistant. How's your day going?",
        OutputFormat="mp3",
        VoiceId="Ivy"
    )
    with open("polly_output.mp3", "wb") as file:
        file.write(response['AudioStream'].read())
    print("Amazon Polly audio saved as polly_output.mp3")
    playsound("polly_output.mp3")

# Directly use Amazon Polly by default
if __name__ == "__main__":
    print("Running demo using Amazon Polly...")
    run_polly_demo()
