
# Document Conversational Chat App

This is a Python application that allows users to have a conversation with a chatbot using documents (PDF, TXT, DOC). The application is built using Streamlit, OpenAI, and other libraries.

## Overview

The application provides the following functionality:

- Users can upload documents (PDF, TXT, DOC) and ask questions about the contents of those documents.
- The application extracts text from the uploaded documents.
- The text is split into smaller chunks for efficient processing.
- The text chunks are converted into vectors using OpenAI's embeddings.
- Users can ask questions, and the application provides responses based on the content of the documents.

## Credit

This project was inspired by a YouTube video tutorial created by **[Alejandro AO - Software & Ai](https://www.youtube.com/@alejandro_ao)**. I have modified and extended the original project to suit my requirements and added additional features.



## How It Works

1. Users upload documents (PDF, TXT, DOC).
2. The text is extracted from the documents and processed into smaller chunks.
3. Text chunks are converted into vectors using OpenAI's embeddings.
4. Users can ask questions in a chat-like interface.
5. The application uses the chatbot to provide responses based on the content of the documents.

## Code Components

The code is organized into functions that handle specific tasks:

- `get_document_text`: Extracts text from uploaded documents.
- `get_text_chunks`: Splits the text into smaller chunks.
- `get_vectorstore`: Converts text chunks into vectors.
- `get_conversation_chain`: Sets up a conversational retrieval chain.
- `handle_userinput`: Handles user input and chat responses.
- `is_openai_api_key_valid`: Checks the validity of an OpenAI API key.
- `main`: Defines the main application logic.

## Installation and Setup

Follow these steps to install and set up the project:

 1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ajit-2111/document-converse.git
   cd document-converse
```
 2. ******Install Dependencies****:**
 ```python
pip install -r requirements.txt
```
 3. ******Set Up OpenAI API Key****:**
- Sign up for an OpenAI account and obtain an API key. A new OpenAI account will have a free $5 credit.
- Create a new OpenAI API Key.

 4. ******Run the Application****:**
 ```python
streamlit run main.py
```
 5. **Access the application in your web browser at **`http://localhost:8501`**.**


## System Requirements

To run this application, ensure that your system meets the following specifications:

-   Python 3.9+
-   Adequate RAM for processing large documents
-   Internet connectivity to access OpenAI services


## Future Work

This project can be further enhanced in the following ways:

-   **Improved Natural Language Processing**: Enhance the chatbot's understanding of user questions and provide more context-aware responses.
-   **Support for More Document Formats**: Extend the application to support additional document formats for a broader range of use cases.
-   **User Authentication**: Implement user authentication to securely access and manage documents.
-   **Multi-Language Support**: Add support for multiple languages to cater to a diverse user base.
-   **Interactive Visualization**: Integrate data visualization tools to provide visual insights based on document content.
-   **Document Summarization**: Implement document summarization to provide concise overviews of lengthy documents.

## Author

Ajit Choudhary
