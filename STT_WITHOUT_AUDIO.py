import speech_recognition as sr
import sys

# Initialize the recognizer
r = sr.Recognizer()

# Set the language code for Kannada
language_code = ["kn-IN", "en-IN"]

"""
Hindi": "hi-IN",
    "Kannada": "kn-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Marathi": "mr-IN",
    "Gujarati": "gu-IN",
    "Malayalam": "ml-IN",
    "Bengali": "bn-IN",
    "Punjabi": "pa-IN",
    "Urdu": "ur-IN"
    """

# Counter for consecutive unknown errors
unknown_error_count = 0

# Maximum number of consecutive errors allowed
max_errors = 1

# Loop to continuously listen for input
while True:
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source2:
            print(f"Listening for input in Kannada (2 seconds timeout)...")

            # Adjust the energy threshold based on surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # Listen for the user's input with a 5-second timeout
            audio2 = r.listen(source2, timeout=2)

            # Using Google to recognize audio in Kannada
            MyText = r.recognize_google(audio2, language=language_code)
            MyText = MyText.lower()

            # Reset error counter on successful input
            unknown_error_count = 0

            print("Did you say (in Kannada):", MyText)

    except sr.WaitTimeoutError:
        print("No audio detected for 5 seconds. Exiting.")
        sys.exit()  # Exit the program if no input is detected within 5 seconds

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        sys.exit()  # Exit the program on API errors

    except sr.UnknownValueError:
        print("Could not understand the audio. Please try again.")
        unknown_error_count += 1

        # Exit if too many consecutive errors occur
        if unknown_error_count >= max_errors:
            print(f"Too many consecutive errors ({unknown_error_count}). Exiting.")
            sys.exit()
