import random
from main import App

class Learn:
  def __init__(self, host: App):
    self.host = host
    self.current_score = 0
    self.mistakes = 0
    self.questions: list = []

  def configure(self):
    """hier wordt bepaald welke vragen er
    gesteld gaan worden enzo"""
    # hier moeten de vragen (sommen) bepaald worden
    # en toegevoegd worden aan de lijst self.questions
    # met behulp van "self.questions.append(vraag)"

    # bijv.: self.questions.append("1+1")

  def run(self):
    """run the learn app"""
    while True:
      # main loop


    # einde