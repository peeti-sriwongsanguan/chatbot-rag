import unittest
from unittest.mock import patch, MagicMock
import chatbot

class TestChatbot(unittest.TestCase):
    @patch('chatbot.HuggingFaceEmbeddings')
    @patch('chatbot.FAISS')
    @patch('chatbot.LlamaCpp')
    def test_qa_chain_initialization(self, mock_llama, mock_faiss, mock_embeddings):
        # Mock the dependencies
        mock_embeddings.return_value = MagicMock()
        mock_faiss.load_local.return_value = MagicMock()
        mock_llama.return_value = MagicMock()

        # Call the function that initializes the QA chain
        qa_chain = chatbot.qa_chain

        # Assert that the QA chain was initialized
        self.assertIsNotNone(qa_chain)

    @patch('chatbot.qa_chain')
    def test_chatbot_response(self, mock_qa_chain):
        # Mock the QA chain response
        mock_qa_chain.return_value = {"answer": "This is a test response"}

        # Simulate a user input
        user_input = "Test question"

        # Call the function that processes user input (you might need to adjust this based on your actual implementation)
        response = chatbot.process_user_input(user_input)

        # Assert that the response is as expected
        self.assertEqual(response, "This is a test response")

if __name__ == '__main__':
    unittest.main()