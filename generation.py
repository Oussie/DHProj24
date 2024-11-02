from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple, List
from tiles import TileManager
import numpy as np
import random
import heapq

@dataclass
class Tile:
  x: int
  y: int
  possible_states: List[str]

  def __lt__(self, other: Tile) -> bool:
    return len(self.possible_states) < len(other.possible_states)

def generate(grid_size: Tuple[int, int]) -> np.ndarray:
  world = np.zeros(grid_size)
  
  tiles = []
  tile_ids = TileManager.get_ids()
  for x in range(grid_size[0]):
    for y in range(grid_size[1]):
      tiles.append(Tile(x, y, tile_ids))

  tiles = heapq.heapify(tiles)

  while tiles:
    next_tile: Tile = heapq.heappop(tiles)

    state = random.choice(next_tile.possible_states)

    world[next_tile.y][next_tile.x] = int(state)
