# langchain_chatpdf
Talk with your pdfs

## Dependencies in your env
```
pip install langchain pypdf2 python-dotenv streamlit tiktoken faiss-cpu
```

or simply use the requirements.txt file as such:
```
pip install -r requirements
```

## Set up your API Key
Use '.env.example' to create your .env file with your own OPENAI_API_KEY
### Find your API key here:
OpenAI: https://platform.openai.com/account/api-keys

## Usage
To use the application, run the main.py file with the streamlit CLI (after having installed streamlit):

```
streamlit run main.py
```
### Inspired by this:
https://bennycheung.github.io/ask-a-book-questions-with-langchain-openai

The semantic search is done by facebook ai's FAISS (Facebook AI Similarity Search)
![Workflow](https://bennycheung.github.io/images/ask-a-book-questions-with-langchain-openai/Ask_Book_Questions_Workflow.jpg)

