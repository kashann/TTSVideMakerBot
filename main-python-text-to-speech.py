import pyttsx3

def print_hi(name):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Select a natural sounding voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Adjust the speech rate to a natural pace (between 120-160)
    engine.setProperty('rate', 150)

    # Adjust the pitch to a natural range (between 0-100)
    engine.setProperty('pitch', 80)

    # Set a moderate volume level (between 0-1)
    engine.setProperty('volume', 0.7)

    # Convert a text string to speech
    text = "Hello, how are you doing today?"
    engine.say(text)
    engine.runAndWait()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
