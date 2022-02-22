def maze_resolve(observation):
    path = []
    start = observation[4]
    finish = observation[5]
    maze = observation[6]
    my_stack = []
    visited = [start]
    current = start

    print('finisas ' + finish)

    [my_stack.append(neighbour) for neighbour in get_neighbours(maze, start)]

    while len(my_stack) > 0:

        current = my_stack.pop()

        if len([node for node in visited if node == current]) > 0:
            continue
        path.append(current)  # action
        visited.append(current)

        if current == finish:
            break
        [my_stack.append(neighbour) for neighbour in get_neighbours(maze, current)]

    path.reverse()
    path_validation(path, maze)
    return path


def get_neighbours(maze, position):
    # neighbours = []
    # for road in maze:
    #     if road[0] == position:
    #         neighbours.append(road[1])
    neighbours = [road[1] for road in maze if road[0] == position]
    return neighbours


def path_validation(path, maze):
    i = 0
    while i < len(path) - 1:
        if node_validation(path[i], path[i + 1], maze):
            i = i + 1
        else:
            path.pop(i + 1)

    return path

def node_validation(prew, next, maze):
    if next in get_neighbours(maze, prew):
        return True
    else:
        return False
