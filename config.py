from typing import Tuple


class Config:

    def __init__(self, left: Tuple[str, ...], right: Tuple[str, ...], up: Tuple[str, ...], down: Tuple[str, ...]):
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    @classmethod
    def get_melon_pumpkin(cls):
        return cls(('x', 'a'), ('x', 'd'), ('w',), ('s',))

    @classmethod
    def get_cocoa(cls):
        return cls(('a',), ('d',), ('x', 'w'), ('x', 's'))

    @classmethod
    def get_mushroom(cls):
        return cls(('x', 'w', 'a'), ('x', 'd'), ('w',), ('s',))

    @classmethod
    def get_sugarcane(cls):
        return cls(('x', 'a'), ('x', 's'), ('w',), ('s',))

    @classmethod
    def get_cactus(cls):
        return cls(('x', 'a'), ('x', 'd'), ('w',), ('s',))

    @classmethod
    def get_modes(cls):
        return {
            "Melon / Pumpkin": cls.get_melon_pumpkin,
            "Cocoa Beans": cls.get_cocoa,
            "Mushroom": cls.get_mushroom,
            "Sugarcane": cls.get_sugarcane,
            "Cactus": cls.get_cactus,
        }
