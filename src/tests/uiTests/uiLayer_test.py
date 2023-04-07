import unittest
import ui.uiLayer
import pygame


class TestUiLayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((64, 64))

    def test_ui_Text_Returns_None_If_Valid_Input(self):
        valid_input = ui.uiLayer.showText("moi", 10, 10)
        self.assertEqual(valid_input, None)

    def test_ui_text_returs_None_even_with_weird_input(self):
        weird_input = ui.uiLayer.showText(pygame.display, 10, 10)
        self.assertEqual(weird_input, None)
