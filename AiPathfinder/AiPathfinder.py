import heapq
import random

def calc_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_path(grid_map, start_pos, end_pos):
    total_rows = len(grid_map)
    total_cols = len(grid_map[0])

    open_nodes = []
    heapq.heappush(open_nodes, (0, start_pos))

    parent_map = {}
    g_cost = {start_pos: 0}
    f_cost = {start_pos: calc_dist(start_pos, end_pos)}

    while len(open_nodes) > 0:
        current_node = heapq.heappop(open_nodes)[1]

        if current_node == end_pos:
            final_path = []
            while current_node in parent_map:
                final_path.append(current_node)
                current_node = parent_map[current_node]
            final_path.append(start_pos)
            final_path.reverse()
            return final_path

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for move in directions:
            next_r = current_node[0] + move[0]
            next_c = current_node[1] + move[1]
            neighbor_node = (next_r, next_c)

            if next_r < 0 or next_c < 0 or next_r >= total_rows or next_c >= total_cols:
                continue

            if grid_map[next_r][next_c] == 1:
                continue

            new_g = g_cost[current_node] + 1

            if neighbor_node not in g_cost or new_g < g_cost[neighbor_node]:
                parent_map[neighbor_node] = current_node
                g_cost[neighbor_node] = new_g
                new_f = new_g + calc_dist(neighbor_node, end_pos)
                f_cost[neighbor_node] = new_f
                heapq.heappush(open_nodes, (new_f, neighbor_node))

    return None

def make_grid(n, obstacle_chance):
    grid_data = []
    for i in range(n):
        row = []
        for j in range(n):
            if random.random() < obstacle_chance:
                row.append(1)
            else:
                row.append(0)
        grid_data.append(row)

    grid_data[0][0] = 0
    grid_data[n-1][n-1] = 0
    return grid_data

grid_size = 10
my_grid = make_grid(grid_size, 0.3)
start = (0, 0)
goal = (grid_size - 1, grid_size - 1)
path_result = find_path(my_grid, start, goal)

if path_result:
    print("Path found! Length:", len(path_result))
    for r in range(grid_size):
        line = ""
        for c in range(grid_size):
            cell = (r, c)
            if cell == start:
                line += "S "
            elif cell == goal:
                line += "G "
            elif cell in path_result:
                line += "* "
            elif my_grid[r][c] == 1:
                line += "# "
            else:
                line += ". "
        print(line)
else:
    print("No path found.")
