def dash():
    while wall_on_right():
        while wall_in_front():
            turn_left()
        move()


def turn_right():
    for i in range(0, 3):
        turn_left()


while not at_goal():
    dash()
    turn_right()
    if at_goal():
        break
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front():
        turn_right()
    move()
