import pygame
import services.settings
import sprites.tile
import sprites.player
import sprites.flag

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.flag_1 = sprites.flag.Flag((4, 5), [self.visible_sprites], 1)
        self.flag_2 = sprites.flag.Flag((11, 5), [self.visible_sprites], 2)

    def create_map(self):
        game_map = services.settings.MAP
        height = len(game_map)
        width = len(game_map[0])
        for i in range(height):
            for j in range(width):
                x_coordinate = j * services.settings.TILESIZE
                y_coordinate = i * services.settings.TILESIZE
                if game_map[i][j] == "x":
                    sprites.tile.Tile((x_coordinate, y_coordinate), [self.visible_sprites, self.obstacle_sprites], 1)
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

    def update_map(self, game_map, player_one, player_two):
        height = len(game_map)
        width = len(game_map[0])
        for i in range(height):
            for j in range(width):
                x_coordinate = j * services.settings.TILESIZE
                y_coordinate = i * services.settings.TILESIZE
                if game_map[i][j] == "p1":
                    if player_one.has_flag:
                        self.flag_2.current_position = [j,i,]
                        self.flag_2.rect.topleft = (x_coordinate, y_coordinate)
                    player_one.pos = [j, i,]
                    player_one.rect.topleft = (x_coordinate, y_coordinate)
                elif game_map[i][j] == "p2":
                    if player_two.has_flag:
                        self.flag_1.current_position = [j,i,]
                        self.flag_1.rect.topleft = (x_coordinate, y_coordinate)
                    player_two.pos = [j, i,]
                    player_two.rect.topleft = (x_coordinate, y_coordinate)
                elif game_map[i][j] == "p1flag":
                    self.flag_1.current_position = [j,i,]
                    self.flag_1.rect.topleft = (x_coordinate, y_coordinate)
                elif game_map[i][j] == "p2flag":
                    self.flag_2.current_position = [j,i,]
                    self.flag_2.rect.topleft = (x_coordinate, y_coordinate)

        self.all_sprites.add(self.visible_sprites,self.obstacle_sprites)

    def draw_map(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
