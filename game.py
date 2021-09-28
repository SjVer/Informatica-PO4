import pygame as pg
from main import App

DISPLAY_SIZE = (600, 600)

class Game:
  def __init__(self, host: App):
    """ maak een nieuwe Game instance """
    self.host: App = host
    self.DISPLAY = None
    self.is_running: bool = False


  def start(self):
    """start de game"""
    pg.init()
    self.is_running = True
    self.DISPLAY = pg.display.set_mode(DISPLAY_SIZE)

  def quit(self):
    """stop de game"""
    self.DISPLAY = None
    self.is_running = False
    pg.quit()