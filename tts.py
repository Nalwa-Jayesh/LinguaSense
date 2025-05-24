import torch
from TTS.api import TTS
from langdetect import detect
from pydub import AudioSegment
import tempfile
import os

device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2").to(device)

def chunk_text(text, max_words=250):
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]

def text_to_speech(text, output_path="audio_outputs/output.wav"):
    speaker = "Craig Gutsy"
    language = detect(text)
    
    chunks = chunk_text(text, max_words=250)
    audio_segments = []

    for chunk in chunks:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
            temp_path = tmp_file.name
        tts.tts_to_file(text=chunk, speaker=speaker, language=language, file_path=temp_path)
        audio_segments.append(AudioSegment.from_wav(temp_path))
        os.remove(temp_path)

    combined_audio = audio_segments[0]
    for seg in audio_segments[1:]:
        combined_audio += seg
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    combined_audio.export(output_path, format="wav")