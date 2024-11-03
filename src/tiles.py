import json

class _TileManager:
    def __init__(self):
        with open("assets/tiles.json") as file:
            self.tiles = json.load(file)
        #Load json
    
    def get(self, tile_id):
        return self.tiles[str(tile_id)]
        #Get tile from json

    def get_ids(self):
        return list(self.tiles.keys())
    
TileManager = _TileManager()  
if __name__ == "__main__":
    print('\n', _TileManager().get(1))