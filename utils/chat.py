import streamlit as st

from utils.rag import RAGRetriever


@st.cache_resource
def load_retriever():
    return RAGRetriever()
