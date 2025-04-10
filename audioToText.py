import os
import subprocess
import whisper
import speech_recognition as sr

# r = sr.Recognizer()
# microphone = sr.Microphone()
#model = whisper.load_model("turbo")
model = whisper.load_model("base")


def writeText(source) :
    audio = whisper.load_audio(source)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    return result.text

def open_file_in_editor(cmd_texte):
    file_name = cmd_texte.replace('Ouvre le fichier, ', '')
    file_path = f"downloads/text_exports/{file_name}".strip()
    print(file_path)
    subprocess.call(["gnome-text-editor", file_path])
