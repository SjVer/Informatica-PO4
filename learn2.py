from random import randint, choice

class Learn2:
	def __init__(self, host):
		self.host = host
		self.current_score = 0
		self.mistakes = 0
		self.questions: list = []


	def configure(self, group):
		"""hier wordt bepaald welke vragen er
		gesteld gaan worden enzo"""
	
		self.questions.clear()

		words = []
		with open("words.txt", 'r') as f:
			for word in f.read().split("\n"):
				if len(word) > (4 if group < 5 else 5 if group < 6 else 6):
					words.append(word)

		for _ in range(10 if group < 6 else 15):
			word = choice(words)
			words.remove(word)
			self.questions.append(word)

	def run(self):
		"""run the learn2 app"""
		unasked = self.questions.copy()

		while len(unasked): # zelfde als "while len(unasked) > 0"

			question = unasked.pop(randint(0, len(unasked) - 1))
			print(f"question {len(self.questions) - len(unasked)}/{len(self.questions)}:")

			letters = list(question)
			# indices = []
			
			# group = self.host.group
			# for _ in range(1 if group < 5 else 2 if group < 6 else 3):
			# 	rand = randint(0, len(letters) - 1)
			# 	while rand in indices:
			# 		rand = randint(0, len(letters) - 1)	
			# 	indices.append(rand)
			
			# for index in indices:
			index = randint(0, len(letters) - 1)
			letters[index] = "_"
			
			print("".join(letters) + " = ", end='')
			answer = input()
			
			if answer == question:
				self.current_score += 1
				print(f"correct! ({self.current_score} points)")
			else:
				self.mistakes += 1
				print(f"wrong! The answer was {question}. ({self.mistakes} mistakes)")
			print()