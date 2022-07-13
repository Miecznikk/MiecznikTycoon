import src.misc.colors as colors
import pygame

class Button:
    def __init__(self,size,font,color,bgcolor,text,position):
        self.font = font
        self.size = size
        self.color = color
        self.bgcolor = bgcolor
        self.text_label = text
        self.position = position
        self.text = self.font.render(self.text_label,True,self.color)
        self.text_rect = self.center_text()

    def center_text(self):
        text_rect = self.text.get_rect()
        rect = (self.position[0] + ((self.position[0] + self.size[0] - self.position[0]) - text_rect.width)//2
                ,self.position[1])
        return rect

class Game:
    running = False
    state = None
    window_size = None
    buttons = []

    def __init__(self,window_size):
        pygame.init()
        pygame.font.init()
        self.mainfont = pygame.font.SysFont('Arial',60)
        self.buttonfont = pygame.font.SysFont('Arial',35)
        self.init_menu_buttons()
        self.window_size = window_size
        self.screen = pygame.display.set_mode(self.window_size)
        self.running = True
        self.state = 'menu'
        self.clock = pygame.time.Clock()

    def init_menu_buttons(self):
        self.buttons.append(Button((200,40),self.buttonfont,colors.white,(0,0,0),'QUIT',(300,300)))

    def draw_menu(self):
        self.screen.fill(colors.dgray)
        for button in self.buttons:
            pygame.draw.rect(self.screen,button.bgcolor,
                             [button.position[0],button.position[1],button.size[0],button.size[1]])
            self.screen.blit(button.text,button.text_rect)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if self.state == 'menu':
                self.draw_menu()
            pygame.display.update()
        self.clock.tick(60)


