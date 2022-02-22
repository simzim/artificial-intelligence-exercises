import math

# konvertuojam koordinates i atskirus skaicius
def convert_to_num(node):
    x = int(node.split('-')[0])
    y = int(node.split('-')[1])
    return x, y


# skaiciuojam atstuma(value) nuo tasko iki aukso
def get_value(next_node, gold):
    position = convert_to_num(next_node)
    goal = convert_to_num(gold)
    value = math.sqrt((position[0]-goal[0])**2 + (position[1]-goal[1])**2)
    return value


# ieskom tasko kaimynu ir susiskaiciujam kiekvieno atstumus
def get_neighbours(observation, current, gold):
    neighbours = {}
    xy_current = convert_to_num(current)

    if observation[0]:
        next_node = str(xy_current[0]) + '-' + str(xy_current[1] + 1)
        neighbours[next_node] = get_value(next_node, gold)
    if observation[1]:
        next_node = str(xy_current[0]) + '-' + str(xy_current[1] - 1)
        neighbours[next_node] = get_value(next_node, gold)
    if observation[2]:
        next_node = str(xy_current[0] - 1) + '-' + str(xy_current[1])
        neighbours[next_node] = get_value(next_node, gold)
    if observation[3]:
        next_node = str(xy_current[0] + 1) + '-' + str(xy_current[1])
        neighbours[next_node] = get_value(next_node, gold)
    return neighbours


# ieskom sekancio ejimo krypti
def find_next(neighbours, visited, path):

    step_back_mode = True
    for x in range(len(neighbours)):
        closest = min(neighbours, key=neighbours.get)
        if closest not in visited:
            step_back_mode = False
            step = closest
            continue
        if closest in visited:
            del(neighbours[closest])

    # jeigu visi kaimynai jau buvo aplankyti darom zingsni atgal
    if step_back_mode:
        path.pop()
        step = path.pop()

    return step


# ejimas
def do_step(current, step):
    xy_current = convert_to_num(current)
    xy_step = convert_to_num(step)

    if xy_step[0] > xy_current[0]:
        action = 3
    elif xy_step[0] < xy_current[0]:
        action = 2
    elif xy_step[1] > xy_current[1]:
        action = 0
    elif xy_step[1] < xy_current[1]:
        action = 1

    return action