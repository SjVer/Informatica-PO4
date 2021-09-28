# importeer de Game en Learn objecten
from game import Game
from learn import Learn

# de App class
class App:
  def __init__(self):
    self.game : Game = Game(self)
    self.learn : Learn = Learn(self)
    self.username : str = ""
    self.group : int = 0

  def login(self):
    username = input("Enter your name: ")
    group = False
    # we herhalen dit tot we een nummer hebben
    while not group:
      try:
        group = int(input("Enter your group: "))
        # alleen groep 4 tot en met 6       
        if group < 4 or group > 6:
          group = False
          print("Invalid group! (Not a number from 4 to 6)")
      except ValueError:
        print("Invalid group! (Not a number from 4 to 6)")
      
    print(f"Welcome {username.title()} from group {group}!")
    self.username = username.tite()
    self.group = group

    # zorg ervoor dat het Learn gedeelte weet
    # welke vragen die moet stellen enzo
    self.learn.configure()

  def run(self):
    """run het programma"""
    self.learn.run()

# dit zorgt ervoor dat de App
# alleen start als we specifiek
# dit script uitvoeren
if __name__ == "__main__":
  app = App()
  app.login()
  app.run()