import pygame
pygame.init()
font = pygame.font.Font(None,30)

def showText(text, y=20, x=640):  #osa youtube tutoriaalia: https://www.youtube.com/watch?v=QU1pPzEGrqw jossain n. 5min jälkeen
    display_surface = pygame.display.get_surface()
    failed = False
    try:
        text_surface = font.render(str(text), True, "White")
    except:
        text_surface = font.render(str("unvalid input"), True, "White")
        failed = True
    text_rectangle = text_surface.get_rect(center = (x,y))
    pygame.draw.rect(display_surface, "Black", text_rectangle)
    display_surface.blit(text_surface, text_rectangle)
    if failed:
        return False