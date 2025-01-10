import random
import time
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
REDSTONE_TORCH_ID = 76

def generate_single_tnt_position(base_pos, radius=5):
    return (
        base_pos.x + random.randint(-radius, radius),
        base_pos.y,
        base_pos.z + random.randint(-radius, radius),
    )

def activate_single_tnt(tnt_position):
    x, y, z = tnt_position
    dx, dz = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])  
    return x + dx, y, z + dz

def place_block(mc, position, block_id):
    x, y, z = position
    mc.setBlock(x, y, z, block_id)


def tntbot_run(should_continue):
    while should_continue():
        player_pos = mc.player.getTilePos()
        tnt_position = generate_single_tnt_position(player_pos)
        place_block(mc, tnt_position, block.TNT.id)  
        torch_position = activate_single_tnt(tnt_position)
        place_block(mc, torch_position, REDSTONE_TORCH_ID)  
        time.sleep(3)

