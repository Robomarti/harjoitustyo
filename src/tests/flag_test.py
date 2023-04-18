import unittest
import pygame
import sprites.flag

class TestFlag(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        display = pygame.display.set_mode((4,4))
        pygame.init()
        self.flag = sprites.flag.Flag((0,0), [], 3)

    def test_setup(self):
        self.assertEqual(self.flag.original_position, (0,0))
        self.assertEqual(self.flag.current_position, [0,0])