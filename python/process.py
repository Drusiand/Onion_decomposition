from typing import Tuple, List


def oriented_square(point_1: Tuple[float, float], point_2: Tuple[float, float], point_3: Tuple[float, float]):
    # print((point_2[0] - point_1[0]) * (point_3[1] - point_1[1]) - (point_2[1] - point_1[1]) * (point_3[0] - point_1[0]))
    return (point_2[0] - point_1[0]) * (point_3[1] - point_1[1]) - (point_2[1] - point_1[1]) * (
            point_3[0] - point_1[0])


def sort_points(points: List[Tuple[float, float]]):
    points.sort(key=lambda x: (x[0], x[1]))


def graham_algorithm(points: List[Tuple[float, float]]):
    convex_hull = list()
    hull_bot, new_points = graham_step(points, True)
    convex_hull.extend(hull_bot)
    convex_hull.pop()
    sort_points(new_points)
    hull_top, new_points = graham_step(new_points, False)
    convex_hull.extend(reversed(hull_top))
    convex_hull.pop()
    sort_points(new_points)
    return convex_hull, new_points


def graham_step(points: List[Tuple[float, float]], traversal_order: bool) -> List[Tuple[float, float]]:
    stack = list()
    new_points = [points[0]] if traversal_order else []
    for point in points:
        stack.append(point)
        if len(stack) < 3:
            continue
        while (oriented_square(stack[-3], stack[-2], stack[-1]) > 0) == traversal_order or \
                oriented_square(stack[-3], stack[-2], stack[-1]) == 0:
            new_points.append(stack.pop(-2))
            if len(stack) < 3:
                break
    if traversal_order:
        new_points.append(points[-1])
    return stack, new_points
