from pyblockworld import World


def b_key_pressed(p_world: World):
    x, y, z = p_world.player_position()
    world.setBlock(x, y-1, z, "default:grass")
    world.setBlock(x+1, y-1, z, "default:grass")


world = World()
world.build_key_pressed = b_key_pressed
world.run()
