"""Solving mazes using Dijkstra algorithm."""

from argparse import ArgumentParser
from itertools import product
from pathlib import Path
from typing import List, Tuple

import cv2
import matplotlib.pyplot as plt
import numpy as np

from point import Point
from utils import get_neighbours, sort_down, sort_up

WHITE_POINT = np.array([255, 255, 255])


def find_shortest_path(
    img: np.ndarray, start_x: int, start_y: int, finish_x: int, finish_y: int
) -> List[Tuple[int, int]]:
    """
    Find the shortest path between two points in a maze.

    Args:
        img: maze image as a numpy array
        start_x: starting point x coordinate
        start_y: starting point y coordinate
        finish_x: finishing point x coordinate
        finish_y: finishing point y coordinate
    """
    matrix = np.full(img.shape, None)  # access by matrix[row][col]
    queue = []  # min heap priority queue

    for row, col in product(img.shape[0], img.shape[1]):
        if np.array_equal(img[row][col], WHITE_POINT):
            matrix[row][col] = Point(col, row, len(queue))
            queue.append(matrix[row][col])

    matrix[start_y][start_x].dist = 0


def draw_path(
    img: np.ndarray, path: List[Tuple[int, int]], thickness: int = 2
) -> None:
    """
    Draw a path on an image.

    Args:
        img: image array
        path: a list of path coordinates as (x, y) tuples
        thickness: path thickness
    """
    curr = path[0]

    for point in path[1:]:
        cv2.line(img, curr, point, (255, 0, 0), thickness)
        curr = point


def main(
    filepath: Path, start_x: int, start_y: int, finish_x: int, finish_y: int
) -> None:
    """
    Find and shows the shortest path between two points in a maze.

    Args:
        filepath: path to the maze image file
        start_x: starting point x coordinate
        start_y: starting point y coordinate
        finish_x: finishing point x coordinate
        finish_y: finishing point y coordinate
    """
    img = cv2.imread(filepath)

    if not np.array_equal(img[start_y][start_x], WHITE_POINT):
        print("Starting point must be white!")
        return

    if not np.array_equal(img[finish_y][finish_x], WHITE_POINT):
        print("Finishing point must be white!")
        return

    path = find_shortest_path(img, start_x, start_y, finish_x, finish_y)
    draw_path(img, path, thickness=img.shape // 100)
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="maze_solver",
        description="Solving mazes using Dijkstra algorithm.",
    )

    parser.add_argument("start_x", type=int, help="start point x coordinate")
    parser.add_argument("start_y", type=int, help="start point y coordinate")
    parser.add_argument("finish_x", type=int, help="end point x coordinate")
    parser.add_argument("finish_y", type=int, help="end point y coordinate")

    parser.add_argument(
        "image",
        default="images/maze.png",
        type=Path,
        help="path to the maze image file",
    )

    args = parser.parse_args()
    main(args.image, args.start_x, args.start_y, args.finish_x, args.finish_y)
