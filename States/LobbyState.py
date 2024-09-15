from cgitb import text
from matplotlib import container
from pygame import Surface, Vector2, Vector3, image
from States.State import State
from UI.Abstract import UIContainer, UIElement
from UI.Label import Label
from UI.Entry import Entry
from UI.Button import ImageButton
from UI.Containers import VertContainer
from Utils.Draw import hex_to_rgb


class LobbyState(State):
    def __init__(self, game, msg=None, layer="foreground"):
        super().__init__(game, msg, layer)

        # Set the font
        self.chat_msg_font = self.game.font_medium
        self.entry_msg_font = self.game.font_medium

        # Create UI elements

        # Create a container for the chat messages
        CHAT_CONTAINER_WIDTH = 1000
        CHAT_CONTAINER_HEIGHT = self.game.GAME_H - 200
        ALIAS_LABEL_WIDTH = 100
        PADDING = 5
        x, y, w, h = (
            self.game.GAME_W // 2 - 0.5 * CHAT_CONTAINER_WIDTH,
            20,
            CHAT_CONTAINER_WIDTH,
            CHAT_CONTAINER_HEIGHT,
        )
        container_bg_color = Vector3(1) * 20
        self.chat_container = VertContainer(
            self.canvas, x, y, width=w, height=h, bg_color=container_bg_color
        )
        self.chat_container.padding = Vector2(5, 5)

        msg_entry_pos = (self.game.GAME_W // 2, CHAT_CONTAINER_HEIGHT + 100)
        self.msg_entry = Entry(
            self.canvas,
            center=msg_entry_pos,
            width=CHAT_CONTAINER_WIDTH // 2,
            height=50,
            placeholder="Enter message",
            corner_radius=10,
        )

        def enter_btn_command():
            text_label = Label(self.canvas, text=self.msg_entry.text,
                               height=self.chat_msg_font.size(" ")[1],
                               font=self.chat_msg_font,
                               width=CHAT_CONTAINER_WIDTH - ALIAS_LABEL_WIDTH - 2 * PADDING,
                               fg_color=(255, 255, 255))
            alias_label = Label(self.canvas, text="You", bg_color=hex_to_rgb("28E247"), fg_color=(0,0,0),
                                height=self.chat_msg_font.size(" ")[1],
                                width=ALIAS_LABEL_WIDTH,
                                font=self.chat_msg_font)
            group = UIElement(self.canvas, bg_color=(0, 0, 0), width=CHAT_CONTAINER_WIDTH, height=text_label.height)
            group.add_child(alias_label)
            group.add_child(text_label)
            self.chat_container.add_child(
                group
            )
            text_label.rect.x = group.rect.x + ALIAS_LABEL_WIDTH + PADDING
            text_label.rect.y = group.rect.y
            alias_label.rect.x = group.rect.x + PADDING
            alias_label.rect.y = group.rect.y
            self.msg_entry.clear_text()

        self.msg_entry.set_enter_key_callback(enter_btn_command)

        img = image.load(self.game.assets_dir +
                         "/sprites/ui/send_msg_small.png")
        hov_img = image.load(
            self.game.assets_dir + "/sprites/ui/send_msg_small_hover.png"
        )
        pad_x = 10
        enter_btn_pos = (
            self.game.GAME_W // 2
            + self.msg_entry.width * 0.5
            + img.get_rect().width * 0.5
            + pad_x,
            self.msg_entry.y,
        )

        self.enter_btn = ImageButton(
            self.canvas,
            x=enter_btn_pos[0],
            y=enter_btn_pos[1],
            width=50,
            height=50,
            bg_color="transparent",
            command=enter_btn_command,
            hover_animation=[img],
            mouse_pressed_image=hov_img,
            animation_fps=10,
        )

    def render(self, surface: Surface):
        return super().render(surface)

    def update(self, dt: float):
        return super().update(dt)
