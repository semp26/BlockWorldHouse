from pyblockworld import World


class Wall:
    def __init__(self, p_pos: tuple, p_bw: World):
        self.width = 6
        self.height = 5
        self.pos = p_pos
        self.rotated = False
        self.material_id = "default:stone"
        self.bw = p_bw

    def build(self):
        x, y, z = self.pos
        if not self.rotated:
            self.bw.setBlocks(x + 1, y - 1, z + 1, x + self.width, y + self.height - 1, z + 1, self.material_id)
        else:
            self.bw.setBlocks(x + 1, y - 1, z + 1, x + 1, y + self.height - 1, z + self.width + 2, self.material_id)


def b_key_pressed(p_world: World):
    x, y, z = p_world.player_position()
    wand1 = Wall((x, y, z), p_world)
    wand2 = Wall((x,y,z),)
    W


world = World()
world.build_key_pressed = b_key_pressed
world.run()
