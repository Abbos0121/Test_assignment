import random
import matplotlib.pyplot as plt


class CityGrid:
    def __init__(self, rows, cols, obstacle_coverage=0.3):
        self.rows = rows
        self.cols = cols
        self.obstacle_coverage = obstacle_coverage
        self.grid = self.generate_grid()

    def generate_grid(self):
        grid = [[0] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() < self.obstacle_coverage:
                    grid[i][j] = 1
        return grid

    def visualize_city_grid(self):
        plt.imshow(self.grid, cmap='gray', interpolation='none')
        plt.title('City Grid')
        plt.show()

    def place_tower(self, x, y, r):
        # Place tower logic here
        pass

    def optimize_tower_placement(self):
        # Optimization logic here
        pass

    def find_reliable_path(self, start, end):
        # Pathfinding logic here
        pass


# Тестирование
city = CityGrid(rows=10, cols=10)
city.visualize_city_grid()
