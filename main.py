# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot  



def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  asteroid_field = AsteroidField()

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  updatable.add(player)
  drawable.add(player)
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  
  while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots.copy():  # Iterate over a copy to safely remove items
                if shot.collides_with(asteroid):
                   shot.kill()
                   asteroid.split() 

            if player.collides_with(asteroid):
                print("Game Over!")
                pygame.quit()
                sys.exit()
                

        
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        player.draw(screen)
        pygame.display.flip()
        

        dt = clock.tick(60) / 1000
        

  pygame.quit()


if __name__ == "__main__":
    main()
