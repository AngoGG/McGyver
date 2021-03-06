"""
@desc    Only contain Class Level, see the description below
"""
import random
from classes.constants import Constants


class Level:
    """
    From a file, get the level structure and character/items positionning
    """

    def __init__(self):
        self.file = Constants.FILE
        self.structure = []
        self.empty_cells = []
        self.character_start = []
        self.items_cells = []
        self.end_level = []

    def get_structure(self):
        """
        Parsing File, return Structure List
        Update empty_cell with the cells who are not walls
            (for item positionning and character movement management)
        @return list    structure   Structure of the labyrinth
        """
        with open(self.file, "r") as fichier:
            y = 0
            for line in fichier:
                x = 0
                line_level = []
                for sprite in line.rstrip():
                    if sprite == "0":
                        line_level.append(sprite)
                    elif sprite == "C":
                        self.character_start = [x, y]
                        line_level.append(sprite)
                    elif sprite == "1":
                        self.empty_cells.append([x, y])
                        line_level.append(sprite)
                    elif sprite == "G":
                        line_level.append(sprite)
                        self.end_level = [x, y]
                    x += 1
                self.structure.append(line_level)
                y += 1
            self.put_item_on_map()
            return self.structure

    def put_item_on_map(self):
        """
        Place each item on an empty cell
        Update the labyrinth structure with items positions
        """
        items_cells = random.sample(self.empty_cells, 3)
        self.items_cells = items_cells
        for i, item in enumerate(Constants.ITEMS):
            self.structure[int(items_cells[i]
                               [1])][int(items_cells[i][0])] = item['map']

    @property
    def get_item_position(self):
        """
        @return list    Return the items position inside the labyrinth
        """
        return self.items_cells

    @property
    def get_character_start(self):
        """
            @return list    Return the characters start position
        """
        return self.character_start

    @property
    def get_map_structure(self):
        """
            @return list    Return the labyrinth structure
        """
        return self.structure

    @property
    def get_empty_cells(self):
        """
            @return list    Return the empty cells from labyrinth Structure
                    those cells are cells where items can be place and
                    where the character can move
        """
        return self.empty_cells

    @property
    def get_end_level(self):
        """
            @return list    Return the exit cell from the labyrinth
        """
        return self.end_level
