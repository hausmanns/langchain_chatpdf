from dotenv import load_dotenv
#import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings # Wrapper of embeddings from OpenAI
from langchain.vectorstores import FAISS # Wrapper of FAISS

def main():
    load_dotenv()
    #print(os.getenv("OPENAI_API_KEY")) # Just to make sure it's working, should return the key
    st.set_page_config(page_title = "Ask Your PDF")
    st.header("Ask Your PDF")

    # Upload PDF file
    pdf = st.file_uploader("Upload your PDF file", type=["pdf"])
    # Extract text from PDF
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # split text into chunks, this is a class method
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200, # This is the number of characters from the previous chunk that will be repeated in the next chunk
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Create embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)




if __name__ == '__main__':
    main()