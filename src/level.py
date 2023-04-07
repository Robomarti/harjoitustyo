import pygame
import settings
import sprites.tile
import sprites.player


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def update_map(self, game_map, player_one, player_two):
        height = len(game_map)
        width = len(game_map[0])
        for i in range(height):
            for j in range(width):
                x_coordinate = j * settings.TILESIZE
                y_coordinate = i * settings.TILESIZE
                if game_map[i][j] == "x":
                    sprites.tile.Tile((x_coordinate, y_coordinate), [self.visible_sprites, self.obstacle_sprites], 1)
                elif game_map[i][j] == "p1":
                    player_one.pos = [j, i,]
                    player_one.rect.topleft = (j*settings.TILESIZE, i*settings.TILESIZE)
                elif game_map[i][j] == "p2":
                    player_two.pos = [j, i,]
                    player_two.rect.topleft = (j*settings.TILESIZE, i*settings.TILESIZE)
                elif game_map[i][j] == "p1gu":
                    sprites.tile.Tile((x_coordinate, y_coordinate), [self.visible_sprites], 2)
                elif game_map[i][j] == "p1g":
                    sprites.tile.Tile((x_coordinate, y_coordinate), [self.visible_sprites], 3)
                elif game_map[i][j] == "p1gl":
                    sprites.tile.Tile((x_coordinate, y_coordinate), [self.visible_sprites], 4)
                elif game_map[i][j] == "p2gu":
                    sprites.tile.Tile((x_coordinate, y_coordinate), [self.visible_sprites], 5)
                elif game_map[i][j] == "p2g":
                    sprites.tile.Tile((x_coordinate, y_coordinate), [self.visible_sprites], 6)
                elif game_map[i][j] == "p2gl":
                    sprites.tile.Tile((x_coordinate, y_coordinate), [self.visible_sprites], 7)

        self.all_sprites.add(self.visible_sprites,self.obstacle_sprites)

    def draw_map(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
