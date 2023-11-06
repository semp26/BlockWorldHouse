from pyblockworld import World


class Wall:
    def __init__(self, p_pos: tuple, p_bw: World, rotated: bool):
        self.width = 6
        self.height = 5
        self.pos = p_pos
        self.rotated = rotated
        self.material_id = "default:stone"
        self._bw = p_bw

    def build(self):
        x, y, z = self.pos
        if not self.rotated:
            self._bw.setBlocks(x + 1, y - 1, z + 1, x + self.width, y + self.height - 1, z + 1, self.material_id)
        else:
            self._bw.setBlocks(x + 1, y - 1, z + 1, x + 1, y + self.height - 1, z + self.width, self.material_id)


class WallWithWindow(Wall):
    def __int__(self, p_pos: tuple, p_bw: World, rotated: bool):
        super(self).__init__(p_pos, p_bw, rotated)
        self.pos = p_pos

    def build(self):
        Wall.build(self)
        x, y, z = self.pos
        if not self.rotated:
            self._bw.setBlocks(x + 3, y, z + 2, x + self.width - 2, y + self.height - 3, z + 1, "air")
        else:
            self._bw.setBlocks(x + 2, y, z + 3, x + 1, y + self.height - 3, z + self.width - 2, "air")


class WallWithDoor(Wall):
    def __int__(self, p_pos: tuple, p_bw: World, rotated: bool):
        super(self).__init__(p_pos, p_bw, rotated)
        self.pos = p_pos

    def build(self):
        Wall.build(self)
        x, y, z = self.pos
        if not self.rotated:
            self._bw.setBlocks(x + 3, y-1, z + 2, x + self.width - 2, y + self.height - 3, z + 1, "air")
        else:
            self._bw.setBlocks(x + 2, y-1, z + 3, x + 1, y + self.height - 3, z + self.width - 2, "air")


def b_key_pressed(p_world: World):
    x, y, z = p_world.player_position()
    wand1 = WallWithWindow((x, y, z), p_world, False)
    wand2 = WallWithWindow((x, y, z), p_world, True)
    wand1.build()
    wand2.build()
    x, y, z = x, y, z + 5
    door1 = WallWithDoor((x, y, z), p_world, False)
    x, y, z = x + 5, y, z - 5
    door2 = WallWithDoor((x, y, z), p_world, True)
    door1.build()
    door2.build()


world = World()
world.build_key_pressed = b_key_pressed
world.run()
