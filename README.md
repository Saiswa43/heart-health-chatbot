# Heart Health Chatbot 💓

## Project Description
A GenAI-powered medical chatbot designed specifically for heart health.  
It uses a Retrieval-Augmented Generation (RAG) pipeline to combine large language models with custom heart health PDF documents, providing accurate and context-aware answers through an easy-to-use Streamlit interface.

## Why This Technology?
- **RAG Pipeline:** Enables fact-based answers by augmenting LLMs with external medical documents.  
- **PubMedBERT Embeddings:** Domain-specific embeddings optimized for biomedical texts, improving search relevance.  
- **ChromaDB:** Fast and efficient vector store for semantic search.  
- **LlamaCpp & BioMistral:** Open-source LLM offering strong performance on local machines.  
- **Streamlit:** Quick and interactive deployment of the chatbot web app.  
- **Python-dotenv:** Secure management of API tokens and environment variables.

## Challenges Faced
- Balancing model size and performance for local deployment.  
- Ensuring fast retrieval from large medical documents.  
- Keeping API tokens secure and out of public repos.  
- Crafting prompt templates for truthful and relevant responses.

## Features
- Conversational interface for heart health queries.  
- Uses custom PDFs as medical knowledge base.  
- Open-source LLM-based with semantic search.  
- Streamlit-powered web app deployment.  
- Secure environment variable handling.

## Installation & Setup (Windows)

### Clone the repo
```bash
git clone https://github.com/your-username/heart-health-chatbot.git
cd heart-health-chatbot
```
### Create & activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Create .env file
Add your Hugging Face token:
```bash
HUGGINGFACEHUB_API_TOKEN=your_token_here
```
### Add your data
Place heart health PDFs inside the data/ folder
### Add the model
Place the BioMistral .gguf model file inside the models/ folder.
### Run the app
```bash
streamlit run app.py
```
### Project Structure
```bash
heart-health-chatbot/
│
├── .env                  # API keys (not tracked)
├── .gitignore            # Git ignore rules
├── app.py                # Streamlit app entry
├── chatbot.py            # RAG pipeline logic
├── prompt_template.py    # Custom prompt text
├── requirements.txt      # Python packages
├── README.md             # This file
│
├── data/                 # Medical PDFs
├── models/               # LLM model files
├── assets/               # Screenshots and images
└── venv/                 # Virtual environment (ignored)

```
### Security Note
Do NOT commit .env or any API keys.
.gitignore is configured to exclude sensitive files and folders.
### License
MIT License — see LICENSE.
### Acknowledgements
Thanks to GUVI’s GenAI course and the open-source tools: LangChain, SentenceTransformers, Streamlit, and BioMistral.
