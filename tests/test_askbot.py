import time
import unittest
from unittest.mock import MagicMock
from bots.askbot import AskBot

class TestAskBot(unittest.TestCase):

    
    def setUp(self):

        self.mc = MagicMock()
        self.bot = AskBot(self.mc)

    def test_ask_question(self):

        self.bot.ask_question("¿Cuál es la capital de Francia?", "París")
        self.mc.postToChat.assert_any_call("¿Cuál es la capital de Francia?")
        self.mc.postToChat.assert_any_call("Escribe tu respuesta en el chat, tienes 15 segundos.")

    def test_wait_for_answer_timeout(self):

        self.mc.events.pollChatPosts.return_value = []
        answer = self.bot.wait_for_answer("París")
        self.assertIsNone(answer)  

    def test_question_1(self):

        self.bot.question_1()
        self.mc.postToChat.assert_any_call("Cual es el bloque mas resistente en Minecraft?")
        self.mc.postToChat.assert_any_call("Escribe tu respuesta en el chat, tienes 15 segundos.")

    def test_random_question_execution(self):

        self.bot.question_1 = MagicMock()
        self.bot.question_2 = MagicMock()
        self.bot.question_3 = MagicMock()

        def should_continue_mock():
            nonlocal iterations
            iterations -= 1
            return iterations > 0

        iterations = 3 
        self.bot.run(should_continue_mock)

       
        called_questions = (
            self.bot.question_1.called,
            self.bot.question_2.called,
            self.bot.question_3.called,
        )
        self.assertTrue(any(called_questions), "Ninguna pregunta fue llamada durante las iteraciones.")

if __name__ == '__main__':
    unittest.main()
