import pygame
from constants import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_clock = pygame.time.Clock()
updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
Player.containers = (updatables, drawables)
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

def game_loop():
    delta_time = 0
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        player.update(delta_time)
        pygame.display.flip()
        delta_time = (game_clock.tick(60)/1000)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop()


if __name__ == "__main__":
    main()
