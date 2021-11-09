from random import randint, choice

class Learn:
	def __init__(self, host):
		self.host = host
		self.current_score = 0
		self.mistakes = 0
		self.questions: list = []


	def configure(self, group):
		"""hier wordt bepaald welke vragen er
		gesteld gaan worden enzo"""
	
		self.questions.clear()

		if group >= 5:
			ops = ['+', '-', '*']
		else:
			ops = ['+', '-']

		for _ in range(10):

			rand = randint(0 if group < 6 else -10, 10)
			rand2 = randint(0 if group < 6 else -10, 10)
			operation = ' ' + choice(ops) + ' '
			self.questions.append(str(rand) + operation + str(rand2))

		# deel vragen
		if group >= 6:
			for _ in range(5):
				a = randint(1, 10)
				b = randint(1, 10)
				# a * b = c -> c / a = b
				c = a * b
				self.questions.append(str(c)+' / '+str(a))

	def run(self):
		"""run the learn app"""
		unasked = self.questions.copy()

		while len(unasked): # zelfde als "while len(unasked) > 0"

			question = unasked.pop(randint(0, len(unasked) - 1))
			print(f"question {len(self.questions) - len(unasked)}/{len(self.questions)}:")

			answer = False
			# we herhalen dit tot we een nummer hebben
			while answer == False and type(answer) == bool:  
				try:
					answer = int(input(question + " = "))
				except ValueError:
					print("Invalid answer! (Not a number)")

			if answer == eval(question):
				self.current_score += 1
				print(f"correct! ({self.current_score} points)")
			else:
				self.mistakes += 1
				print(f"wrong! The answer was {eval(question)}. ({self.mistakes} mistakes)")

			print()