import unittest
from unittest.mock import MagicMock, patch
from bots.tntbot import activate_single_tnt, generate_single_tnt_position, place_block

class TestTntBot(unittest.TestCase):

    @patch('mcpi.minecraft.Minecraft.create')
    def setUp(self, mock_minecraft_create):
        self.mock_mc_instance = MagicMock()
        mock_minecraft_create.return_value = self.mock_mc_instance

    def test_generate_single_tnt_position(self):
        base_pos = MagicMock(x=0, y=64, z=0)
        self.mock_mc_instance.player.getTilePos.return_value = base_pos
        tnt_pos = generate_single_tnt_position(base_pos)
        self.assertTrue(-5 <= tnt_pos[0] <= 5)
        self.assertEqual(tnt_pos[1], 64)
        self.assertTrue(-5 <= tnt_pos[2] <= 5)

    def test_place_block(self):
        self.mock_mc_instance.setBlock = MagicMock()
        position = (0, 64, 0)
        block_id = 46
        place_block(self.mock_mc_instance, position, block_id)
        self.mock_mc_instance.setBlock.assert_called_once_with(position[0], position[1], position[2], block_id)

    def test_activate_single_tnt(self):
        tnt_position = (0, 64, 0)
        torch_position = activate_single_tnt(tnt_position)
        x, y, z = tnt_position
        tx, ty, tz = torch_position

        self.assertEqual(ty, y)
        self.assertIn((tx - x, tz - z), [(1, 0), (-1, 0), (0, 1), (0, -1)])

    def test_generate_position_within_bounds(self):

        base_pos = MagicMock(x=0, y=64, z=0)
        self.mock_mc_instance.player.getTilePos.return_value = base_pos
        
        tnt_pos = generate_single_tnt_position(base_pos)
        
        self.assertTrue(-5 <= tnt_pos[0] <= 5)
        self.assertEqual(tnt_pos[1], 64)  
        self.assertTrue(-5 <= tnt_pos[2] <= 5)
