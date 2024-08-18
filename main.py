import subprocess
from streamlit.web import cli

if __name__ == "__main__":
    cli.main_run(["core.py", "--server.port", "8501"])

    subprocess.run(
        [
            "/home/hugoriviere/anaconda3/envs/voice-cloning-project/bin/python",
            "services/coqui_tts.py",
        ],
        check=True,
    )
    subprocess.run(
        [
            "/home/hugoriviere/anaconda3/envs/voice-cloning-project/bin/python",
            "services/ollama_llm.py",
        ],
        check=True,
    )
