
print('Welcome to Treasure Island. \nYour mission is to find the treasure.')
print('You are at a cross road. Where do you want to go? Type "left" or "right"?')
Direction = input()
direction = Direction.lower()
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    print('Type "wait" to wait for a boat. Type "swim" to swim across.')
    Swim = input()
    swim = Swim.lower()
    if swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print("One red, one yellow and one blue. Which colour do you choose?")
        Color = input()
        color = Color.lower()
        if color == "yellow":
            print("You found the treasure! You Win!")
        elif color == "blue":
            print("You enter a room of beasts. Game Over.")
        elif color == "red":
            print("It's a room full of fire. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
