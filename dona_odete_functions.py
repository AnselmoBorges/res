# import openai
import tempfile
from services.coqui_tts import tts


def gerar_audio_resposta(resposta):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        tts.tts_to_file(
            text=resposta,
            speaker_wav="U4pQ536JZNY_.wav",
            language="pt",
            file_path=temp_file.name,
        )
    return temp_file.name
