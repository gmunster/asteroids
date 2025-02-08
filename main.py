# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

clock = pygame.time.Clock()
dt = 0



def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  running = True
  while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000

  pygame.quit()


if __name__ == "__main__":
    main()
