from collections import (
        namedtuple,
        )
from dataclasses import dataclass



@dataclass
class Cube3:
    x: int
    y: int
    z: int

    def __post_init__(self):
        assert self.x + self.y + self.z == 0


    def __add__(self, other):
        return Cube(self.x + other.x, self.y + other.y, self.z + other.z)


    def __iadd__(self, other):
        return Cube(self.x + other.x, self.y + other.y, self.z + other.z)


    def __radd__(self, other):
        return Cube(self.x + other.x, self.y + other.y, self.z + other.z)



Cube = namedtuple('Cube', ('x', 'y', 'z'))



def addCube(a: Cube, b: Cube):
    c = Cube(a.x + b.x, a.y + b.y, a.z + b.z)
    assert c.x + c.y + c.z == 0

    return c
