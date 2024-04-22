import pygame
import random
import time
import psycopg2

from game_object import GameObject
from game_object import Point  
from worm import Worm
from food import Food
from wall import Wall

def check_user_exists(username):
    """Check if the user exists in the database and retrieve their current level."""
    try:
        with psycopg2.connect(host="localhost", database="snake", user="postgres", password="123") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT username, level FROM users WHERE username = %s", (username,))
                return cur.fetchone()  # Returns (username, level) if user exists, None otherwise
    except psycopg2.Error as e:
        print("Database error:", e)
        return None

def insert_user(username):
    """Insert a new user into the database with level 1."""
    try:
        with psycopg2.connect(host="localhost", database="snake", user="postgres", password="123") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (username, level) VALUES (%s, %s)", (username, 1))
                conn.commit()
    except psycopg2.Error as e:
        print("Database error:", e)

def insert_score(username, level, score):
    """Insert the user's score into the user_scores table."""
    try:
        with psycopg2.connect(host="localhost", database="snake", user="postgres", password="123") as conn:
            with conn.cursor() as cur:
                # Get the user_id corresponding to the username
                cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
                user_id = cur.fetchone()[0]
                # Insert the score into the user_scores table
                cur.execute("INSERT INTO user_scores (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
                conn.commit()
    except psycopg2.Error as e:
        print("Database error:", e)

# Game setup
def create_background(screen, width, height):
    colors = [(255, 255, 255), (212, 212, 212)]
    tile_width = 20
    y = 0
    while y < height:
        x = 0
        while x < width:
            row = y // tile_width
            col = x // tile_width
            pygame.draw.rect(screen, colors[(row + col) % 2], pygame.Rect(x, y, tile_width, tile_width))
            x += tile_width
        y += tile_width

# Game loop
def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # Prompt the user to enter their username
    username = input("Enter your username: ")

    # Check if the user exists
    user_data = check_user_exists(username)
    if user_data:
        print("Welcome back, {}! Your current level is {}".format(user_data[0], user_data[1]))
    else:
        print("Welcome, {}! Starting at level 1.".format(username))
        insert_user(username)
        user_data = (username, 1)  # Default to level 1 if user is new

    foodPoints = [Point(120, 20)]

    worm = Worm(20)
    food = Food(20, foodPoints)
    wall = Wall(20)

    score = 0
    level = user_data[1]  # Get the user's current level

    foodColors = [(100, 255, 100), (0, 140, 0), (0, 0, 0)]  # list of food colors
    foodWeight = 1  # starting food weight and color
    foodColor = foodColors[foodWeight - 1]

    def generateFood():
        # function to generate new food and delete old
        if food.can_eat(worm.points[0]):
            x1 = food.eat_points(worm.points[0]).X
            y1 = food.eat_points(worm.points[0]).Y

            index = 0  # finding the index of old food to pop
            for x in foodPoints:
                if x.X == x1 and x.Y == y1:
                    break
                else:
                    index += 1

        while True:  # checking for intersection with worm and walls
            p1 = random.randrange(0, 39) * 20
            p2 = random.randrange(0, 29) * 20

            warmCheck = False
            wallsCheck = False

            for x in worm.points:
                if x.X == p1 and x.Y == p2:
                    warmCheck = True

            for x in wall.points:
                if x.X == p1 and x.Y == p2:
                    wallsCheck = True

            if not warmCheck and not wallsCheck:
                break

        foodPoints.pop()  # foodPoints.pop(index) for many foods on the screen
        foodPoints.append(Point(p1, p2))

        return 0

    l1, l2, l3 = True, True, True  # flags for next levels

    TimerActive = False  # timer flag
    TimerStart = 0

    paused = False  # Flag to indicate if the game is paused

    while True:
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pause the game when "P" key is pressed
                    paused = not paused  # Toggle the pause state
                else:
                    filtered_events.append(event)

        if paused:
            # Display pause message and wait until game is unpaused
            # Optionally, you can display a message on the screen indicating the game is paused
            continue  # Skip the rest of the game loop if paused

        worm.process_input(filtered_events)
        worm.move()

        eaten = False
        pos1 = food.can_eat(worm.points[0])
        if pos1 is not None:
            worm.increase(pos1)
            score += foodWeight
            eaten = True

            if (score == 5 or score == 6 or score == 7) and l1:  # switching to next levels
                wall.next_level()
                level += 1
                l1 = False
            elif (score == 10 or score == 11 or score == 12) and l2:
                wall.next_level()
                level += 1
                l2 = False
            elif (score == 15 or score == 16 or score == 17) and l3:
                wall.next_level()
                level += 1
                l3 = False

        if foodWeight == 3:  # 3 second timer for black food
            if not TimerActive:
                TimerActive = True
                TimerStart = time.time()

            currentTime = time.time()
            elapsedTime = currentTime - TimerStart
            if elapsedTime >= 3:
                generateFood()
                TimerActive = False

        if eaten:
            eaten = False

            foodWeight = random.randrange(1, 4)  # generating new food weight (1-3)
            foodColor = foodColors[foodWeight - 1]

            generateFood()

        pos2 = wall.collision(worm.points[0])
        if pos2 is not None:
            insert_score(username, level, score)
            break

        create_background(screen, 800, 600)

        food.draw(screen, foodColor)
        wall.draw(screen)
        worm.draw(screen)

        font = pygame.font.Font(None, 35)  # displaying score and level info
        scoreTxt = font.render(str(score), True, "black")
        levelTxt = font.render(str(level), True, "black")
        screen.blit(scoreTxt, [760, 20])
        screen.blit(levelTxt, [20, 20])

        pygame.display.flip()
        clock.tick((level * 3) + 5)  # increasing speed by 3 for every next level

    # Close the game
    pygame.quit()

if __name__ == "__main__":
    main()
