import unittest
from unittest.mock import MagicMock, patch
from bots.tntbot import activate_single_tnt, generate_single_tnt_position, place_block, tntbot_run

class TestTntBot(unittest.TestCase):

    def setUp(self):
        self.mc = MagicMock()
        self.mc.player.getTilePos.return_value = MagicMock(x=0, y=64, z=0)

    def test_generate_single_tnt_position(self):
        base_pos = self.mc.player.getTilePos.return_value
        tnt_pos = generate_single_tnt_position(base_pos)
        self.assertTrue(-5 <= tnt_pos[0] <= 5)
        self.assertEqual(tnt_pos[1], 64)
        self.assertTrue(-5 <= tnt_pos[2] <= 5)

    def test_place_block(self):
        self.mc.setBlock = MagicMock()
        position = (0, 64, 0)
        block_id = 46
        place_block(self.mc, position, block_id)
        self.mc.setBlock.assert_called_once_with(position[0], position[1], position[2], block_id)

    def test_activate_single_tnt(self):
        tnt_position = (0, 64, 0)
        torch_position = activate_single_tnt(tnt_position)
        x, y, z = tnt_position
        tx, ty, tz = torch_position

        self.assertEqual(ty, y)  
        self.assertIn((tx - x, tz - z), [(1, 0), (-1, 0), (0, 1), (0, -1)]) 

    @patch('bots.tntbot.place_block')
    def test_tntbot_run(self, mock_place_block):
        should_continue = MagicMock(side_effect=[True, True, False])  #
        tntbot_run(should_continue)

        self.assertGreaterEqual(mock_place_block.call_count, 4)

    def test_generate_position_within_bounds(self):
        base_pos = self.mc.player.getTilePos.return_value
        for _ in range(100):  
            tnt_pos = generate_single_tnt_position(base_pos)
            self.assertTrue(-5 <= tnt_pos[0] <= 5)
            self.assertTrue(-5 <= tnt_pos[2] <= 5)

if __name__ == '__main__':
    unittest.main()
