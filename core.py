import base64
import streamlit as st

# from pathlib import Path
from services.ollama_llm import client

# from dotenv import load_dotenv

from dona_odete_functions import gerar_audio_resposta


# Carregando as variaveis de ambiente
# load_dotenv()

# FIXME:  json: cannot unmarshal object into Go struct field ChatRequest.messages of type string


# Configurar Streamlit
st.title("Dona Odete Responde")
st.write("Digite uma pergunta para Dona Odete (essa simpatia) e ouça a resposta.")

# Adicionar uma imagem de uma URL
url = "https://observatoriodatv.uol.com.br/wp-content/uploads/2023/03/Neide.jpg.webp"
st.image(url, caption="Dona Odete", use_column_width=True)

# Defina as instruções iniciais para Dona Odete
system_message = {
    "role": "system",
    "content": "Você é Dona Odete é uma velha crente e viúva de um ex marido cachaceiro que morreu de cirrose que chama Mário, que tem 2 filhos imprestáveis. A filha casou e foi morar nos Estados Unidos e não fala mais com a mãe, mas ela fala pro outro filho Gilberto que a irmã dele Jennyfer deu certo na vida e ele não faz nada direito. Ela vai responder tudo sobre novelas nacionais sempre fazendo uma piada com algo das novelas referente a sua vida. Ela está sempre mal humorada e faz respostas grossas. Sempre antes de gerar as respostas escritas faça piadas aleatorias que vai escrever pois posso não ter entendido",
}

# Inicializar o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = [system_message]
    st.session_state.last_response = ""

# Entrada de texto do usuário
user_input = st.text_input("Digite sua pergunta", "")

# Processar a pergunta do usuário
if st.button("Perguntar"):
    if user_input:
        # Adicionar a pergunta do usuário ao histórico
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Obter a resposta do modelo
        response_message = client.chat(
            model="gemma2:2b", messages=st.session_state.messages
        )

        # Adicionar a resposta do assistente ao histórico
        st.session_state.messages.append(
            {"role": "assistant", "content": response_message}
        )

        # Gerar e reproduzir o áudio da resposta
        audio_file_path = gerar_audio_resposta(response_message["message"]["content"])
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

        st.markdown(
            f"""
            <audio id="response-audio" autoplay>
                <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
            </audio>
            <script>
                var audio = document.getElementById('response-audio');
                audio.onended = function() {{
                    var textContainer = parent.document.getElementById('response-text');
                    textContainer.style.display = 'block';
                }};
            </script>
            """,
            unsafe_allow_html=True,
        )

        # Armazenar a última resposta
        st.session_state.last_response = response_message

        # Limpar a entrada de texto
        user_input = ""

# Container para o texto da resposta
st.markdown(
    f"""
    <div id="response-text" style="display: contents;">
        <p><strong>Dona Odete:</strong> {st.session_state.last_response}</p>
    </div>
    """,
    unsafe_allow_html=True,
)
