from ._topological_index import (
    Radius, Diameter,
    TopologicalShapeIndex, PetitjeanIndex,
)

__all__ = ('Diameter', 'Radius', 'TopologicalShapeIndex', 'PetitjeanIndex',)

if __name__ == '__main__':
    from .__main__ import submodule
    submodule()