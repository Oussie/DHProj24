from __future__ import annotations

from typing import Tuple, Set, List, Dict
from dataclasses import dataclass, field
from src.tiles import TileManager
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
  
@dataclass
class State:
  tile: Tile
  adjacent: Dict[Tile] = field(default_factory=dict)

def generate(grid_size: Tuple[int, int]) -> np.ndarray:
  world = np.zeros(grid_size, dtype=np.int16)
  
  stack: List[State] = []
  tiles: List[Tile] = []
  tile_ids = TileManager.get_ids()
  for x in range(grid_size[0]):
    for y in range(grid_size[1]):
      tiles.append(Tile(x, y, set(tile_ids)))

  heapq.heapify(tiles)

  backtrack = False

  while tiles:
    if backtrack:
      prev_state = stack.pop()
      if not prev_state.tile.possible_states:
        continue

      backtrack = False

      tiles.append(prev_state.tile)
      for tile in tiles:
        coords = (tile.x, tile.y)
        if prev_state.adjacent.get(coords, False):
          tile.possible_states = prev_state.adjacent[coords].possible_states

      heapq.heapify(tiles)
      continue

    next_tile: Tile = heapq.heappop(tiles)

    x = next_tile.x
    y = next_tile.y
    choice = random.choice(list(next_tile.possible_states))
    world[y][x] = int(choice)

    state = State(Tile(x, y, next_tile.possible_states - {choice}))

    directions = ["north", "east", "south", "west"]
    to_adjacent = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    adjacent_indices = { (x + i, y + j) : direction for direction, (i, j) in zip(directions, to_adjacent) }

    for tile in tiles:
      coords = (tile.x, tile.y)
      if adjacent_indices.get(coords, False):
        possible_states = set(TileManager.get(choice)[adjacent_indices[coords]])
        state.adjacent[coords] = tile

        new_states = possible_states & tile.possible_states
        if not new_states: 
          backtrack = True
          break

        tile.possible_states = new_states

    heapq.heapify(tiles)
    stack.append(state)

  return world

if __name__ == "__main__":
  print(generate((10, 10)))
  

