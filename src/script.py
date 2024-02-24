import time
from typing import List
from graph import GraphVisualization


class TravellingSalesmanProblem:
    def __init__(self, matrix) -> None:
       self.graphic = GraphVisualization()

       self.distance_matrix: List[List[int]] = matrix 
       self.completed_visit: int = (1 << len(matrix)) - 1 
       self.memo: List[List[int]] = [[-1 for _ in range(len(matrix))] for _ in range(2 ** len(matrix))]
       self.path_memo = [[-1 for _ in range(len(matrix))] for _ in range(2 ** len(matrix))]
       self.shortest_path: List[int] = []
       self.min_cost: int = 0

       self.algorithm_execution_time: float = 1

    def __del__(self):
        print(f'Object {id(self)} was deleted')

    def solve(self, mark:int, position:int) -> None:
        start = time.time()
        self.min_cost = self.__calculate_min_cost(mark, position)
        end = time.time()
        self.algorithm_execution_time = end - start

        self.shortest_path = self.__find_shortest_path(mark, position)

    def draw_solution(self):
        self.graphic.draw(self.distance_matrix, self.shortest_path)

    def __find_shortest_path(self, mark, position) -> List[int]:
        '''Finding shortest path in graph'''

        path = [0]

        while True:
            next_position = self.path_memo[mark][position]
            if next_position == -1:
                break
            path.append(next_position)
            mark |= (1 << next_position)
            position = next_position
        path.append(0)

        return path


    def __calculate_min_cost(self, mark, position) -> int:
        '''Calculating min cost of path'''

        # base case: if all cities are visited
        # we return dist from current city to start city 
        if mark == self.completed_visit:
            return self.distance_matrix[position][0]
         
        # if subproblem is solved, return dist
        if self.memo[mark][position] != -1:
            return self.memo[mark][position]
        
        min_path_cost = float('inf')

        for city in range(len(self.distance_matrix)):
            if (mark & (1 << city)) == 0:
                new_answer = self.distance_matrix[position][city] + self.__calculate_min_cost(mark | (1 << city), city)

                if min_path_cost > new_answer:
                    min_path_cost = new_answer
                    self.path_memo[mark][position] = city

        self.memo[mark][position] = min_path_cost

        return min_path_cost
