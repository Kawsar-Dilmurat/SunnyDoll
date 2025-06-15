import boto3
from gtts import gTTS
from playsound import playsound
import time

# Function: Use gTTS (Google Text-to-Speech) to synthesize and play voice
def run_gtts_demo():
    text = "Hello, I am your SunnyDoll assistant. How's your day going?"
    tts = gTTS(text=text, lang="en")
    tts.save("gtts_output.mp3")
    print("gTTS audio saved as gtts_output.mp3")
    playsound("gtts_output.mp3")
    time.sleep(3)

# Function: Use Amazon Polly with Ivy (female voice)
def run_polly_ivy_demo():
    polly = boto3.client('polly', region_name='us-east-1')
    response = polly.synthesize_speech(
        Text="Hello, I am Ivy, your SunnyDoll assistant. How's your day going?",
        OutputFormat="mp3",
        VoiceId="Ivy"
    )
    with open("polly_ivy.mp3", "wb") as file:
        file.write(response['AudioStream'].read())
    print("Amazon Polly audio saved as polly_ivy.mp3")
    playsound("polly_ivy.mp3")
    time.sleep(3)

# Function: Use Amazon Polly with Justin (male voice)
def run_polly_justin_demo():
    polly = boto3.client('polly', region_name='us-east-1')
    response = polly.synthesize_speech(
        Text="Hello, I am Justin, another voice option from SunnyDoll.",
        OutputFormat="mp3",
        VoiceId="Justin"
    )
    with open("polly_justin.mp3", "wb") as file:
        file.write(response['AudioStream'].read())
    print("Amazon Polly audio saved as polly_justin.mp3")
    playsound("polly_justin.mp3")
    time.sleep(3)

# Function: Use Amazon Polly with Chinese voice
def run_polly_chinese_demo():
    polly = boto3.client('polly', region_name='us-east-1')
    response = polly.synthesize_speech(
        Text="你好，我是你的 SunnyDoll 助手。今天过得怎么样？",
        OutputFormat="mp3",
        VoiceId="Zhiyu"  # Zhiyu is a Mandarin Chinese female voice
    )
    with open("polly_chinese.mp3", "wb") as file:
        file.write(response['AudioStream'].read())
    print("Amazon Polly audio saved as polly_chinese.mp3")
    playsound("polly_chinese.mp3")
    time.sleep(4)

# Main menu to choose demo
if __name__ == "__main__":
    print("Choose which TTS demo to run:")
    print("1 - gTTS (Google Text-to-Speech, English)")
    print("2 - Amazon Polly - Ivy (English, female)")
    print("3 - Amazon Polly - Justin (English, male)")
    print("4 - Amazon Polly - Zhiyu (Chinese, female)")

    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == "1":
        run_gtts_demo()
    elif choice == "2":
        run_polly_ivy_demo()
    elif choice == "3":
        run_polly_justin_demo()
    elif choice == "4":
        run_polly_chinese_demo()
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
