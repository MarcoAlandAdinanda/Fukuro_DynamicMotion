import bezier
import numpy as np
from scipy.spatial import Voronoi
from dijkstar import Graph, find_path


class Fukuro_Dynamic:
    def __init__(self, start_point : list[int], end_point : list[int], robot_coordinate : list[int], smooth : int):
        self.start_point = start_point
        self.end_point = end_point
        self.robot_coordinate = robot_coordinate
        self.smooth = smooth
        self.field_points = np.array([[0, 1400],[0, 0],[2200, 0], [2200, 1400],
                                    [1100, 1400], [1100, 0], [550, 1400],[550, 0],
                                    [1650, 1400], [1650, 0], [2200, 700], [0, 700],
                                    ])
        self.koordinat_attack_zone = np.array([[1975, 900],
                                            [1975, 700],
                                            [1975, 500]])
        self.points = np.append(self.robot_coordinate, self.field_points).reshape(-1, 2)

    def make_curve(self, shortest_path):
        """
            Fungsi untuk menentukan koordinat kurva. Jumlah koordinat untuk membentuk 
            kurva dapat diatur menggunakan attribute smooth
        """
        control_points = shortest_path.T
        t_values = np.linspace(0.0, 1.0, self.smooth)
        
        curve = bezier.Curve(control_points, degree=len(control_points[0])-1)
        curve_points = curve.evaluate_multi(t_values)

        return control_points, curve_points, curve.length
    
    def dijkstra_voronoi(self, end_point) -> list[int]:
        """
            Fungsi untuk menggunakan dijkstra algorithm dengan control point yang 
            berasal dari vertex voronoi diagram 
        """

        vor = Voronoi(self.points)
        vertices = vor.vertices

        graph = Graph()

        for region in vor.regions:
            if not -1 in region and len(region) > 0:
                for i in range(len(region)):
                    v1 = vertices[region[i]]
                    v2 = vertices[region[(i + 1) % len(region)]]
                    distance = ((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)**0.5
                    graph.add_edge(region[i], region[(i + 1) % len(region)], distance)

        start_index = min(range(len(vertices)), key=lambda i: ((vertices[i][0] - self.start_point[0])**2 + (vertices[i][1] - self.start_point[1])**2))
        end_index = min(range(len(vertices)), key=lambda i: ((vertices[i][0] - end_point[0])**2 + (vertices[i][1] - end_point[1])**2))

        shortest_path = find_path(graph, start_index, end_index)
        shortest_path_coordinates = [list(vertices[node]) for node in shortest_path.nodes]
        shortest_path_coordinates.append(end_point)

        return np.array(shortest_path_coordinates)

    def main(self):
        global_curve_points = {}
        global_control_points = {}
        global_length = {}
        
        for i in range(len(self.koordinat_attack_zone)):
            try:
                shortest_path = self.dijkstra_voronoi(self.koordinat_attack_zone[i])
                curve_points, control_points, length = self.make_curve(shortest_path)

                if any(point < 0 or point > 2200 for point in curve_points[0]):
                    raise ValueError("Koordinat x salah")
                
                if any(point < 0 or point > 1400 for point in curve_points[1]):
                    raise ValueError("Koordinat y salah")

                global_curve_points[i] = curve_points
                global_control_points[i] = control_points
                global_length[i] = length

            except:
                continue
        
        min_index = min(global_length, key=global_length.get)

        return global_curve_points[min_index], global_control_points[min_index], global_length[min_index]
