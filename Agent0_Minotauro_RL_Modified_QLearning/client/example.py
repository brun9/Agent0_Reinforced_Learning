import client
import ast
import random

def getTargets(c):
    ''' Return the targets defined in the world.'''
    msg = c.execute("info", "targets")
    res = ast.literal_eval(msg)
    # test
    # print('Received targets:', res)
    return res

def getListTargets(c,targets,max_coord):
    targets_list =[]
    for y in range(max_coord[1]):
        for x in range(max_coord[0]):
            if targets[x][y] == 1:
                targets_list.append((x,y))
    # Test
    #print("Targets List:",targets_list)
    return targets_list

def getPos(c):
    '''Return the actual position of the agent. '''
    msg = c.execute("info", "position")
    pos = ast.literal_eval(msg)
    # test
    #print('Received agent\'s position:', pos)
    return pos

def getReward(c):
    msg = c.execute("info","rewards")
    reward = ast.literal_eval(msg)
    # test
    #print('Reward map: ', reward)
    return reward

def getMaxCoord(c):
    msg = c.execute("info", "maxcoord")
    max_coord = ast.literal_eval(msg)
    # test
    #print('Received maxcoord', max_coord)
    return max_coord

def getGoalPosition(c):
    msg = c.execute("info", "goal")
    goal = ast.literal_eval(msg)
    # test
    #print('Goal is located at:', goal)
    return goal

def getObstacles(c):
    msg = c.execute("info","obstacles")
    obst =ast.literal_eval(msg)
    # test
    print('Received map of obstacles:', obst)
    return obst

def getTurns(direction, desired_direction):
    # Return directions
    if direction == "north" and desired_direction == "east":
        return ["right"]
    if direction == "north" and desired_direction == "west":
        return ["left"]
    if direction == "north" and desired_direction == "south":
        return ["right", "right"]

    if direction == "south" and desired_direction == "east":
        return ["left"]
    if direction == "south" and desired_direction == "west":
        return ["right"]
    if direction == "south" and desired_direction == "north":
        return ["right", "right"]

    if direction == "east" and desired_direction == "north":
        return ["left"]
    if direction == "east" and desired_direction == "south":
        return ["right"]
    if direction == "east" and desired_direction == "west":
        return ["right", "right"]

    if direction == "west" and desired_direction == "north":
        return ["right"]
    if direction == "west" and desired_direction == "south":
        return ["left"]
    if direction == "west" and desired_direction == "east":
        return ["left", "left"]
    return []


def reactive_example_2(c,res:int,qTable):

    initial_pos = getPos(c)
    goal = getGoalPosition(c)
    max_coord = getMaxCoord(c)
    rewards = getReward(c)
    targetsL = getListTargets(c, getTargets(c), max_coord)
    print(initial_pos)

    if res != -1:

        for i in range(500):
            print(i)
            c.execute("command", "home", 0.02)
            findGoal = False
            findTarget = False
            episode = []
            episode.append(initial_pos)
            msg = c.execute("command", "set_steps")
            while findGoal == False and findTarget == False:
                direction = random.randint(1, 4)
                if direction == 1:
                    value = "north"
                elif direction == 2:
                    value = "south"
                elif direction == 3:
                    value = "east"
                else:
                    value = "west"
                # Selecting Policy
                # ...
                action = "command"
                # Test
                # print("Action Value pair:", action, ":", value)
                msg = c.execute(action, value, 0.02)
                pos = getPos(c)
                episode.append(pos)  # New position
                # Test
                # agent.print_message(msg)

                # Final Position
                # if pos == goal or pos in one of the targets!!
                if pos == goal:
                    findGoal = True
                if pos in targetsL:
                    findTarget = True
            episode_reversed = episode[::-1]
            last_pos = episode_reversed[0]
            del episode_reversed[0]

            peso = 0.9
            movement = ""
            last_reward = rewards[last_pos[0]][last_pos[1]]

            for pos in episode_reversed:
                if pos[0] == last_pos[0]:
                    if pos[1] > last_pos[1] and pos[1] - last_pos[1] == 1:
                        movement = "north"
                    elif pos[1] < last_pos[1] and pos[1] - last_pos[1] == -1:
                        movement = "south"
                    elif pos[1] == 0 and last_pos[1] == max_coord[1]  -1:
                        movement = "north"
                    elif pos[1] == max_coord[1] -1 and last_pos[1] == 0:
                        movement = "south"
                elif pos[1] == last_pos[1]:
                    if pos[0] > last_pos[0] and pos[0] - last_pos[0] == 1:
                        movement = "west"
                    elif pos[1] < last_pos[0] and pos[0] - last_pos[0] == -1:
                        movement = "east"
                    elif pos[1] == 0 and last_pos[0] == max_coord[0] -1:
                        movement = "west"
                    elif pos[1] == max_coord[0] -1 and last_pos[0] == 0:
                        movement = "east"
                else:
                    movement = ""

                if(movement != ""):
                    last_value = qTable[str(pos)]
                    print("last reward: ", last_reward)
                    r = rewards[last_pos[0]][last_pos[1]]
                    if (r == 100 or r == -50):
                        new_r = 0 + peso * last_reward
                    else:
                        new_r = r + peso * last_reward
                    last_reward = new_r
                    if movement == "north":
                        if(new_r > last_value[0]):
                            qTable[str(pos)] = [new_r, last_value[1], last_value[2], last_value[3]]
                    elif movement == "east":
                        if (new_r > last_value[1]):
                            qTable[str(pos)] = [(last_value[0]), new_r, last_value[2], last_value[3]]
                    elif movement == "south":
                        if (new_r > last_value[2]):
                            qTable[str(pos)] = [(last_value[0]),last_value[1] , new_r, last_value[3]]
                    elif movement == "west":
                        if (new_r > last_value[3]):
                            qTable[str(pos)] = [last_value[0], last_value[1], last_value[2], new_r]

                    last_pos = pos
        obstacles = getObstacles(c)
        for casa in qTable:
            max_reward = 0
            max_reward_index = 0
            for reward in range(len(qTable[casa])):
                array_rewards = qTable[casa]
                if array_rewards[reward] > max_reward:
                    max_reward = array_rewards[reward]
                    max_reward_index = reward
            pos = (int(casa[1]), int(casa[4]))
            print(casa, ":", qTable[casa])
            if(obstacles[int(casa[1])][int(casa[4])] == 0 and pos != goal and pos not in targetsL):
                if max_reward_index == 0:
                    c.execute("marrow ", "north," + casa[4] + "," + casa[1])
                elif max_reward_index == 1:
                    c.execute("marrow ", "east," + casa[4] + "," + casa[1])
                elif max_reward_index == 2:
                    c.execute("marrow ", "south," + casa[4] + "," + casa[1])
                elif max_reward_index == 3:
                    c.execute("marrow ", "west," + casa[4] + "," + casa[1])

def main():
    c = client.Client('127.0.0.1', 50001)
    res = c.connect()
    random.seed()  # To become true random, a different seed is used! (clock time)
    #reactive_example_2()

    max_coord = getMaxCoord(c)
    actions = 4
    qTable = {}
    for i in range(max_coord[0]):
        for j in range(max_coord[1]):
            qTable[str((i,j))] = [0.0] * actions

    reactive_example_2(c, res, qTable)
    u = input("")


main()
