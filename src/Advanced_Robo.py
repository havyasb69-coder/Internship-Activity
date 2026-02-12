import random
import time
import os

WIDTH = 20
HEIGHT = 10
PATH_LENGTH = 80

SYMBOLS = {
    "robot": "🤖",
    "person": "👤",
    "wall": "🧱",
    "coin": "💰",
    "boss": "🚧",
    "empty": "·"
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def progress_bar(distance):
    bar_len = 30
    filled = int(bar_len * distance / PATH_LENGTH)
    return "[" + "█" * filled + "-" * (bar_len - filled) + "]"

def generate_world():
    world = []
    for y in range(HEIGHT):
        row = []
        for x in range(PATH_LENGTH + WIDTH):
            tile = random.choice([" ", " ", "P", "W", "C"])
            if x == PATH_LENGTH - 5:
                tile = "B"
            row.append(tile)
        world.append(row)
    return world

def safe(world, x, y):
    if 0 <= y < HEIGHT and 0 <= x < len(world[0]):
        return world[y][x]
    return " "

def draw(robot, world, offset, distance, score, status):
    clear()
    print(f"Progress: {progress_bar(distance)}  Distance: {distance}/{PATH_LENGTH}")
    print(f"Score: {score}  Status: {status}")
    print("-" * 40)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            wx = offset + x
            if [x, y] == robot:
                print(SYMBOLS["robot"], end=" ")
            else:
                tile = safe(world, wx, y)
                if tile == "P": print(SYMBOLS["person"], end=" ")
                elif tile == "W": print(SYMBOLS["wall"], end=" ")
                elif tile == "C": print(SYMBOLS["coin"], end=" ")
                elif tile == "B": print(SYMBOLS["boss"], end=" ")
                else: print(SYMBOLS["empty"], end=" ")
        print()
    print("-" * 40)

def countdown():
    for i in range(3, 0, -1):
        clear()
        print(f"Starting in {i}...")
        time.sleep(1)

def game():
    robot_name = input("Robot name: ") or "Robo"
    speed_choice = input("Speed level (slow/normal/fast): ").lower()

    SPEED = 0.4
    if speed_choice == "fast": SPEED = 0.15
    elif speed_choice == "slow": SPEED = 0.6

    countdown()

    world = generate_world()
    robot = [0, HEIGHT//2]
    offset = 0
    score = 0
    distance = 0
    checkpoints = []
    status = "auto-moving"

    while True:

        draw(robot, world, offset, distance, score, status)

        # auto checkpoint every 10 distance
        if distance % 10 == 0 and distance != 0 and distance not in checkpoints:
            checkpoints.append(distance)

        # random glitch
        if random.random() < 0.08:
            robot[1] += random.choice([-1, 1])
            print("⚡ Direction glitch!")
            time.sleep(0.4)

        x, y = robot
        wx = offset + x
        front = safe(world, wx + 1, y)

        # PERSON
        if front == "P":
            status = "waiting"
            print("Person ahead… waiting")
            time.sleep(1)
            robot[0] += 1

        # WALL (interactive)
        elif front == "W":
            status = "blocked"
            draw(robot, world, offset, distance, score, status)
            print("🧱 Wall ahead!")

            moved = False
            while not moved:
                move = input("Choose move (up/down/back/jump): ").lower()

                if move == "jump":
                    robot[0] += 1
                    moved = True

                elif move == "up":
                    robot[1] -= 1
                    moved = True

                elif move == "down":
                    robot[1] += 1
                    moved = True

                elif move == "back":
                    robot[0] -= 1
                    moved = True

                else:
                    print("Invalid choice. Try again.")

        # BOSS WALL
        elif front == "B":
            status = "boss wall"
            if score >= 50:
                print("Boss destroyed!")
                robot[0] += 1
                score -= 50
                time.sleep(1)
            else:
                print("Not enough score — waiting")
                time.sleep(1)
                continue

        # NORMAL MOVE
        else:
            robot[0] += 1

        robot[0] = max(0, min(robot[0], WIDTH-1))
        robot[1] = max(0, min(robot[1], HEIGHT-1))

        wx = offset + robot[0]

        # collect coin
        if safe(world, wx, robot[1]) == "C":
            score += 20
            world[robot[1]][wx] = " "

        offset += 1
        distance += 1

        if distance >= PATH_LENGTH:
            status = "finished"
            break

        time.sleep(SPEED)

    clear()
    print("🎉 VICTORY SCREEN 🎉")
    print(f"Robot: {robot_name}")
    print(f"Distance travelled: {distance}")
    print(f"Final score: {score}")
    print(f"Checkpoints: {checkpoints}")
    print("Mission complete!")

def main():
    while True:
        game()
        again = input("\nReplay? (y/n): ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
