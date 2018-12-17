import sys
import os
import configparser
import pygame
import assets
import sprites

class Game:
    def __init__(self, width = 1280,  height = 960, framerate = 60, debug = False):
        pygame.init()
        pygame.font.init()
        self._width = width
        self._height = height
        self._framerate = framerate
        self._current_fps = None
        self._time = pygame.time.Clock()
        self._debug = debug
        self.initialize()

    def initialize(self):
        #read config file
        self.config = configparser.ConfigParser()
        _path = os.path.join('assets','settings.cfg')
        self.config.read(_path)
        self._width = int(self.config['DEFAULT']['width'])
        self._height = int(self.config['DEFAULT']['height'])
        self._fullscreen = self.config['DEFAULT']['fullscreen']
        self._scale = int(self.config['DEFAULT']['scale'])
        self._key_right = self.config['CONTROLS']['key_right']
        self._key_left = self.config['CONTROLS']['key_left']
        self._key_up = self.config['CONTROLS']['key_up']
        self._key_down = self.config['CONTROLS']['key_down']
        #set_mode must be before we load any art
        self._screen = pygame.display.set_mode( (self._width,self._height) )
        if(self._fullscreen == "True"):
            pygame.display.toggle_fullscreen()
        #instantiate game object
        self.init_objects()

    def init_objects(self):
        self.background = assets.Background(self._width, self._height)
        self.middleground = assets.Middlegroung(self._width, self._height)
        self.Player = sprites.Animated(2)
        self.fps = assets.Fps()

    def run(self):
        print("App is running!")
        while True:    
            self._time.tick(self._framerate)
            self._current_fps = self._time.get_fps()
            self.process_events()
            self.draw_all()

    def draw_all(self):
        self.background.draw(self._screen)
        self.middleground.draw(self._screen)
        self.fps.draw(self._screen,self._current_fps)
        self.Player.draw(self._screen, self._width/2, self._height/2 )
        pygame.display.flip()

    def process_events(self):
        self.middleground.offset(-3.5,0)
        for event in pygame.event.get():
            if self._debug == True:
                print(event)
            if event.type == pygame.QUIT:
                print("App terminated!") 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == getattr(pygame,self._key_left):
                    print('left')           
                if event.key == getattr(pygame,self._key_right):
                    print('right')
                if event.key == getattr(pygame,self._key_up):
                    print('up')
                if event.key == getattr(pygame,self._key_down):
                    print('down')
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        
app = Game()
app.run()