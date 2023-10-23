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


class WallWithWindow(Wall):
    def __init__(self, p_pos: tuple, p_bw: World):
        super().__init__(p_pos, p_bw)
        self.window_material_id = "air"

    def build(self):
        x, y, z = self.pos
        if not self.rotated:
            self.bw.setBlocks(x + 1, y - 1, z + 1, x + self.width, y + self.height - 1, z + 1, self.material_id)
            self.bw.setBlocks(x + 3, y, z + 1, x + 4, y + 2, z + 1, self.window_material_id)
        else:
            self.bw.setBlocks(x + 1, y - 1, z + 1, x + 1, y + self.height - 1, z + self.width, self.material_id)
            self.bw.setBlocks(x + 1, y, z + 3, x + 1, y + 2, z + 4, self.window_material_id)


class WallWithDoor(Wall):
    def __init__(self, p_pos: tuple, p_bw: World):
        super().__init__(p_pos, p_bw)
        self.door_material_id = "air"

    def build(self):
        x, y, z = self.pos
        if not self.rotated:
            self.bw.setBlocks(x + 1, y - 1, z + 1, x + self.width, y + self.height - 1, z + 1, self.material_id)
            self.bw.setBlocks(x + 3, y - 1, z + 1, x + 4, y + 2, z + 1, self.door_material_id)
        else:
            self.bw.setBlocks(x + 1, y - 1, z + 1, x + 1, y + self.height - 1, z + self.width, self.material_id)
            self.bw.setBlocks(x + 1, y - 1, z + 3, x + 1, y + 2, z + 4, self.door_material_id)


class Roof:
    def __init__(self, p_pos: tuple, p_bw: World):
        self.width = 6
        self.depth = 6
        self.roof_material_id = "default:brick"
        self.pos = p_pos
        self.bw = p_bw

    def build(self):
        x, y, z = self.pos
        self.bw.setBlocks(x + 1, y + 5, z + 1, x + self.width, y + 5, z + self.depth, self.roof_material_id)


class House:
    def __init__(self, p_pos: tuple, p_bw: World):
        x, y, z = p_pos
        self.wallFront = WallWithDoor(p_pos, p_bw)
        self.wallLeft = WallWithWindow((x + 5, y, z), p_bw)
        self.wallLeft.rotated = True
        self.wallRight = WallWithWindow((x, y, z), p_bw)
        self.wallRight.rotated = True
        self.wallBack = Wall((x, y, z + 5), p_bw)
        self.pos = p_pos
        self.roof = Roof((x, y, z), p_bw)
        self.bw = p_bw

    def build(self):
        self.wallFront.build()
        self.wallLeft.build()
        self.wallRight.build()
        self.wallBack.build()
        self.roof.build()

    def change_wall_material(self, new_material_id: str):
        self.wallFront.material_id = new_material_id
        self.wallLeft.material_id = new_material_id
        self.wallRight.material_id = new_material_id
        self.wallBack.material_id = new_material_id
        self.build()


def b_key_pressed(p_world: World):
    x, y, z = p_world.player_position()
    house1 = House((x, y, z), p_world)
    house1.build()
    house1.change_wall_material("default:grass")


world = World()
world.build_key_pressed = b_key_pressed
world.run()
