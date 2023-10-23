import random
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import time
import docx2txt
import openai
def get_document_text(uploaded_docs):
    text = ""
    for document in uploaded_docs:
        if document.type == 'application/pdf':
            pdf_reader = PdfReader(document)
            for page in pdf_reader.pages:
                text += page.extract_text()
        elif document.type == "text/plain":
            text += document.read().decode()
        elif document.type in ['application/msword',
                               'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
            text += docx2txt.process(document)
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)
    response = st.session_state.conversation({'question': user_question})

    st.session_state.chat_history = response['chat_history']

    ai_response = st.session_state.chat_history[len(st.session_state.chat_history)-1].content
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        till_character = 0
        for character , response in enumerate(ai_response):
            if character == till_character:
                till_character += random.randint(2,20)
                time.sleep(random.uniform(0.1,0.04))
            full_response += response
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

def is_openai_api_key_valid(key):
    openai.api_key = key
    try:
        openai.Model.list()
    except openai.error.AuthenticationError as e:
        return False
    else:
        return True
def main():
    st.set_page_config(page_title="PDF Converse",
                       page_icon=":books:")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.header(":books: Chat with PDF's ")

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_question = st.chat_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        api_key_input = st.text_input('Enter Your OPENAI API key',placeholder='API KEY')
        if api_key_input:
            os.environ["OPENAI_API_KEY"] = api_key_input


        st.subheader("Your documents")
        user_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True,type=["pdf","txt","msword"])
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_document_text(user_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(
                    vectorstore)


if __name__ == '__main__':
    main()
