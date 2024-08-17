# import openai
import tempfile
import os
from dotenv import load_dotenv
from TTS.api import TTS
import torch

# Carregando as variaveis de ambiente
load_dotenv()

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True).to("cuda")

# List available 🐸TTS models
print(TTS().list_models())


# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")


def gerar_audio_resposta(resposta):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    tts.tts_to_file(
        text=resposta,
        speaker_wav=os.getenv("SPEAKER_WAVE"),
        language="pt",
        file_path=temp_file.name,
    )
    return temp_file.name
