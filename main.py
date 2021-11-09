# importeer de Game en Learn objecten
from game import Game
from learn import Learn
from learn2 import Learn2
from os import system

MINSCORE = 7

# de App class
class App:
	def __init__(self):
		self.game : Game = Game(host=self)
		self.learn : Learn = None
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
			
		print(f"Welcome {username.title()} from group {group}!\n")
		self.username = username.title()
		self.group = group

		ans = input("Do you want to do maths or spelling? [m/s]: ").lower()
		while not ans in ['m', 's']:
			print("Invalid answer, try again.") 
			ans = input("Do you want to do maths or spelling? [m/s]: ").lower()
		print()
		
		if ans == 'm':
			self.learn = Learn(host=self)
		elif ans == 's':
			self.learn = Learn2(host=self)

	def run(self):
		"""run het programma"""

		# de regel hieronder is nu even een comment voor het testen
		self.learn.run()
		# self.learn.current_score = 7 # deze regel is tijdelijk

		print(f"Done! You have {self.learn.current_score} points and {self.learn.mistakes} mistakes.")

		# hier bepalen we of de speler het spel mag spelen
		if self.learn.current_score >= MINSCORE:
			print("This means you can play the game!")
			self.game.run()
		else:
			print(f"You need {MINSCORE} points to play the game. Too bad!")

		# deze methode returned een waarde die zegt of de speler
		# opnieuw wilt spelen
		return input("\nDo you want to go again? [yes/no]: ").lower() == "yes"

# dit zorgt ervoor dat de App
# alleen start als we specifiek
# dit script uitvoeren
if __name__ == "__main__":

	while True:
		system("clear") # maak het scherm schoon
		app = App()
		app.login()
		app.learn.configure(app.group)

		if not app.run():
			print("Goodbye!")
			break
		print()