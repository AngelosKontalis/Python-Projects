import sys
import numpy as np
import pygame
import pygame.gfxdraw
import random


pygame.init()
pygame.display.init()
screen_size = 1080, 720
screen = pygame.display.set_mode(screen_size)
fps = 240
clock = pygame.time.Clock()

black = 0
color_a = 0x282d3f

rnd_color = ["0x"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
color_m = int(rnd_color[0],16)



square_size = 7

rows, cols = int(screen_size[1] / square_size), int(screen_size[0] / square_size)

grid = np.zeros((rows, cols), dtype=np.uint8)
print(f"\n{grid}\n")
print(
    f"Screen size: {screen_size[0]}x{screen_size[1]}\n"
    f"Square size: {square_size}\n"
    f"Grid size: {grid.shape[1]}x{grid.shape[0]}")


class Ant:
    ANT_UP = 0
    ANT_RIGHT = 1
    ANT_DOWN = 2
    ANT_LEFT = 3

    def __init__(self, position, direction: int, ):
        self.position: list[int] = [int(position[0]), int(position[1])]
        self.direction = direction
        

    def turn_right(self):
        self.direction += 1
        self.direction %= 4

    def turn_left(self):
        self.direction -= 1
        self.direction %= 4

    def on_zero(self):
        # print("Checking square color")
        # print(not grid[self.position[1]][self.position[0]])
        return not grid[self.position[1], self.position[0]]

    def switch_color(self):
        # print("Switching color")
        grid[self.position[1], self.position[0]] = not grid[self.position[1], self.position[0]]
        
        
    
    def move(self):
        if self.direction == self.ANT_UP:
            self.position[1] -= 1
        elif self.direction == self.ANT_RIGHT:
            self.position[0] += 1
        elif self.direction == self.ANT_DOWN:
            self.position[1] += 1
        elif self.direction == self.ANT_LEFT:
            self.position[0] -= 1

        if self.position[0] > cols - 1:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = cols - 1

        if self.position[1] > rows - 1:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = rows - 1

    def step(self):
        if self.on_zero():
            # print("Left")
            self.turn_right()
            self.switch_color()
            self.move()
        else:
            # print("Right")
            self.turn_left()
            self.switch_color()
            self.move()


def display(surface):
  
    
    x, y = 0, 0
    for row in grid:
        for col in row:
            if col:
                pygame.draw.rect(surface, color_m, (x, y, square_size, square_size))
            x += square_size
        y += square_size
        x = 0


def draw_grid():
    for x in range(0, screen_size[0], square_size):
        pygame.gfxdraw.vline(screen, x, 0, screen_size[1], (0, 0, 0))
    for y in range(0, screen_size[1], square_size):
        pygame.gfxdraw.hline(screen, 0, screen_size[0], y, (0, 0, 0))

a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)
d = random.randint(0,100)
e = random.randint(0,100)
f = random.randint(0,100)
g = random.randint(0,100)
h = random.randint(0,100)
popo = random.randint(0,3)


ant = Ant((a, b), 1)


ant1 = Ant((c,d), 2)
ant2 = Ant((e,f), 3)
ant3 = Ant((g,h), 4)


def main():
    steps = 0




    while True:
        clock.tick(fps)

        if (popo==0):
            ant.step()
        elif (popo==1):
            ant.step()
            ant1.step()
        elif (popo==2):
            ant.step()
            ant1.step()
            ant2.step()
        elif (popo==3):
            ant.step()
            ant1.step()
            ant2.step()
            ant3.step() 
            
        # Exit on ESCAPE key press or if the user presses the X button on the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE:
                print(steps)
                sys.exit("bye")

        
 
        screen.fill(color_a)
        display(screen)
        draw_grid()
        pygame.display.flip()
        pygame.display.set_caption(f"Langton's ant ({round(clock.get_fps())}/{fps} fps)")
        steps += 1

   
      

if __name__ == "__main__":
    main()
