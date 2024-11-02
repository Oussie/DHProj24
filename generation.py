from __future__ import annotations

from typing import Tuple, Set, List
from dataclasses import dataclass
from tiles import TileManager
import numpy as np
import random
import heapq

@dataclass
class Tile:
  x: int
  y: int
  possible_states: Set[str]

  def __lt__(self, other: Tile) -> bool:
    return len(self.possible_states) < len(other.possible_states)

def generate(grid_size: Tuple[int, int]) -> np.ndarray:
  world = np.zeros(grid_size)
  
  stack = []
  tiles: List[Tile] = []
  tile_ids = TileManager.get_ids()
  for x in range(grid_size[0]):
    for y in range(grid_size[1]):
      tiles.append(Tile(x, y, set(tile_ids)))

  heapq.heapify(tiles)

  while tiles:
    next_tile: Tile = heapq.heappop(tiles)

    x = next_tile.x
    y = next_tile.y
    state = random.choice(list(next_tile.possible_states))
    world[y][x] = int(state)

    directions = ["north", "east", "south", "west"]
    to_adjacent = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    adjacent_indices = { (x + i, y + j) : direction for direction, (i, j) in zip(directions, to_adjacent) }

    for tile in tiles:
      coords = (tile.x, tile.y)
      if adjacent_indices.get(coords, False):
        possible_states = set(TileManager.get(state)[adjacent_indices[coords]])
        tile.possible_states = possible_states & tile.possible_states

    heapq.heapify(tiles)

    print(world)
    print("\n\n\n")

  return world

if __name__ == "__main__":
  print(generate((5, 5)))
  

