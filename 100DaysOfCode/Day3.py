# Treasure Island

print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')

print("Welcome to Treasure Island! \nYour mission is to find the treasure.")
crossroad = input("You are at a crossroad. Do you want to go left or right?").lower()
if crossroad == "left":
    river = input("You've reached a lake. There is an island in the middle of the lake. Do you want to swim across or wait for a boat?").lower()
    if river == "wait":
        door = input("You've reached the island unharmed. There is house with 3 colored doors- red, yellow, and blue. "
                     "Which door would you like to enter?").lower()
        if door == "red":
            print("You got burned by fire. Game over.")
        elif door == "yellow":
            print("You win!")
        elif door == "blue":
            print("You got eaten by beasts. Game over.")
        else:
            print("Game Over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")
