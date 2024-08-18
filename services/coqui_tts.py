from TTS.api import TTS
import torch

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
