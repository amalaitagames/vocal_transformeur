import os

import whisper
import speech_recognition as sr

#model = whisper.load_model("turbo")
model = whisper.load_model("base")

r = sr.Recognizer()
microphone = sr.Microphone()

def record_text(i):

    while True:
        with microphone as source:
            print("You can speak now...")
            r.adjust_for_ambient_noise(source)
            input_audio = r.listen(source)
            return input_audio

def writeText(input_audio) :
    audio = whisper.load_audio(input_audio)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(result.text)
    if (result.text.__contains__("lire")):
        os.system("flatpak run org.videolan.VLC")

    return result.text

text_recorded = ""

def set_text_recorded(result):
    global text_recorded
    text_recorded = result

def get_text_recorded():
    return text_recorded

def record_and_translate(isRecording):
    i = 0
    while(isRecording):

        text = record_text(i)
        fileName = f"speech_text_{i}.wav"
        with open(fileName, "wb") as file:
            file.write(text.get_wav_data())
            file.close()
        text_rec = writeText(file.name)
        set_text_recorded(text_rec.text)
        i +=1
        print("\n")
        isRecording = False
        return text_rec
