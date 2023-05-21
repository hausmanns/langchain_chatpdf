from dotenv import load_dotenv # Library to load environment variables
import streamlit as st # Framework for creating web applications
from utils.pdf_reader import read_pdf # Function to read PDFs
from utils.text_splitter import split_text # Function to split text into chunks
from utils.embedding_creator import create_embeddings # Function to create embeddings
from utils.question_answerer import answer_question # Function to generate answers to questions

from langchain.callbacks import get_openai_callback # Callback to get the OpenAI money spent
def main():
    """
    Main function of the application.
    It loads the environment variables, sets up the Streamlit page,
    reads and processes the uploaded PDF, and handles the user's questions.
    """
    load_dotenv()
    st.set_page_config(page_title = "Ask Your PDF")
    st.header("Ask Your PDF")

    # Upload PDF file
    pdf = st.file_uploader("Upload your PDF file", type=["pdf"])
    # Extract text from PDF
    if pdf is not None:
        text = read_pdf(pdf)
        chunks = split_text(text)
        knowledge_base = create_embeddings(chunks)

        # Show user input
        user_question = st.text_input("Ask a question")
        if user_question:
            with get_openai_callback() as openai_callback: # How much you spend for executing this chain
                response = answer_question(knowledge_base, user_question, model_name="gpt-3.5-turbo")
                print(openai_callback)
            st.write(response)

if __name__ == '__main__':
    main()
