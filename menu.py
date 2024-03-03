import pygame

class Button():
    # Constructor
    def __init__(self, x, y, btn_w, btn_h):
        self.rect = pygame.Rect(x, y, btn_w, btn_h)

    # Draw Func
    def draw(self, surface, color):
        pygame.draw.rect(surface, color,self.rect)

    # Draw Text
    def text(self, txt, surface, size):
        font = pygame.font.SysFont(None, size)
        text_surf = font.render(txt, True, (0,0,0))
        surface.blit(text_surf, text_surf.get_rect(center = self.rect.center))

    # Status Var
    active = False
        
class Text():
    # Constructor
    def __init__(self, x, y, txt_w, txt_h):
        self.rect = pygame.Rect(x, y, txt_w, txt_h)

    # Draw Func
    def draw(self, surface, bg_color = (0,0,0)):
        pygame.draw.rect(surface, bg_color,self.rect)

    # Draw Text
    def text(self, txt, surface,  color, size):
        font = pygame.font.SysFont(None, size)
        text_surf = font.render(txt, True, color)
        surface.blit(text_surf, text_surf.get_rect(center = self.rect.center))


class IconButton():
    # Constructor
    def __init__(self, x, y, btn_w, btn_h):
        self.rect = pygame.Rect(x, y, btn_w, btn_h)

    # Draw Func
    def draw(self, surface, color):
        pygame.draw.rect(surface, color,self.rect)

    # Draw Text
    def icon(self, image, btn_w, btn_h, surface):
        img = pygame.image.load(image).convert_alpha()
        image_scale = pygame.transform.scale(img, (btn_w, btn_h))
        surface.blit(image_scale, image_scale.get_rect(center = self.rect.center))

    # Status Var
    active = False