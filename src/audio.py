import pyttsx3
from concurrent.futures import ThreadPoolExecutor

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

executor = ThreadPoolExecutor(max_workers=1)


def _speak(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    # Since pyttsx3 is blocking, it causes a delay in the main thread.
    # Delay is noticeable, so we use a single-threaded executor to queue speech requests
    executor.submit(_speak, text)
