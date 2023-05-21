from langchain.text_splitter import CharacterTextSplitter  # Langchain's class for text splitting

def split_text(text, separator="\n", chunk_size=1000, chunk_overlap=200):
    """
    Function to split the text into chunks using Langchain's CharacterTextSplitter.

    Parameters:
    text (str): String to be splitted.
    separator (str): Separator to split the text.
    chunk_size (int): Maximum size of a chunk.
    chunk_overlap (int): Number of characters from the previous chunk to be repeated in the next one.

    Returns:
    chunks (list): List of chunks.
    """
    text_splitter = CharacterTextSplitter(
        separator=separator,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap, 
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks
