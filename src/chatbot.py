from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import LlamaCpp
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from src.config import get_config

class RAGChatbot:
    def __init__(self):
        # Load configuration
        self.config = get_config()

        # Initialize embeddings
        self.embeddings = HuggingFaceEmbeddings(model_name=self.config['embeddings_model'])

        # Load the vector store
        self.vectorstore = FAISS.load_local(
            self.config['faiss_index_path'],
            self.embeddings,
            allow_dangerous_deserialization=True
        )

        # Initialize the Llama model
        self.llm = LlamaCpp(
            model_path=self.config['llama_model_path'],
            n_ctx=self.config['llama_n_ctx'],
            n_batch=self.config['llama_n_batch'],
            verbose=self.config['llama_verbose'],
        )

        # Set up the conversational chain
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            self.llm,
            retriever=self.vectorstore.as_retriever(),
            memory=self.memory
        )

    def get_response(self, question):
        response = self.qa_chain({"question": question})
        return response['answer']