import pygame


def draw_rect_alpha(surface, color, rect, corner_radius=10):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect(), border_radius=corner_radius)
    surface.blit(shape_surf, rect)

def hex_to_rgb(hex_num: str) -> tuple[int, int, int]:
    print(tuple(int(hex_num[i : i + 2], 16) for i in (0, 2, 4)))
    return tuple(int(hex_num[i : i + 2], 16) for i in (0, 2, 4))