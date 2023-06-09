import unittest
import pygame

import services.level
import logic.game_loop


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        0


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        display = pygame.display.set_mode((1, 1))
        level = services.level.Level()
        events = [StubEvent(pygame.KEYDOWN, pygame.K_LEFT),]
        event_queue = StubEventQueue(events)
        clock = StubClock()
        self.loop = logic.game_loop.GameLoop(
            level, display, event_queue, clock)

    def test_first_turn(self):
        self.assertEqual(self.loop.current_turn, 1)

    def test_change_turns_works(self):
        self.loop.change_turns()
        self.assertEqual(self.loop.current_turn, 2)
        self.loop.change_turns()
        self.assertEqual(self.loop.current_turn, 3)
        self.loop.change_turns()
        self.assertEqual(self.loop.current_turn, 4)
        self.loop.change_turns()
        self.assertEqual(self.loop.current_turn, 5)
        self.loop.change_turns()
        self.assertEqual(self.loop.current_turn, 1)

    def test_handle_player_positions_works(self):
        self.loop.player1.pos = 0
        self.loop.player1.real_pos = 1
        self.loop.player1.rendering_pos = 2
        self.loop.handle_player_positions()
        self.assertEqual(self.loop.player1.rendering_pos, 0)
        self.loop.current_turn = 3
        self.loop.handle_player_positions()
        self.assertEqual(self.loop.player1.rendering_pos, 1)
