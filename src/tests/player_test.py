import unittest
import pygame
import sprites.player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        display = pygame.display.set_mode((4,4))
        pygame.init()
        self.player = sprites.player.Player([],1)
        self.player2 = sprites.player.Player([],2)
        self.player.pos = [1,1]
        self.player.real_pos = [1,1]
        self.player2.pos = [1,1]
        self.player2.real_pos = [1,1]
        self.game_map = [["x","x","x","x"],["x"," "," ","x"],["x"," "," ","x"],["x","x","x","x"]]

    def test_player_default_position(self):
        self.assertEqual(self.player.pos, [1,1])
        self.assertEqual(self.player.real_pos, [1,1])

    def test_player_move_up(self):
        self.player.pos = [2,2]
        self.player.real_pos = [2,2]
        self.player.move(self.game_map,"up")
        self.assertEqual(self.player.pos, [2,1])
        self.assertEqual(self.player.real_pos, [2,2])

    def test_player_move_down(self):
        self.player.move(self.game_map,"down")
        self.assertEqual(self.player.pos, [1,2])
        self.assertEqual(self.player.real_pos, [1,1])

    def test_player_move_left(self):
        self.player.pos = [2,2]
        self.player.real_pos = [2,2]
        self.player.move(self.game_map,"left")
        self.assertEqual(self.player.pos, [1,2])
        self.assertEqual(self.player.real_pos, [2,2])

    def test_player2_move_right(self):
        self.player2.move(self.game_map,"right")
        self.assertEqual(self.player2.pos, [2,1])
        self.assertEqual(self.player2.real_pos, [1,1])

    def test_playe2r_cannot_move_up(self):
        self.player2.move(self.game_map,"up")
        self.assertEqual(self.player.pos, [1,1])
        self.assertEqual(self.player.real_pos, [1,1])

    def test_player2_cannot_move_down(self):
        self.player2.pos = [2,2]
        self.player2.real_pos = [2,2]
        self.player2.move(self.game_map,"down")
        self.assertEqual(self.player2.pos, [2,2])
        self.assertEqual(self.player2.real_pos, [2,2])

    def test_player_cannot_move_left(self):
        self.player2.move(self.game_map,"left")
        self.assertEqual(self.player2.pos, [1,1])
        self.assertEqual(self.player2.real_pos, [1,1])

    def test_player2_cannot_move_right(self):
        self.player2.pos = [2,2]
        self.player2.real_pos = [2,2]
        self.player2.move(self.game_map,"right")
        self.assertEqual(self.player2.pos, [2,2])
        self.assertEqual(self.player2.real_pos, [2,2])

    def test_apply_real_position(self):
        self.player.move(self.game_map,"down")
        self.assertEqual(self.player.real_pos, [1,1])
        self.player.apply_real_position()
        self.assertEqual(self.player.real_pos, [1,2])