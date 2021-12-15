import heapq

data = []
with open("day15.txt") as f:
    for x in f.readlines():
        data.append(x.strip())

# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self, value, point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0

    def move_cost(self, other):
        return self.value


grid = {}
for y in range(0, len(data)):
    for x in range(0, len(data[0])):
        grid[(x, y)] = Node(int(data[y][x]), (x, y))


def children(point, grid):
    x, y = point.point
    neighbours = []
    for neighbour in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
        if (
            neighbour[0] < 0
            or neighbour[1] < 0
            or neighbour[0] >= len(data)
            or neighbour[1] >= len(data)
        ):
            continue
        else:
            neighbours.append(neighbour)
    links = [grid[d] for d in neighbours]
    return links


def manhattan(point, point2):
    return abs(point.point[0] - point2.point[0]) + abs(point.point[1] - point2.point[0])


def aStar(start, goal, grid):
    # The open and closed sets
    openset = set()
    closedset = set()
    # Current point is the starting point
    current = start
    # Add the starting point to the open set
    openset.add(current)
    # While the open set is not empty
    while openset:
        # Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o: o.G + o.H)
        # If it is the item we want, retrace the path and return it
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        # Remove the item from the open set
        openset.remove(current)
        # Add it to the closed set
        closedset.add(current)
        # Loop through the node's children/siblings
        for node in children(current, grid):
            # If it is already in the closed set, skip it
            if node in closedset:
                continue
            # Otherwise if it is already in the open set
            if node in openset:
                # Check if we beat the G score
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    # If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                # If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)
                # Set the parent to our current item
                node.parent = current
                # Add it to the set
                openset.add(node)
    # Throw an exception if there is no path
    raise ValueError("No Path Found")


path = aStar(grid[(0, 0)], grid[(len(data) - 1, len(data) - 1)], grid)

cost = 0
for node in path:
    x, y = node.point
    print(f"({node.point[0]}, {node.point[1]}): {grid[(x,y)].value}")
    if node.point[0] == 0 and node.point[1] == 0:
        continue
    else:
        cost += grid[(x, y)].value

print(cost)
