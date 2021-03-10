
# You task is to design an algorithms with breadth-first search that is able to find the shortest path from a given source to a given destination. 
# The maze is represented by a two-dimensional list.

# The (0,0) is the source and (4,4) is the destination. 
# 0 represents walls or obstacles and 1 is the valid cells we can include in the solution.
#note the only way out is to the right and then down
#in every iteration we can make 4 moves (u, d, l, r)

#5:00

from collections import deque

class MazeSolver:
    def __init__(self, matrix):
        self.matrix = matrix
        #note these moves represent x1, y 0 (i.e. right) then x0, y-1 (i.e. down)....
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        #bfs---all cels are set to false for visited in this 2d structure
        #self.visited = [[False for _ in rows] for _ in columns]
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.min_distance = float('inf')

if __name__ == "__main__":

    maze = [
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1],
    [0, 0, 0, 1, 1]
    ]

    maze_solver = MazeSolver(maze)
    maze_solver.search(0, 0, 4, 4)
    maze_solver.show_result()