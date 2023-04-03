import pygame
import services.settings
import sprites.tile
import sprites.player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()


    def update_map(self, map,p1,p2):
        for i in range(len(map)):
            for j in range(len(map[i])):
                x = j * services.settings.TILESIZE
                y = i * services.settings.TILESIZE
                if map[i][j] == "x":
                    sprites.tile.Tile((x,y),[self.visible_sprites, self.obstacle_sprites],1)
                    
                elif map[i][j] == "p1":
                    p1.pos = [j,i,]
                    p1.rect.topleft = (j*services.settings.TILESIZE,i*services.settings.TILESIZE)
                
                elif map[i][j] == "p2":
                    p2.pos = [j,i,]
                    p2.rect.topleft = (j*services.settings.TILESIZE,i*services.settings.TILESIZE)

                elif map[i][j] == "p1gu":
                    sprites.tile.Tile((x,y),[self.visible_sprites, self.obstacle_sprites],2)
                elif map[i][j] == "p1g":
                    sprites.tile.Tile((x,y),[self.visible_sprites, self.obstacle_sprites],3)
                elif map[i][j] == "p1gl":
                    sprites.tile.Tile((x,y),[self.visible_sprites, self.obstacle_sprites],4)
                elif map[i][j] == "p2gu":
                    sprites.tile.Tile((x,y),[self.visible_sprites, self.obstacle_sprites],5)
                elif map[i][j] == "p2g":
                    sprites.tile.Tile((x,y),[self.visible_sprites, self.obstacle_sprites],6)
                elif map[i][j] == "p2gl":
                    sprites.tile.Tile((x,y),[self.visible_sprites, self.obstacle_sprites],7)


    def draw_map(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        