import arcade
from settings.universalVariables import *

class AudioHandler:
    ''' Import arcade.Sound objects and manage them '''
    def __init__(self, music = [], sounds = []):
        self.music = music
        self.sounds = sounds
        self.music_player = None
        self.sound_player = None

    def playMusic(self, music):
        self.music_player = self.music[music].play(MUSIC_VOLUME)

    def stopMusic(self):
        self.music_player.delete()

    def playSound(self, sound):
        self.sound_player = self.sounds[sound].play(SOUND_VOLUME)

    def pauseMusic(self):
        if self.music_player.playing:
            self.music_player.pause()
        else:
            self.music_player.play()
    
    def pauseSound(self):
        if self.sound_player.playing:
            self.sound_player.pause()
        else:
            self.sound_player.play()

    def pauseAllSound(self):
        self.pauseMusic()
        self.pauseSound()
    
    def setLoop(self, music, loop):
        self.music[music].loop = loop

    def stopSound(self):
        self.sound_player.delete()

    def addMusic(self, music, stream=False):
        self.music.append(arcade.Sound(music, stream))

    def addSound(self, sound):
        self.sounds.append(arcade.Sound(sound))

    def removeMusic(self, music):
        self.music.pop(music)

    def removeSound(self, sound):
        self.sound.pop(sound)

    def getMusicList(self):
        return self.music
    
    def getSoundList(self):
        return self.sounds
    
    def clearMusic(self):
        self.music = [] 

    def clearSounds(self):
        self.sounds = []

