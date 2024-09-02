import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chatbot import RAGChatbot


class TestChatbot(unittest.TestCase):
    @patch('src.chatbot.HuggingFaceEmbeddings')
    @patch('src.chatbot.FAISS')
    @patch('src.chatbot.LlamaCpp')
    @patch('src.chatbot.ConversationalRetrievalChain')
    def test_rag_chatbot_initialization(self, mock_chain, mock_llama, mock_faiss, mock_embeddings):
        # Mock the dependencies
        mock_embeddings.return_value = MagicMock()
        mock_faiss.load_local.return_value = MagicMock()
        mock_faiss.from_texts.return_value = MagicMock()
        mock_llama.return_value = MagicMock()
        mock_chain.from_llm.return_value = MagicMock()

        # Initialize the RAGChatbot
        chatbot = RAGChatbot()

        # Assert that the chatbot was initialized
        self.assertIsNotNone(chatbot)
        self.assertIsNotNone(chatbot.qa_chain)

    @patch('src.chatbot.HuggingFaceEmbeddings')
    @patch('src.chatbot.FAISS')
    @patch('src.chatbot.LlamaCpp')
    @patch('src.chatbot.ConversationalRetrievalChain')
    def test_chatbot_response(self, mock_chain, mock_llama, mock_faiss, mock_embeddings):
        # Mock the dependencies
        mock_embeddings.return_value = MagicMock()
        mock_faiss.load_local.return_value = MagicMock()
        mock_faiss.from_texts.return_value = MagicMock()
        mock_llama.return_value = MagicMock()

        # Mock the ConversationalRetrievalChain
        mock_qa_chain = MagicMock()
        mock_qa_chain.return_value = {"answer": "This is a test response"}
        mock_chain.from_llm.return_value = mock_qa_chain

        # Initialize the RAGChatbot
        chatbot = RAGChatbot()

        # Simulate a user input
        user_input = "Test question"

        # Call the get_response method
        response = chatbot.get_response(user_input)

        # Assert that the response is as expected
        self.assertEqual(response, "This is a test response")


if __name__ == '__main__':
    unittest.main()