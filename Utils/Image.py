import pygame.image


def images_from_spritesheet(path: str, tilesize: tuple[int, int]) -> list[pygame.image]:
    """
    Very useful function that returns a list of images based on a tiled spritesheet.
    You can use for example Aseprite to create an animation, then export the animation as a spritesheet,
    and finally use this function to get all the frames at once, without needing to crop or export single frames.
    :param path: path of the spritesheet
    :param tilesize: a tuple of 2 ints, representing the width and height of each frame in the animation
    :return: a list of the images (pygame images) of the animation.
    """
    x = y = 0
    full_img = pygame.image.load(path).convert_alpha()
    max_x, max_y = full_img.get_rect().size
    images: list[pygame.image] = []
    while y < max_y:
        while x < max_x:
            subsurface_rect = pygame.rect.Rect((x, y), tilesize)
            image = full_img.subsurface(subsurface_rect)
            images.append(image)
            x += tilesize[0]
        x = 0
        y += tilesize[1]
    return images
