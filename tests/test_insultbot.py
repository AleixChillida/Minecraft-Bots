import unittest
from unittest.mock import MagicMock, patch
from bots.insultbot import InsultBot

class TestInsultBot(unittest.TestCase):

    @patch('mcpi.minecraft.Minecraft.create')
    def setUp(self, mock_minecraft_create):
        self.mock_mc_instance = MagicMock()
        mock_minecraft_create.return_value = self.mock_mc_instance

        self.bot = InsultBot(self.mock_mc_instance)

    def test_insult_random(self):
        with patch('bots.insultbot.random.choice', return_value="Eres malísimo"):
            self.bot.insult_random()
            self.mock_mc_instance.postToChat.assert_any_call("Eres malísimo")

    @patch('bots.insultbot.random.choice')
    def test_insult_personalized(self, mock_random_choice):
        mock_random_choice.return_value = "Eres malisimo"
        player_name = "Steve"
        self.bot.insult_personalized(player_name)
        self.mock_mc_instance.postToChat.assert_any_call(f"{player_name}, Eres malisimo")

    def test_insult_funny(self):
        self.bot.insult_funny()
        self.mock_mc_instance.postToChat.assert_any_call("Un bebe juega mejor que tu")

    def test_bot_initialization(self):
        expected_insults = [
            "Eres malisimo",
            "Aprende a construir",
            "No sabes pelear",
            "Construyes como un noob.",
            "Así es como juegas Minecraft? Vergonzoso.",
        ]
        self.assertEqual(self.bot.INSULTS, expected_insults)
