import pygame

class Button():
    # Constructor
    def __init__(self, x, y, btn_w, btn_h):
        self.rect = pygame.Rect(x, y, btn_w, btn_h)

    # Draw Func
    def draw(self, surface, color):
        pygame.draw.rect(surface, color,self.rect)

    # Draw Text
    def text(self, txt, surface,  size, color =(0,0,0)):
        font = pygame.font.SysFont('Calibri', size)
        text_surf = font.render(txt, True, color)
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
    def text(self, txt, surface,  size, color,  centered = True):
        font = pygame.font.SysFont(None, size)
        text_splitted = txt.split('\n')
        new_txt = []
        x = self.rect.centerx 
        y = self.rect.centery - self.rect.height / 3.5
        for sentence in text_splitted:
            text_surf = font.render(sentence, True, color)
            if centered:
                new_txt.append([text_surf, (text_surf.get_rect(center = self.rect.center))])
            else:
                new_txt.append([text_surf, (text_surf.get_rect(center = (x,y)))])
                y+=size
           
        surface.blits(new_txt)

    # Status Var
    active = False

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


class CicleButton():
    # Constructor
    def __init__(self, x, y, btn_w, btn_h):
        self.rect = pygame.Rect(x, y, btn_w, btn_h)

    # Draw Func
    def draw(self, surface, color, size):
        pygame.draw.circle(surface, color,self.rect.center, size )

    # Draw Text
    def text(self, txt, surface,  size, color =(0,0,0)):
        font = pygame.font.SysFont('Calibri', size)
        text_surf = font.render(txt, True, color)
        surface.blit(text_surf, text_surf.get_rect(center = self.rect.center))

    # Status Var
    active = False

class Mixer():

    def __init__(self):
        self.mixer = pygame.mixer
        