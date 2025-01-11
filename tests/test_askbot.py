import time
import unittest
from unittest.mock import MagicMock, patch
from bots.askbot import AskBot

class TestAskBot(unittest.TestCase):

    @patch('mcpi.minecraft.Minecraft.create')
    def setUp(self, mock_minecraft_create):
        # Simular la conexión
        self.mock_mc_instance = MagicMock()
        mock_minecraft_create.return_value = self.mock_mc_instance

        # Crear el bot con la instancia simulada
        self.bot = AskBot(self.mock_mc_instance)

    def test_ask_question(self):
        self.bot.ask_question("¿Cuál es la capital de Francia?", "París")
        self.mock_mc_instance.postToChat.assert_any_call("¿Cuál es la capital de Francia?")
        self.mock_mc_instance.postToChat.assert_any_call("Escribe tu respuesta en el chat, tienes 15 segundos.")

    def test_wait_for_answer_timeout(self):
        self.mock_mc_instance.events.pollChatPosts.return_value = []
        answer = self.bot.wait_for_answer("París")
        self.assertIsNone(answer)

    def test_question_1(self):
        self.bot.question_1()
        self.mock_mc_instance.postToChat.assert_any_call("Cual es el bloque mas resistente en Minecraft?")
        self.mock_mc_instance.postToChat.assert_any_call("Escribe tu respuesta en el chat, tienes 15 segundos.")

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
