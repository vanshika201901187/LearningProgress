def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear() and not wall_in_front():
        move()
    else: 
        turn_left()
        
        
        
 # Link to game: https://reeborg.ca/index_en.html
