import streamlit as st
from chatbot import load_and_index_docs, load_llm, build_rag_chain

st.set_page_config(page_title="Heart Health Chatbot", page_icon="🩺")
st.title("🩺 Heart Health Medical Chatbot")

# Initialize resources
@st.cache_resource
def initialize_chatbot():
    vectorstore = load_and_index_docs()
    llm = load_llm()
    return build_rag_chain(vectorstore, llm)

rag_chain = initialize_chatbot()

# User input
user_query = st.text_input("Ask something about heart health:")

if user_query:
    with st.spinner("Generating response..."):
        response = rag_chain.invoke(user_query)
        st.markdown("### 💬 Answer")
        st.write(response)
