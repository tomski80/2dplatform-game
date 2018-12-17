import pygame
import os
import appglobals

class Background:
    def __init__(self, w, h, _name = 'background.png'):
        self._w = w
        self._h = h
        self.surface = None
        self.load(_name)


    def load(self, name):
        try:
            _path = os.path.join('assets','warped','PNG','environment','layers',name)
            print(_path)
            self.surface = pygame.image.load(_path)
        except:
            print('An error has occurred while the game was loading the image' + name )
            exit(0)
        self.surface.set_colorkey(appglobals.APP_COLOR_KEY)
        self.surface = pygame.transform.scale(self.surface, (self._w,self._h))
        self.surface = self.surface.convert()

    def draw(self,_screen):
        _screen.blit(self.surface, (0,0) )

class Middlegroung(Background):
    def __init__(self, w, h, name = 'middleground.png'):
        super().__init__(w,h,name)
        self._x_offset = 0
        self._y_offset = 0
        self._temp_surf = pygame.Surface((self._w,self._h))
        self._temp_surf2 = pygame.Surface((self._w,self._h))
        self._temp_surf.set_colorkey(appglobals.APP_COLOR_KEY)
        self._temp_surf2.set_colorkey(appglobals.APP_COLOR_KEY)
        self._temp_surf = self._temp_surf.convert()
        self._temp_surf2 = self._temp_surf2.convert()

            
    def draw(self,_screen):
        dx = int(self._x_offset)
        dy = int(self._y_offset)
        # X scroll
        if dx != 0:
            if dx < 0:
                dx = self._w + dx
            fragment_right = pygame.Rect(self._w - dx, 0, self._w, self._h)
            fragment_left = pygame.Rect(0, 0 ,self._w - dx, self._h) 
            self._temp_surf.fill(appglobals.APP_COLOR_KEY)
            self._temp_surf.blit(self.surface, (dx,0), fragment_left)
            self._temp_surf.blit(self.surface, (0,0), fragment_right)
        else:
            self._temp_surf.fill(appglobals.APP_COLOR_KEY)
            self._temp_surf.blit(self.surface,(0,0))
        # Y scroll
        if dy != 0:
            if dy < 0:
                dy = self._h + dy
            fragment_bottom = pygame.Rect(0, self._h - dy, self._w, self._h)
            fragment_top = pygame.Rect(0,0,self._w,self._h - dy)
            self._temp_surf2.fill(appglobals.APP_COLOR_KEY)
            self._temp_surf2.blit(self._temp_surf,(0,0), fragment_bottom)
            self._temp_surf2.blit(self._temp_surf,(0,dy), fragment_top)
            _screen.blit(self._temp_surf2,(0,0))
        else:
            _screen.blit(self._temp_surf,(0,0))


    def offset(self,x,y):
        self._x_offset = self._x_offset + x
        self._y_offset = self._y_offset + y
        if self._x_offset > self._w:
            self._x_offset = 0
        if self._y_offset > self._h:
            self._y_offset = 0
        if self._x_offset < -self._w:
            self._x_offset = 0
        if self._y_offset < -self._h:
            self._y_offset = 0
    

class Fps:
    def __init__(self):
        self._font = pygame.font.SysFont("Arial", 30)

    def draw(self,screen,fps):
        textsurface = self._font.render(str(int(fps)),False,pygame.Color(10,255,10))
        screen.blit(textsurface,(10,10))