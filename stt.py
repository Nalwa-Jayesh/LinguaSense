import torch
import pyaudio
import wave
from faster_whisper import WhisperModel

# Choose appropriate model size for your GPU (GTX 1650): "small" is a good balance
MODEL_SIZE = "small"

# Initialize model with best device config
model = WhisperModel(
    MODEL_SIZE,
    device="cuda" if torch.cuda.is_available() else "cpu",
    compute_type="int8_float16" if torch.cuda.is_available() else "int8"
)

def record_audio(output_path="input.wav", record_seconds=6):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("🎙️ Recording...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("✅ Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(output_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe_audio(audio_path):
    segments, info = model.transcribe(audio_path, beam_size=5)
    text = " ".join([segment.text for segment in segments])
    return text.strip(), info.language