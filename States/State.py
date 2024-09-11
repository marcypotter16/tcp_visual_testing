import pygame
from pygame import Rect

from Generic.Stack import Stack
from UI.Abstract import UICanvas
from Utils.Text import draw_centered_text


class State:
    def __init__(self, game, msg=None, layer="foreground"):
        self.game = game
        self.canvas: UICanvas = UICanvas(game)
        self.render_stack = Stack()
        self.prev_state = None
        self.msg = msg
        self.layer = layer

    def render(self, surface: pygame.Surface):
        surface.fill((0, 0, 0))
        self.canvas.render(surface)
        if self.msg is not None:
            draw_centered_text(self.game.font_big, surface, self.msg, (255, 255, 255), rect=Rect(
                0, 0, self.game.GAME_W, self.game.GAME_H // 2
            ))

    def update(self, delta_time):
        self.canvas.update(delta_time)

    def enter_state(self):
        if self.game.state_stack.size() > 1:
            self.prev_state = self.game.state_stack.top()  # ossia l'ultimo elemento dello stack di stati
        self.game.state_stack.push(self)
        self.game.render_stack[self.layer].append(self.render)

    def exit_state(self):
        self.game.state_stack.pop()

    def change_layer(self, layer):
        self.game.render_stack[self.layer].remove(self.render)
        self.layer = layer
        self.game.render_stack[self.layer].append(self.render)

    def change_render_index_in_layer(self, index):
        self.game.render_stack[self.layer].remove(self.render)
        self.game.render_stack[self.layer].insert(index, self.render)

    def set_above_all(self):
        self.game.render_stack[self.layer].remove(self.render)
        self.layer = "above_all"
        self.game.render_stack["above_all"].append(self.render)
