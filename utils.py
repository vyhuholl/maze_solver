"""Utility functions."""

from typing import List, Optional

import numpy as np

from point import Point


def get_neighbours(
    matrix: List[List[Optional[Point]]], row: int, col: int
) -> List[Point]:
    """
    Finds unprocessed neighbours of a point.

    Args:
        matrix: points matrix
        row: point row
        col: point column

    Returns:
        a list of point neighbours
    """
    neighbours = []

    if row > 0 and matrix[row - 1][col] and not matrix[row - 1][col].processed:
        neighbours.append(matrix[row - 1][col])

    return neighbours
