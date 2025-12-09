# 'Advent of code' solution for year 2025 day 9
import os
import sys
import numpy as np

import matplotlib.pyplot as plt
from shapely.geometry import Polygon , box

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def _get_input():
    content = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r", encoding="utf-8") as file:
            content = file.read().strip().splitlines()
        return content
    else:
        print("Error! Input file does not exist!")
        sys.exit()

def part_1(i: list[str]):
    coords = [tuple(map(int, line.split(","))) for line in i]
    coords = np.array(coords, dtype=int)

    area = -1

    for p1_i, p1 in enumerate(coords):
        for p2_i in range(p1_i + 1, len(coords)):
            p2 = coords[p2_i]
            width, height = abs(p1[0] - p2[0]) + 1, abs(p1[1] - p2[1]) + 1
            curr = width * height
            if curr > area:
                area = curr

    print(f"[P1] Largest area {area}")

def part_2(inp: list[str]):
    max_area = 0
    coords = [tuple(map(int, line.split(","))) for line in inp]
    coords = np.array(coords, dtype=int)

    # Build polygon
    poly = Polygon(coords)

    # Store valid rectangles and their coordinates
    valid_rects = []
    valid_rect_coords = []
    largest_rect = None

    # Set up live preview
    plt.ion()
    fig, ax = plt.subplots()
    x, y = poly.exterior.xy
    ax.plot(x, y, color='black', linewidth=2, label='Polygon')
    ax.set_aspect('equal')
    ax.legend()
    fig.canvas.draw()
    fig.canvas.flush_events()

    n = len(coords)
    for i in range(n):
        for j in range(n):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            minx, maxx = min(x1, x2), max(x1, x2)
            miny, maxy = min(y1, y2), max(y1, y2)
            rect = box(minx, miny, maxx, maxy)
            # Allow rectangle to touch the polygon edge but not cross it
            if not poly.covers(rect):
                continue
            area = rect.area
            valid_rects.append(rect)
            valid_rect_coords.append((minx, miny, maxx, maxy))
            # Live preview: plot current rectangle
            rx, ry = rect.exterior.xy
            rect_plot, = ax.plot(rx, ry, color='blue', alpha=0.5)
            best_rect = None
            if largest_rect:
                bx, by = largest_rect.exterior.xy
                best_rect, = ax.plot(bx, by, color="red", alpha=0.5)
            fig.canvas.draw()
            fig.canvas.flush_events()
            rect_plot.remove()
            if best_rect:
                best_rect.remove()
            if area > max_area:
                max_area = area
                largest_rect = rect

    if largest_rect:
        bx, by = largest_rect.exterior.xy
        print(bx, by)
        width = abs(max(bx) - min(bx)) + 1
        height = abs(max(by) - min(by)) + 1
        print(width, height)
        max_area = width * height

    print(f"[P2] Largest area: {max_area}")

    plt.show()
    plt.ioff()

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs)
    part_2(inputs)

    sys.exit()
