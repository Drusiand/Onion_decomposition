from typing import Tuple, List


def is_left_turn(point_1: Tuple[float, float], point_2: Tuple[float, float], point_3: Tuple[float, float]):
    return (point_2[0] - point_1[0]) * (point_3[1] - point_1[1]) - (point_2[1] - point_1[1]) * (
            point_3[0] - point_1[0]) > 0


def sort_points(points: List[Tuple[float, float]]):
    points.sort(key=lambda x: (x[0], x[1]))


def graham_algorithm(points: List[Tuple[float, float]]):
    convex_hull = list()
    convex_hull.extend(graham_step(points, True))
    convex_hull.pop()
    convex_hull.extend(reversed(graham_step(points, False)))
    convex_hull.pop()
    return convex_hull


def graham_step(points: List[Tuple[float, float]], traversal_order: bool) -> List[Tuple[float, float]]:
    stack = list()
    for point in points:
        stack.append(point)
        if len(stack) < 3:
            continue
        while is_left_turn(stack[-3], stack[-2], stack[-1]) is traversal_order:
            stack.pop(-2)
            if len(stack) < 3:
                break
    return stack
