import os
import streamlit as st
import pickle
import time
import langchain
# from langchain.chains import RetrievalQAWithSourcesChain
# from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import HuggingFaceEmbeddings


# Use a pipeline as a high-level helper
from transformers import pipeline
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-Guard-2-8B", token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

pass
