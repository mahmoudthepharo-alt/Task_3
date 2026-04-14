def move_player(position, direction):
    x, y = position

    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "right":
        x += 1
    elif direction == "left":
        x -= 1
    else:
        return None

    return (x, y)


x = int(input("Enter the x coordinate: "))
y = int(input("Enter the y coordinate: "))

while True:
    direction = input("Enter the direction to move (up, down, left, right): ")

    if direction == "exit":
        print("Exiting the game.")
        break

    new_position = move_player((x, y), direction)

    if new_position is None:
        print("Invalid direction!")
    else:
        x, y = new_position
        print("New position:", (x, y))