from python.file_manager import read_points, generate_normal_sample
from python.process import graham_algorithm, sort_points
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import sys


def draw_plot(points, hull):
    fig, ax = plt.subplots(1, 1)
    for i, point in enumerate(hull):
        ax.scatter(point[0], point[1], c='r')
        ax.add_patch(Polygon(hull, fill=False))
    for point in points:
        ax.scatter(point[0], point[1], c='b')

    plt.show()


def run(filename: str) -> None:
    with open('output.txt', 'w') as f:
        points = read_points(filename)
        sort_points(points)
        while len(points) > 0:
            convex_hull, points = graham_algorithm(points)
            draw_plot(points, convex_hull)
            for point in convex_hull:
                f.write(str(point[0]) + ',' + str(point[1]) + ';')
            f.write('\n')
            if len(points) == 0:
                break
            if len(points) < 3:
                for point in points:
                    f.write(str(point[0]) + ',' + str(point[1]) + ';')
                f.write('\n')
                break


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]
        run(file)
        print('Success!\n'
              'Result is saved in \"output.txt\" file')
    else:
        print('Not enough arguments, consider pass input filename as 1st argument!')
