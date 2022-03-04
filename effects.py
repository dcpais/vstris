from PIL import Image, ImageFilter, ImageEnhance
import PIL
import pygame

"""
Simple visual effects library using PIL to manipulate 
pygame surfaces. Made for the purposes of Vstris
"""

def surf_to_image(surface: pygame.Surface) -> Image:
    """
    Converts pygame surface into PIL image
    """
    return Image.frombytes("RGBA", surface.get_size(), 
        pygame.image.tostring(surface, "RGBA", False))


def image_to_surf(image: Image) -> pygame.Surface:
    """
    Converts PIL image to pygame surface
    """
    return pygame.image.fromstring(image.tobytes(), image._size, "RGBA")


def blur_surface(surface: pygame.Surface, r: float) -> pygame.surface:
    """
    Blurs a pygame surface with Gaussian Blur a
    """
    return image_to_surf(surf_to_image(surface)
        .filter(ImageFilter.GaussianBlur(radius = r)))


def surf_brightness(surface: pygame.Surface, factor: float) -> pygame.Surface:
    """
    Adjusts a pygame surface's brightness given a factor:
            FACTOR -> 1.0 gives the original image 
                      & 0.0 gives a black image

    """
    _ = ImageEnhance.Brightness(surf_to_image(surface))
    _ = _.enhance(factor)
    return image_to_surf(_)


def surf_hue(surface: pygame.Surface, colour: str) -> pygame.Surface:
    """
    Adjusts the hue of a pygame surface given a hue colour:
            COLOUR -> 
    """
    raise NotImplementedError


def adjust_alpha(surface: pygame.Surface, amount: int) -> pygame.Surface:
    """
    adjust's the alpha of a pygame surface by 'amount', based on the current
    alpha of the surface.
            AMOUNT -> number between -255 <-> 255
    """
    if not 0 <= surface.get_alpha() + amount <= 255:
        alpha = 0 if surface.get_alpha() + amount < 0 else 255
    else:
        alpha = surface.get_alpha() + amount
    surface.set_alpha(alpha)
    return surface



