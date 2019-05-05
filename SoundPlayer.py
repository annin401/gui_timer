# -*- coding: utf-8 -*-
from mutagen.mp3 import MP3 as mp3
import pygame

class SoundPlayer():

    def __init__(self):
        self.filename = 'Resources/chime_sound.mp3'
        self.__play_music_times = -1 # infinite loop
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.set_volume(1.0)
        
    def play(self):
        pygame.mixer.music.play(self.__play_music_times)

    def stop(self):
        pygame.mixer.music.stop()
