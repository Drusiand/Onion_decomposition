from typing import Tuple, List
import numpy as np

__PAIR_DELIMITER = ';'
__POINT_DELIMITER = ','


def read_points(filename: str) -> List[Tuple[float, float]]:
    points = list()
    with open(filename, 'r') as source:
        raw_data = source.read().split(__PAIR_DELIMITER)[:-1]
    for pair in raw_data:
        points.append(tuple(float(token) for token in pair.split(__POINT_DELIMITER)))
    return points


def write_points(points: List[Tuple[float, float]]) -> None:
    pass


def generate_normal_sample(size: int) -> None:
    points = list()
    for _ in range(size):
        points.append((round(float(np.random.normal()), 2), round(float(np.random.normal()), 2)))

    with open('data/input_normal.txt', 'w') as f:
        for point in points:
            f.write(str(point[0]) + ',' + str(point[1]))
            if points[-1] != point:
                f.write(';')
