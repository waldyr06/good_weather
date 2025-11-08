import pygame
import threading

def tocar_som():
    def _tocar():
        pygame.mixer.init()
        pygame.mixer.music.load("pomodoro/sounds/trovao.mp3")
        pygame.mixer.music.play()
    
    # toca em outra thread para não travar o Tkinter
    threading.Thread(target=_tocar, daemon=True).start()