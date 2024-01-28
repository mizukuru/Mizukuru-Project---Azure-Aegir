'''
Author: Richard Zhang

Date: XX June 2022

Description:
The game I will be creating will be a single-player
arcade-like game. The goal of the game will be to
achieve the highest possible score. The user will be
able to use the arrow keys to move the character around,
and the ‘z’ and ‘x’ keys to activate extra abilities
(to make the game more interesting). When playing the game,
you control a flying character, and dodge projectiles
coming at you. The projectiles emanate from a “boss”
character, which also moves around. The goal of the game
is to survive as long as possible, which will exponentially
increase your game score.

TL;DR: bullet hell game
'''

import os
import pygame
import time
import Boss
import Player
import Projectile
import Label
import PauseScreen
import UI
import SprintUI
import ShrinkUI
import Lives

pygame.init()

def main():
    '''the main logic of the code'''
    # Display
    screen = pygame.display.set_mode((1280, 950))
    pygame.display.set_caption("Mizukuru Project: The Embodiment of Azure Aegir")

    # Entities
    background = pygame.image.load("bg.jpg")
    background = pygame.transform.scale(background, (1280, 800))
    background = background.convert()
    screen.blit(background, (0,0))

    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    hit = pygame.mixer.Sound("hit2.wav")
    allSprites = pygame.sprite.OrderedUpdates()
    enemySprites = pygame.sprite.OrderedUpdates()
    bulletSprites = pygame.sprite.OrderedUpdates()
    scorecounter = Label.Label(0, (820, 40), True)
    hiscore = Label.Label(0, (870, 40), False)
    ui = UI.UI(screen)
    sprint_ui = SprintUI.SprintUI(screen)
    shrink_ui = ShrinkUI.ShrinkUI(screen)
    lives_ui = Lives.Lives(3, (825, 750))
    boss = Boss.Boss(screen)
    player = Player.Player(screen)
    allSprites.add([ui] + [sprint_ui] + [shrink_ui] + [lives_ui] + [player] + [boss] + [scorecounter] + [hiscore])
    enemySprites.add([boss])
    file = open("hiscore.txt", "r")
    for line in file:
        if(line.strip() != ""):
            hiscore.setCounter(int(line.strip()))
            break

    # ACTION
    # Assign
    clock = pygame.time.Clock()
    keepGoing = True
    lives = 3
    difficulty_increase_timer = 12
    fps_counter = 0
    iframes = 0
    endgamecounter = 0
    endgame = False
    sprint_boost = 2
    sprint_boost_cnt = 0
    fadeout = False
    pauseCheck = False
    game_start_delay = True
    gameOver = True

    # start screen
    startscreen = pygame.image.load("startmenu.jpg")
    startscreen = pygame.transform.scale(startscreen, (1280, 950))
    startscreen = startscreen.convert()
    screen.blit(startscreen, (0,0))
    pygame.display.flip()
    start = True
    pygame.mixer.music.pause()
    while(start):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                start = False
                gameOver = False
            if event.type == pygame.KEYDOWN:
                start = False
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,800,1280,100))
    pygame.mixer.music.unpause()
    # Loop
    while keepGoing:
        # Time
        clock.tick(30)

        # end of game check
        if lives <= 0:
            endgamecounter += 1
            endgame = True

        if(endgame):
            if(not fadeout):
                pygame.mixer.music.fadeout(2)
                fadeout = True
            if(endgamecounter == 2 * 30 + 15):
                keepGoing = False
                continue

        if(not endgame):
            # increase in difficulty and score check
            fps_counter += 1
            if(iframes > 0):
                iframes -= 1

            if(fps_counter == 30):
                difficulty_increase_timer -= 1
                fps_counter = 0
                scorecounter.increase_counter(int(player.getSpeed()))
                # increase the bullet amount
                bullets = boss.spawnProjectiles()
                bulletSprites.add(bullets)
                enemySprites.add(bullets)
            # increase player and boss speeds
            if(difficulty_increase_timer == 0):
                difficulty_increase_timer = 12
                boss.increaseSpeed()
                player.increaseSpeed()
                sprint_boost_cnt += 1
                if(sprint_boost_cnt == 3):
                    sprint_boost += 1
                    sprint_boost_cnt = 0

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    # pause logic
                    if event.key == pygame.K_ESCAPE:
                        pauseCheck = True
                        pygame.mixer.music.pause()
                        pauseScreen = PauseScreen.PauseScreen(screen)
                        pauseSprites = pygame.sprite.OrderedUpdates(pauseScreen)
                        allSprites.draw(screen)
                        bulletSprites.draw(screen)
                        pauseSprites.draw(screen)
                        pygame.display.flip()
                        while(pauseCheck):
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                    pauseCheck = False
                                    pauseScreen.kill()
                                    screen.blit(background, (0,0))
                                    pygame.mixer.music.unpause()
                                if event.type == pygame.QUIT:
                                    keepGoing = False
                                    pauseCheck = not pauseCheck
                                    pygame.mixer.music.unpause()
            # game start delay to prevent automatically activating abilities
            if(game_start_delay):
                time.sleep(0.2)
                game_start_delay = False

            # fluid movement and ability check
            keys_pressed = pygame.key.get_pressed()
            if(keys_pressed[pygame.K_z]):
                for cnt in range(sprint_boost):
                    if(keys_pressed[pygame.K_UP]):
                        player.move_up()
                    if(keys_pressed[pygame.K_DOWN]):
                        player.move_down()
                    if(keys_pressed[pygame.K_LEFT]):
                        player.move_left()
                    if(keys_pressed[pygame.K_RIGHT]):
                        player.move_right()
                sprint_ui.pressed()
            else:
                if(keys_pressed[pygame.K_UP]):
                    player.move_up()
                if(keys_pressed[pygame.K_DOWN]):
                    player.move_down()
                if(keys_pressed[pygame.K_LEFT]):
                    player.move_left()
                if(keys_pressed[pygame.K_RIGHT]):
                    player.move_right()
                sprint_ui.unpressed()

            if(keys_pressed[pygame.K_x]):
                if(shrink_ui.cd_over()):
                    shrink_ui.pressed()
                    player.shrink()

            # collision check
            if pygame.sprite.spritecollide(player, enemySprites, False, pygame.sprite.collide_mask):
                if(iframes == 0):
                    lives -= 1
                    lives_ui.decrease_counter()
                    iframes = 30 * 2
                    hit.play()
                    player.flicker()


            # Refresh screen
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,800,1280,100))
            screen.blit(background, (0,0))
            allSprites.update()
            bulletSprites.update()
        allSprites.clear(screen, background)
        bulletSprites.clear(screen, background)
        # The next line calls the update() method for any sprites in the allSprites group.
        allSprites.draw(screen)
        bulletSprites.draw(screen)
        pygame.display.flip()

    # gameover screen
    while(gameOver):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,1280,950))
        gameovertext = Label.Label(1, (150, 220), False)
        scorecounter.changeSize(96)
        hiscore.changeSize(96)
        scorecounter.changePos((370, 220))
        hiscore.changePos((470, 220))
        scoreGroup = pygame.sprite.OrderedUpdates([scorecounter] + [hiscore])
        scoreGroup.update()
        gameovertext.hardSetText("GAME OVER")
        scoreGroup.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = False

    # change hiscore if needed
    file.close()
    if(lives == 0):
        file = open("hiscore.txt", "w")
        user_score = scorecounter.getScore()
        user_hiscore = hiscore.getScore()
        # print(user_score, type(user_score), user_hiscore, type(user_hiscore))
        if(user_score > user_hiscore):
            file.write(str(user_score))
            print("true")
        else:
            file.write(str(user_hiscore))
            print("false")
        file.close()

    # Close the game window
    pygame.quit()

main()
