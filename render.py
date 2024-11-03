from tiles import TileManager
from assets import AssetManager, Cloud


def renderWorld(screen, arr):
    TILE_SIZE = AssetManager.get_size()
    # Draw the grid using blit
    for y, row in enumerate(arr):
        for x, id in enumerate(row):
            index = TileManager.get(id)["index"]
            tile = AssetManager.get(*index)

            # Blit the image at the calculated position
            screen.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))


def renderCloud(screen, cloud_arr):
    TILE_SIZE = Cloud.get_size()
    # Draw the grid using blit
    for y, row in enumerate(cloud_arr):
        for x, id in enumerate(row):
            tile = Cloud.get(cloud_arr[y][x])

            # Blit the image at the calculated position
            screen.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))


def render(screen, world_arr, cloud_arr):
    renderWorld(screen, world_arr)
    renderCloud(screen, cloud_arr)
