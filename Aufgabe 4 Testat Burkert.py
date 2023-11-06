from pyblockworld import World


class Wall:
    def __init__(self, p_pos: tuple, p_bw: World, rotated: bool):
        self.width = 6
        self.height = 5
        self.pos = p_pos
        self.rotated = rotated
        self.material_id = "default:stone"
        self.bw = p_bw

    def build(self):
        x, y, z = self.pos
        if not self.rotated:
            self.bw.setBlocks(x + 1, y - 1, z + 1, x + self.width, y + self.height - 1, z + 1, self.material_id)
        else:
            self.bw.setBlocks(x + 1, y - 1, z + 1, x + 1, y + self.height - 1, z + self.width, self.material_id)


class WallWithWindow(Wall):
    def __int__(self, p_pos: tuple, p_bw: World, rotated: bool):
        super(self).__init__(p_pos, p_bw, rotated)

    def build(self):
        super().build()
        if not super().rotated:

def b_key_pressed(p_world: World):
    x, y, z = p_world.player_position()
    wand1 = Wall((x, y, z), p_world, False)
    wand2 = Wall((x, y, z), p_world, True)
    wand1.build()
    wand2.build()


world = World()
world.build_key_pressed = b_key_pressed
world.run()
