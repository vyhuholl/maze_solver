"""A class for one image point."""

from typing import Optional

import numpy as np


class Point:
    """
    A class for one image point.

    Attributes:
        x: x coordinate
        y: y coordinate
        dist: distance from source node
        parent_x: x coordinate of the parent node
        parent_y: y coordinate of the parent node
        processed: is the pixel already processed
        index_in_queue: index in queue to process
    """

    def __init__(self, x: int, y: int, index_in_queue: Optional[int] = None):
        self.x = x
        self.y = y
        self.dist = np.inf
        self.parent_x = None
        self.parent_y = None
        self.processed = False
        self.index_in_queue = index_in_queue
