from PIL import Image, ImageFilter
import PIL
import pygame

def surf_to_image(surface: pygame.Surface) -> Image:
    """
    Converts pygame surface into PIL image
    """
    size = surface.get_size()
    string = pygame.image.tostring(surface, "RGBA", False)
    return Image.frombytes("RGBA", size, string)


def image_to_surf(image: Image) -> pygame.Surface:
    """
    Converts PIL image to pygame surface
    """
    string = image.tobytes()
    size = image._size
    return pygame.image.fromstring(string, size, "RGBA")


def blur_surface(surface: pygame.Surface, r: float) -> pygame.surface:
    """
    Blurs a pygame surface with Gaussian Blur a
    """
    image = surf_to_image(surface)
    imageCopy = image.copy()
    image = image.filter(ImageFilter.GaussianBlur(radius = r))

    return image_to_surf(image)



