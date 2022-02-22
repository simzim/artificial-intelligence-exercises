
def get_neighbours(observation, current):
    neighbours = []
    x = int(current.split('-')[0])
    y = int(current.split('-')[1])
    if observation[0]:
        neighbours.append(str(x) + '-' + str(y + 1))
    if observation[1]:
        neighbours.append(str(x) + '-' + str(y - 1))
    if observation[2]:
        neighbours.append(str(x - 1) + '-' + str(y))
    if observation[3]:
        neighbours.append(str(x + 1) + '-' + str(y))

    return neighbours


def find_next(neighbours, visited, path):
    # ieskom sekancio kaimyno tasko
    step_back_mode = True
    for one_neighbour in neighbours:

        if one_neighbour not in visited:
            step_back_mode = False
            step = one_neighbour
            continue
    # jeigu visi kaimynai jau buvo aplankyti darom zingsni atgal
    if step_back_mode:
        path.pop()
        step = path.pop()

    return step


def do_step(current, step):

    x_axis = int(current.split('-')[0])
    y_axis = int(current.split('-')[1])

    x = int(step.split('-')[0])
    y = int(step.split('-')[1])

    if x > x_axis:
        action = 3
    elif x < x_axis:
        action = 2
    elif y > y_axis:
        action = 0
    elif y < y_axis:
        action = 1

    return action