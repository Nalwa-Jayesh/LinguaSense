# LinguaSense 🎙️🧠

**LinguaSense** is a multilingual, voice-activated Retrieval-Augmented Generation (RAG) assistant. It enables users — including those with visual impairments — to speak a natural language query into the system, retrieve relevant information from local documents, and hear an AI-generated response aloud in their native language.

---

## 🚀 Features

- 🎤 **Live microphone input** with real-time speech capture
- 🗣️ **Multilingual speech-to-text** using Faster-Whisper (offline-capable)
- 📚 **Semantic search** using Hugging Face embeddings + FAISS
- 🤖 **Contextual response generation** with `google/gemma-7b-it` via Hugging Face Inference API
- 🔊 **Multilingual TTS** using Coqui TTS with automatic language detection
- 🧠 Modular, local-first architecture — easy to extend and customize

---

## 📁 Folder Structure

```
LinguaSense/
├── app.py                  # Main app orchestration
├── config.py               # API keys and model settings
├── recorder.py             # Microphone-based audio recorder
├── stt.py                  # Transcription via Faster-Whisper
├── retriever.py            # Embeds + searches document chunks
├── generator.py            # Uses Gemma LLM via HF API
├── tts.py                  # Text-to-speech via Coqui
├── requirements.txt
├── .env                    # Environment variables
├── documents/              # Knowledge base (.txt files)
├── audio_outputs/          # Output speech files
└── models/                 # STT model files (Faster-Whisper)
```

---

## 🔧 Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure `.env`

Create a `.env` file:

```env
HUGGINGFACE_API_KEY=your_hf_token
```

### 3. Download STT Model

Use `faster-whisper` to download a multilingual model (e.g., `small`, `base`, or `medium`).  
More info: https://github.com/guillaumekln/faster-whisper

Place it under `models/`.

---

## ▶️ Run the App

```bash
python app.py
```

You’ll be prompted to speak. The assistant will:
1. Record and transcribe your voice
2. Retrieve relevant text chunks from local documents
3. Use Gemma to generate a contextual answer
4. Speak the answer aloud

---

## 🧪 Example Queries

- "Who is Sherlock Holmes?"
- "Summarize Pride and Prejudice in a sentence."
- "What is accessibility in web design?"

---

## 🧠 Powered By

- **Faster-Whisper** – offline multilingual speech recognition
- **Hugging Face API** – semantic embeddings + LLM (Gemma)
- **FAISS** – fast similarity search over documents
- **Coqui TTS** – multilingual speech synthesis
- **Langdetect** – dynamic language detection

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

Developed as part of the **Flickdone AI Platform Developer Challenge** to showcase applied multilingual AI for accessibility.
