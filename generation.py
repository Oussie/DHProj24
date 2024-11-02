from __future__ import annotations
from dataclasses import dataclass
from tiles import TileManager
from typing import Tuple
import numpy as np
import heapq

@dataclass
class Tile:
  x: int
  y: int
  num_states: int

  def __lt__(self, other: Tile) -> bool:
    return self.num_states < other.num_states

def generate(grid_size: Tuple[int, int]) -> np.ndarray:
  world = np.zeros(grid_size)
  
  tiles = []
  for x in range(grid_size[0]):
    for y in range(grid_size[1]):
      tiles.append(Tile(x, y, TileManager.num_tiles()))

  tiles = heapq.heapify(tiles)
