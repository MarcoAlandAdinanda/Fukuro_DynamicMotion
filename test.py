import numpy as np
import matplotlib.pyplot as plt
from backup import Fukuro_Dynamic

def bezier_visualizer(curve_points, control_points, robot_coordinate=None):
    plt.figure()
    plt.plot(*curve_points, label="Bezier Curve")
    plt.scatter(curve_points[0][-1], curve_points[1][-1], color="g", label="Control Points")
    plt.scatter(control_points[0][:-1], control_points[1][:-1], color="r", label="Control Points")
    if robot_coordinate is not None:
        plt.scatter(robot_coordinate.T[0], robot_coordinate.T[1], color="b", label="Robot Coordinate")
    plt.xlabel("Length")
    plt.ylabel("Width")
    plt.xlim([0, 2200])
    plt.ylim([0, 1400])
    plt.legend()
    plt.show()


x = np.random.randint(0, 2200, (10, 1)) 
y = np.random.randint(0, 1400, (10, 1))
robot_coordinate = np.append(x, y, axis=1)

start_point = [robot_coordinate[6][0], robot_coordinate[6][1]]
end_point = [1975, 700]

code = Fukuro_Dynamic(start_point, end_point, robot_coordinate, smooth=15)

# print(code.dijkstra_voronoi())
curve_points, control_points, length  = code.main()

print(curve_points)
print(control_points)
print(length)
bezier_visualizer(curve_points, control_points, robot_coordinate=robot_coordinate)
print(f"Panjang lintasan curve: {length}")