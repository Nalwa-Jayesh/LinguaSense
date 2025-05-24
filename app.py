import os
from stt import record_audio, transcribe_audio
from retriever import Retriever
from generator import generate_response
from tts import text_to_speech
from pydub import AudioSegment
from pydub.playback import play

# Constants
DOCS_PATH = "documents"
AUDIO_INPUT = "input.wav"
AUDIO_OUTPUT = "audio_outputs/output.wav"

def main():
    # Step 1: Record user voice from mic
    record_audio(AUDIO_INPUT, record_seconds=6)

    # Step 2: Transcribe audio and detect language
    print("🔊 Transcribing input...")
    query_text, language = transcribe_audio(AUDIO_INPUT)
    print(f"📝 Query ({language}): {query_text}")

    # Step 3: Retrieve top-3 context chunks from documents
    retriever = Retriever(DOCS_PATH)
    retrieved_chunks = retriever.query(query_text, k=3)
    context = "\n\n".join(retrieved_chunks)

    # Step 4: Use Mistral LLM to generate a smart answer
    prompt = (
        f"You are a multilingual assistant for visually impaired users. "
        f"Answer the question clearly, briefly, and in plain language using the context. "
        f"Respond in the same language as the user's query, which is {language}.\n\n"
        f"Context:\n{context}\n\nUser: {query_text}\nAssistant:"
    )
    response_text = generate_response(prompt)
    print("📚 Answer:", response_text)

    # Step 5: Generate speech using multilingual TTS
    print("🗣️ Generating response...")
    text_to_speech(response_text, output_path=AUDIO_OUTPUT)

    # Step 6: Play back the response audio
    print("▶️ Playing response...")
    response_audio = AudioSegment.from_wav(AUDIO_OUTPUT)
    play(response_audio)

if __name__ == "__main__":
    main()