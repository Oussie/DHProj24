from tiles import TileManager
from assets import AssetManager

def render(screen, arr):
    TILE_SIZE = AssetManager.get_size()
    # Draw the grid using blit
    for y,row in enumerate(arr):
        for x,id in enumerate(row):
            index = TileManager.get(id)["index"]
            tile = AssetManager.get(*index)

            # Blit the image at the calculated position
            screen.blit(tile, (x*TILE_SIZE, y*TILE_SIZE))