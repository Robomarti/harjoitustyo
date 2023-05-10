import unittest
import pygame

import services.level
import sprites.player

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = services.level.Level()
        self.game_map = [["x", "p1flag", "p2flag", "x"]]
        self.player = sprites.player.Player([], 1, [1, 1], [1, 1])
        self.level.create_map(self.game_map, None, None)

    def test_reset_flag1(self):
        self.game_map[0][1] = " "
        self.assertEqual(self.game_map, [["x", " ", "p2flag", "x"]])
        self.level.reset_flag1(self.player)
        self.assertEqual(self.game_map, [["x", "p1flag", "p2flag", "x"]])

    def test_reset_flag2(self):
        self.game_map[0][2] = " "
        self.assertEqual(self.game_map, [["x", "p1flag", " ", "x"]])
        self.level.reset_flag2(self.player)
        self.assertEqual(self.game_map, [["x", "p1flag", "p2flag", "x"]])
