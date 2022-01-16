import pygame
import os
import time
import random

from player import Player
from enemy import Enemy
from utils import collide

pygame.font.init()

WIDTH, HEIGHT = 650, 650

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


# Background
BG = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


def main():
    run = True
    lost = False
    lost_count = 0

    FPS = 60
    level = 0
    lives = 5

    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    player = Player(275, 530)
    enemies = []
    wave_length = 5
    enemy_vel = 1
    laser_vel = 4
    player_vel = 5

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH-level_label.get_width()-10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You  Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH/2-lost_label.get_width()/2, 325))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100),
                              random.randrange(-1500, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x - player_vel > 0:  # Left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:  # Right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:  # Up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # Down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player, HEIGHT)

            if random.randrange(0, 120) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies, HEIGHT)


def main_menu():
    title_font = pygame.font.SysFont("comicsans", 60)
    run = True

    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render(
            "Press the mouse to begin...", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH/2-title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()


main_menu()
