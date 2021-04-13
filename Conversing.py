import os
from gtts import gTTS
import playsound
import speech_recognition as sr
from google_trans_new import google_translator 
import pyaudio
import wave
import keyboard
import time

num = 1

translator = google_translator()


def speak_free(language="english"):
    r = sr.Recognizer()
    instruction = ""
    with sr.Microphone() as Source:
        assistant_talks("Adjusting", language)
        r.adjust_for_ambient_noise(Source)
        assistant_talks("Listening", language)
        spoken = r.listen(Source, phrase_time_limit=3.5)
        assistant_talks("Processing your speech", language)
        try:
            instruction = r.recognize_google(spoken)
            print(f"Human: {instruction}")
            # error occurs when google could not understand what was said
            instruction = translator.translate(instruction,  lang_tgt='en')
        except sr.UnknownValueError:
            assistant_talks("I could not understand what was spoken", language)
            return ""

        except sr.RequestError as e:
            print("There was some issue in understanding what was spoken; {0}".format(e), language)
            return ""
        return instruction


def speak_no_space(language="english"):
    r = sr.Recognizer()
    instruction_reduced = ""
    with sr.Microphone() as Source:
        assistant_talks("Wait", language)
        r.adjust_for_ambient_noise(Source)
        assistant_talks("Listening", language)
        spoken = r.listen(Source, phrase_time_limit=3.5)
        assistant_talks("Processing your speech", language)
        try:
            instruction_reduced = r.recognize_google(spoken).replace(" ", "")
            # error occurs when google could not understand what was said
            print(f"Human: {instruction_reduced}")
        except sr.UnknownValueError:
            assistant_talks("I could not understand what was spoken", language)

        except sr.RequestError as e:
            print("There was some issue in understanding what was spoken; {0}".format(e), language)

        return instruction_reduced


def assistant_talks(text, language="english", name=0):
    global num
    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1

    if "english" in language.lower():
        language = 'en'
    elif "hindi" in language.lower():
        language = "hi"
    if name == 0:
        result = translator.translate(text, lang_tgt=language)
        print("Assistant: ", result)
    else:
        print("Assistant: ", text)
    if language == 'en':
        language = 'en-uk'
    if not name == 0:
        toSpeak = gTTS(text=text, lang=language, slow=False, )
    else:
        toSpeak = gTTS(text=result, lang=language, slow=False, )
    # saving the audio file given by google text to speech
    file = "Op_temp_" + str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)


def record_notes(language):
    chunk = 1024
    formatting = pyaudio.paInt16
    channels = 1
    rate = 44100
    assistant_talks("What is the title of these notes?", language)
    title = speak_free(language)
    wave_output_filename = f'{title}.wav'
    p = pyaudio.PyAudio()

    stream = p.open(format=formatting,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    timeout = 60000

    frames = []

    start_time = time.time()
    current_time = time.time()
    assistant_talks('You may start dictating the notes now. Press "space" when you are done')

    while (current_time - start_time) < timeout:
        key = ""
        data = stream.read(chunk)
        frames.append(data)

        current_time = time.time()

        if keyboard.is_pressed('space'):
            key = 'space'

        if key == 'space':
            data = stream.read(chunk)
            frames.append(data)
            break

    else:
        data = stream.read(chunk)
        frames.append(data)

    stream.close()
    p.terminate()

    wf = wave.open(wave_output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(formatting))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
