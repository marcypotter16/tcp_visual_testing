import os.path

import pygame.draw

from Game import Game
from States.State import State
from UI.Button import TextButton, ImageButton
from UI.Entry import Entry
from UI.Label import Label
from UI.Menu import Menu
from UI.Abstract import UIContainer, UICanvas
from UI.Slider import Slider
from UI.TabsFrame import TabsFrame
from Utils.Text import draw_text


class TestState(State):
    def __init__(self, game):
        super().__init__(game)

    def render(self, surface):
        super().render(surface)
        pygame.draw.circle(surface, (255, 255, 255), self.game.mousepos, radius=5)
        draw_text(self.game.font_medium, surface, "Test State", (100, 110, 100), self.game.GAME_W / 2, 30)
        draw_text(self.game.font_medium, surface, f"{self.game.mousepos[0]}, {self.game.mousepos[1]}",
                  color=(200, 200, 200), x=0, y=0)


class UITester:
    def __init__(self, game: Game, elements: list[UICanvas]):
        self.game = game
        state = TestState(self.game)
        state.canvas = elements
        self.game.state_stack.push(state)
        while self.game.running:
            self.game.game_loop()

    def update(self):
        self.game.update()

    def render(self):
        self.game.render()


if __name__ == '__main__':
    g = Game()
    canvas = UICanvas(g)
    frame = UIContainer(parent=canvas, x=900, y=100, width=400, height=5, bg_color=(255, 255, 255))
    button = TextButton(parent=frame, fg_color=(200, 255, 255), height=50, text="Test btn")
    button.pack(side="vert", padx=10, pady=10)
    button2 = TextButton(parent=frame, fg_color=(200, 255, 255), height=50, text="Test btn 2")
    button2.pack(side="vert", padx=10, pady=10)
    button5 = TextButton(parent=frame, fg_color=(200, 255, 255), height=50, text="Test btn 5")
    button5.pack(side="vert", padx=10, pady=10)

    frame2 = UIContainer(parent=canvas, x=50, y=100, width=400, height=50, bg_color=(255, 255, 255))
    print(frame2.width)
    button3 = TextButton(parent=frame2, fg_color=(200, 255, 255), width=380, text="Test btn")
    button3.pack(side="horiz", padx=10, pady=10)
    print(frame2.width)
    button4 = TextButton(parent=frame2, fg_color=(200, 255, 255), width=380, text="Test btn 2")
    button4.pack(side="horiz", padx=10, pady=10)

    # frame3 = UIContainer(parent=canvas, x=500, y=250, width=400, height=50, bg_color=(255, 255, 255))
    # for i in range(10):
    #     b = TextButton(parent=frame3, fg_color=(200, 255, 255), height=50, text=f"Test btn {i+1}")
    #     b.pack(side="vert", padx=10, pady=10)

    menu = Menu(parent=canvas, x=500, y=250, width=400, bg_color=(100, 100, 100), height=50,
                options=["Wela", "Ciao", "Salve"])

    image2 = pygame.image.load(os.path.join(g.base_dir, "Assets/sprites/ui", 'settings.png')).convert_alpha()
    # image2 = pygame.image.load(os.path.join(g.base_dir, "Assets/sprites/ui", 'Open Menu.png'))
    settings_images = []
    for i in range(8):
        image = pygame.image.load(os.path.join(g.base_dir, "Assets/sprites/ui", f"settings{i}.png")).convert_alpha()
        settings_images.append(image)
    settings_images.insert(0, image2)
    img_button = ImageButton(parent=canvas, x=100, y=300, width=100, height=100, hover_animation=settings_images,
                             animation_fps=30)

    label = Label(parent=canvas, x=100, y=200, width=400, height=50, fg_color=(255, 255, 255), text="Label")
    entry = Entry(parent=canvas, x=200, y=400, width=400, height=50, fg_color=(0, 0, 0), focus_color=(255, 255, 255),
                  placeholder="Enter smth...")
    psw_label = Label(parent=canvas, x=200, y=500, width=400, height=50, fg_color=(255, 255, 255), text="Password:")
    psw_entry = Entry(parent=canvas, x=200, y=550, width=400, height=50, focus_color=(255, 255, 255), is_password=True)

    tabs: dict[str, UIContainer] = {}
    tab1 = UIContainer(parent=canvas)
    label1 = Label(parent=tab1, center=tab1.rect.center, fg_color=(255, 255, 255), width=300, height=50, text='Tab 1')
    tab2 = UIContainer(parent=canvas)
    label2 = Label(parent=tab2, center=tab1.rect.center, width=300, height=50, text='Tab 2')
    tabs['Tab one'] = tab1
    tabs['Tab two'] = tab2
    tabs_frame = TabsFrame(parent=canvas, x=700, y=500, width=400, height=300, fg_color=(255, 255, 255), tabs=tabs)

    slider = Slider(parent=canvas, x=700, y=400, width=400, height=50, fg_color=(255, 255, 255),
                    bg_color='transparent')
    # button2.y += 40
    # print(button)
    # print(button2)
    ui_tester = UITester(g, [canvas])
