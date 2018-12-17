import pygame
import os
import appglobals

#animated sprite class
class Animated:
    def __init__(self, scale):
        self._anims = { 'empty' : None }
        self._scale = scale
        self.load('player-idle.png', 4)
        self.load('player-run.png', 10)
        self.frame = 0
        
    def load(self, name, frames = 1):
        dict_name = name.split('.')[0]
        print(dict_name)
        try:
            _path = os.path.join('assets','warped','PNG','spritesheets','player', name)
            self._anims[dict_name] = pygame.image.load(_path)
        except:
            print('An error has occurred while the game was loading the image ' + name )
            exit(0)
        self._anims[dict_name].set_colorkey(appglobals.APP_COLOR_KEY)
        #calculate scale based on resolution
        surf_w, surf_h = self._anims[dict_name].get_size()
        #calculate rect size for frame
        frame_rect_w = int( surf_w / frames ) * self._scale
        print(frame_rect_w)
        for i in range(frames):
            self._anims[dict_name+'_frame_'+str(i)] = ( pygame.Rect( frame_rect_w * i, 0, frame_rect_w, surf_h * self._scale ) )    
        self._anims[dict_name] = pygame.transform.scale(self._anims[dict_name], (surf_w * self._scale,surf_h * self._scale))
        self._anims[dict_name] = self._anims[dict_name].convert()
    
    def draw(self, screen, pos_x , pos_y):
        self.frame = self.frame + 0.2
        if self.frame > 9:
            self.frame = 0
        #screen.blit(self._anims['player-idle'], (pos_x, pos_y), self._anims['player-idle_frame_'+str(int(self.frame))])
        screen.blit(self._anims['player-run'], (0, 0), self._anims['player-run_frame_'+str(int(self.frame))])
        