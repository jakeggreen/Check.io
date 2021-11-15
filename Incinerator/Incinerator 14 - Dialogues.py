"""The modern world is filled with means of communication - the social networks, messengers, phone calls, SMS etc. But sometimes in every communication channel a flaw can be detected and in the moments like that you think to yourself: "I should create my own messenger which won’t have problems like this one".
In this mission you’ll get your chance.
Your task is to create a Chat class which could help a Human(name) and Robot(serial_number) to make a conversation. This class should have a few methods:
connect_human() - connects human to the chat.
connect_robot() - connects robot to the chat.
show_human_dialogue() - shows the dialog as the human sees it - as simple text.
show_robot_dialogue() - shows the dialog as the robot perceives it - as the set of ones and zeroes. To simplify the task, just replace every vowel ('aeiouAEIOU') with "0", and the rest symbols (consonants, white spaces and special signs like ",", "!", etc.) with "1".
Dialog for the human should be displayed like this:
(human name) said: message text
(robot serial number): message text
For the robot:
(human name) said: 11100100011
(robot serial number) said: 100011100101
Interlocutors should have a send() method for sending messages to the dialog.
In this mission you could use the Mediator design pattern.

Input: Interlocutors and the text of messages.

Output: A dialog (the multiline string)."""

import re

vowels = "aeiou"

class Chat:

	def show_robot_dialogue(self):
		robot_messages = []
		human_messages = []

		for message in self.Robot.message:
			robot_message = re.sub(r'[aeiou]', '0', re.sub(r'[^aeiou]', '1', message))
			robot_messages.append(robot_message)

		for message in self.Human.message:
			human_message = re.sub(r'[aeiou]', '0', re.sub(r'[^aeiou]', '1', message))
			human_messages.append(human_message)

		for h_message, r_message in zip(human_messages, robot_messages):
			return f'{self.Human.name} said: {h_message}\n{self.Robot.name} said: {r_message}'

	def show_human_dialogue(self):
		# robot_messages = []
		# human_messages = []
		# final_message = []

		# for message in self.Robot.message:
		# 	robot_messages.append(message)

		# for message in self.Human.message:
		# 	human_messages.append(message)

		# for r_message, h_message in zip(robot_messages, human_messages):
		# 	final_message.append(f'{self.Human.name} said: {h_message}\n{self.Robot.name} said: {r_message}\n')
		
		# print(''.join(final_message))
		# return ''.join(final_message)
		return self.message

	def connect_robot(self, Messenger):
		self.Robot = Messenger

	def connect_human(self, Messenger):
		self.Human = Messenger

class Messenger():
	def __init__(self):
		message = []
		
	def send(self, text):
		message.append(f'{self.name} said: {text}\n')

class Human(Messenger):
	def __init__(self, name):
		super().__init__()
		self.name = name

class Robot(Messenger):
	def __init__(self, name):
		super().__init__()
		self.name = name

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing

	chat = Chat()
	karl = Human("Karl")
	bot = Robot("R2D2")
	chat.connect_human(karl)
	chat.connect_robot(bot)
	karl.send("Hi! What's new?")
	bot.send("Hello, human. Could we speak later about it?")
	print(chat.show_robot_dialogue())
	print(chat.show_human_dialogue())
	assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
	assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

	print("Coding complete? Let's try tests!")

	chat = Chat()
	bob = Human('Bob')
	ann = Robot('Ann-1244c')
	chat.connect_human(bob)
	chat.connect_robot(ann)
	bob.send("Hi, Ann! Is your part of work done?")
	ann.send("Hi, Bob. Sorry, I need a few more hours. Could you wait, please?")
	bob.send("Ok. But hurry up, please. It's important.")
	ann.send("Sure, thanks.")
	assert chat.show_human_dialogue() == "Bob said: Hi, Ann! Is your part of work done?\nAnn-1244c said: Hi, Bob. Sorry, I need a few more hours. Could you wait, please?\nBob said: Ok. But hurry up, please. It's important.\nAnn-1244c said: Sure, thanks."
