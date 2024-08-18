import subprocess
from streamlit.web import cli

if __name__ == "__main__":
    cli.main_run(["core.py", "--server.port", "8501"])

    subprocess.run(
        [
            "/home/hugoriviere/.pyenv/shims/python",
            "services/coqui_tts.py",
        ],
        check=False,
    )
    subprocess.run(
        [
            "/home/hugoriviere/.pyenv/shims/python",
            "services/ollama_llm.py",
        ],
        check=False,
    )
