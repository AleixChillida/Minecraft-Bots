import unittest
from unittest.mock import MagicMock, patch
from bots.insultbot import InsultBot

class TestInsultBot(unittest.TestCase):

    def setUp(self):
        # Mockea el objeto Minecraft
        self.mc = MagicMock()
        self.bot = InsultBot(self.mc)

    @patch('bots.insultbot.random.choice')
    def test_insult_random(self, mock_random_choice):
        mock_random_choice.return_value = "Eres malisimo"
        self.bot.insult_random()
        self.mc.postToChat.assert_any_call("Eres malisimo")

    @patch('bots.insultbot.random.choice')
    def test_insult_personalized(self, mock_random_choice):
        mock_random_choice.return_value = "Eres malisimo"
        player_name = "Steve"
        self.bot.insult_personalized(player_name)
        self.mc.postToChat.assert_any_call(f"{player_name}, Eres malisimo")

    def test_insult_funny(self):
        self.bot.insult_funny()
        self.mc.postToChat.assert_any_call("Un bebe juega mejor que tu")

    def test_bot_initialization(self):
        # Verifica que la lista de insultos esté correctamente inicializada
        expected_insults = [
            "Eres malisimo",
            "Aprende a construir",
            "No sabes pelear",
            "Construyes como un noob.",
            "Así es como juegas Minecraft? Vergonzoso.",
        ]
        self.assertEqual(self.bot.INSULTS, expected_insults)

if __name__ == '__main__':
    unittest.main()
