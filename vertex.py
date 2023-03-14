"""
A class for one pixel of an image.
"""

import numpy as np


class Vertex:
    """
    A class for one pixel of an image.

    Attributes:
        x: x coordinate
        y: y coordinate
        dist: distance from source node
        parent_x: x coordinate of the parent node
        parent_y: y coordinate of the parent node
        processed: is the pixel already processed
        index_in_queue: index in queue to process
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.dist = np.inf
        self.parent_x = None
        self.parent_y = None
        self.processed = False
        self.index_in_queue = None
