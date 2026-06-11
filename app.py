import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama

llm = Ollama(
    model="llama3.2",
    temperature=0.3
)


# Local LLM
llm = Ollama(model="llama3.2")


def extract_text(pdf_path):

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    text = ""

    for doc in docs:
        text += doc.page_content + "\n"

    return text


def generate_questions(text):

    print("Sending prompt to Ollama...")

    prompt = f"""
    Generate 10 important exam questions from:

    {text[:3000]}
    """

    response = llm.invoke(prompt)

    print("Response received!")

    return response


st.set_page_config(page_title="PDF Question Generator")

st.title("📚 PDF Question Generator")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF Uploaded Successfully")

    if st.button("Generate Questions"):

        with st.spinner("Generating Questions..."):

            text = extract_text(pdf_path)

            questions = generate_questions(text)

            st.subheader("Generated Questions")

            st.write(questions)
