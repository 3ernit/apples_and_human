from world import World

world = World(4, 6, 6, ".", "*", "|")

score = 0
moves = 0

while True:
    world.border()
    world.screen.clear()
    world.screen_props()
    print(world.screen.get_str())
    print("Score: " + str(score) + " Type command here: ", end="")
    tusk = input()
    match tusk:
        case "up":
            world.human.move(0, -1)
        case "down":
            world.human.move(0, 1)
        case "left":
            world.human.move(-1, 0)
        case "right":
            world.human.move(1, 0)
        case "exit":
            break
    score += 1 if world.is_collide() else 0
    moves += 1
    if score == world.apple_count:
        print("You won!\n"
              "You have done it in " +str(moves) + " moves!")
        break
input()