from code.fun import print_cindy_header
from code.gradio_ui import setup_gradio_ui
from code.llm_connector import setup_openai


def main():
    print_cindy_header()
    openai = setup_openai()
    setup_gradio_ui(openai=openai)


if __name__ == '__main__':
    main()
