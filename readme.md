# Voice Assistant for Visually Impaired Users

A voice assistant application designed to assist visually impaired users by recording audio, transcribing it, retrieving relevant context, generating a response using a language model, and converting the response to speech.

## Features

- **Multilingual Support**: Handles queries in multiple languages.
- **Voice Recording**: Records audio input from the user.
- **Speech-to-Text**: Transcribes audio to text and detects the language.
- **Context Retrieval**: Retrieves relevant context from documents.
- **Text-to-Speech**: Converts generated responses to speech.

## Pipeline Design

The pipeline consists of several modular components that work together to process user queries and generate responses. The flow of the pipeline is as follows:

1. **Audio Recording**
2. **Speech-to-Text**
3. **Context Retrieval**
4. **Response Generation**
5. **Text-to-Speech**
6. **Audio Playback**

## Tools Used

### Audio Recording

- **Tool**: Python `sounddevice` library
- **Description**: Captures audio input from the user via microphone and saves it to a file for further processing.

### Speech-to-Text

- **Tool**: `faster-whisper`
- **Description**: A faster implementation of OpenAI's Whisper model for speech recognition. Used for transcribing audio to text.

### Context Retrieval

- **Tool**: `sentence-transformers`, `faiss-cpu`
- **Description**: Searches through a set of documents to retrieve relevant context based on the transcribed query. Uses a retriever mechanism to fetch top context chunks.

### Response Generation

- **Tool**: Hugging Face `transformers`
- **Description**: Utilizes a language model to generate a response based on the retrieved context and the user's query. Supports multilingual responses to cater to the user's language.

### Text-to-Speech

- **Tool**: `coqui-tts`
- **Description**: Converts the generated text response into speech. Supports multiple languages for speech output.

### Audio Playback

- **Tool**: Python `pydub` library
- **Description**: Plays back the generated speech response to the user.

## Retrieval/Generation Logic

### Retrieval Logic

1. **Input**: Transcribed text from the Speech-to-Text module.
2. **Process**:
   - The retriever module searches through a predefined set of documents.
   - It uses keyword matching or semantic search to find the most relevant context chunks.
   - The top `k` context chunks are retrieved and passed to the Response Generation module.
3. **Output**: Relevant context chunks.

### Generation Logic

1. **Input**: Retrieved context chunks and the user's transcribed query.
2. **Process**:
   - The language model generates a response based on the retrieved context and the user's query.
   - The prompt includes instructions to respond in the same language as the user's query.
   - The model generates a clear, brief, and plain language response.
3. **Output**: Generated text response.

### Text-to-Speech Logic

1. **Input**: Generated text response.
2. **Process**:
   - The TTS module converts the text response into speech.
   - It uses language-specific models to ensure accurate pronunciation and intonation.
3. **Output**: Audio file with the speech response.

### Audio Playback Logic

1. **Input**: Audio file with the speech response.
2. **Process**:
   - The audio playback module plays the audio file to the user.
3. **Output**: Audio playback of the generated response.

## Requirements

To run the application, you need to install the following Python packages:

- `faster-whisper`: For speech recognition.
- `sounddevice`: For recording and playing audio.
- `scipy`: For scientific and technical computing.
- `faiss-cpu`: For efficient similarity search and clustering.
- `numpy`: For numerical operations.
- `langdetect`: For language detection.
- `coqui-tts`: For text-to-speech conversion.
- `pyaudio`: For audio I/O operations.
- `sentence-transformers`: For generating sentence embeddings.
- `pydub`: For audio processing.
- `fugashi`: For Japanese tokenization.
- `cutlet`: For Japanese text processing.
- `mecab-python3`: For Japanese morphological analysis.
- `unidic-lite`: A lightweight Japanese dictionary for MeCab.
- `transformers`: For using pre-trained language models.

You can install these dependencies using pip:

```sh
pip install -r requirements.txt
```

## Installation

### Step 1: Clone the repository
```sh
git clone https://github.com/Nalwa-Jayesh/LinguaSense.git
cd LinguaSense
```