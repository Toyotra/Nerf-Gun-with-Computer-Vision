import pygame


def buttonValIncrease(image, imageClicking, mouse_pos, coords, screen, hold):
    

    if hold:
        if mouse_pos[0] >= coords[0] and mouse_pos[0] <= coords[0] + image.get_width():
            if mouse_pos[1] >= coords[1] and mouse_pos[1] <= coords[1] + image.get_height():
                screen.blit(imageClicking, (coords[0], coords[1]))
                return 1
    
    screen.blit(image, (coords[0], coords[1]))
    return 0