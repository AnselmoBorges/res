import openai
import tempfile
import os
import torch
from TTS.api import TTS
from dotenv import load_dotenv

# Carregando as variaveis de ambiente
load_dotenv()

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")

# Configure a chave de API
openai.api_key = os.getenv("OPENAI_API_KEY")
headers = {
    "Authorization": f"Bearer {openai.api_key}",
    "Content-Type": "application/json",
}

# Função para gerar o áudio da resposta e retorná-lo
# def gerar_audio_resposta(resposta):
#     tts_endpoint = "https://api.openai.com/v1/audio/speech"
#     data = {
#         "model": "tts-1",
#         "voice": "nova",
#         "input": resposta
#     }


def gerar_audio_resposta(resposta):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    with open(temp_file.name, "wb") as audio_file:
        audio_file.write(
            tts.tts_to_file(
                text=resposta,
                speaker_wav="SPEAKER_WAVE",
                language="pt",
                file_path=temp_file,
            )
        )

        return temp_file.name
