import pygame

class Input:
    def horizontal():
        keys=pygame.key.get_pressed()
        if keys[K_a]: return 1
        if keys[K_d]: return -1
    def vertical():
        keys=pygame.key.get_pressed()
        if keys[K_w]: return 1
        if keys[K_s]: return -1