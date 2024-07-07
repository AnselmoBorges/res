import openai
import requests
import tempfile
import os

# Configure a chave de API
openai.api_key = os.environ.get("OPENAI_API_KEY")
headers = {
    "Authorization": f"Bearer {openai.api_key}",
    "Content-Type": "application/json"
}

# Função para gerar o áudio da resposta e retorná-lo
def gerar_audio_resposta(resposta):
    tts_endpoint = "https://api.openai.com/v1/audio/speech"
    data = {
        "model": "tts-1",
        "voice": "nova",
        "input": resposta
    }

    response = requests.post(tts_endpoint, headers=headers, json=data)
    response.raise_for_status()

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    with open(temp_file.name, "wb") as audio_file:
        audio_file.write(response.content)

    return temp_file.name
