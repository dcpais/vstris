from PIL import Image, ImageFilter, ImageEnhance
import PIL
import pygame

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
                   -> 0.0 gives a black image

    """
    _ = ImageEnhance.Brightness(surf_to_image(surface))
    _ = _.enhance(factor)
    return image_to_surf(_)




