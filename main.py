from streamlit.web import cli

if __name__ == "__main__":
    cli.main_run(["core.py", "--server.port", "8501"])
