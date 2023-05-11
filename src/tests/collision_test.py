import unittest
import pygame

import logic.collision_detector
import sprites.player
import sprites.projectile

class TestCollisionDetector(unittest.TestCase):
    def setUp(self):
        self.player = sprites.player.Player([], 1, [1,1], [1,1])
        self.player2 = sprites.player.Player([], 2, [1,1], [0,0])
        self.game_map = [["x", "x", "x", "x"], ["x", "p1", " ", "x"], [
            "x", " ", " ", "x"], ["x", "x", "x", "x"]]
        self.projectile = sprites.projectile.Projectile()

    def test_handle_player_death(self):
        self.assertEqual(self.game_map[1], ["x", "p1", " ", "x"])
        logic.collision_detector.handle_player_death(self.game_map, self.player, self.player2, self.projectile, "p1")
        self.assertEqual(self.game_map[1], ["x", " ", " ", "x"])

    def test_flag_drops_after_player_death(self):
        self.player2.has_flag = True
        game_map = [["x", "p2", " ", "x"], ["x", " ", " ", "x"]]
        self.assertEqual(game_map[1], ["x", " ", " ", "x"])
        logic.collision_detector.handle_player_death(game_map, self.player2, self.player, self.projectile, "p2")
        self.assertEqual(game_map[1], ["x", "p1flag", " ", "x"])
