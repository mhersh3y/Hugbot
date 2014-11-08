import random

# HUGBOT_NAME = 'HENRIETTA'

boot_options = [True, False]

hugbot_actions = ["hug", "wave","quit", "pet the dog"]


def speak(message):
	print message

def hug():
	speak("*hug*")

def wave():
	speak("*wave*")

# def what_pet():
# 	pet = raw_input("WHAT?! what am i petting?!")

def pet_thing(raw_input):
	speak("the"+ raw_input+" wags its tail and jumps excitedly")

def get_name():
	return HUGBOT_NAME


def perform_action(verb):
	speak(bot_name+" " +verb+"s")


def boot():
	HUGBOT_NAME = raw_input("What is hugbots name? ")
	bot_name = HUGBOT_NAME
	if bot_name == '':
		return False
	else:
		speak("BEEEP BOOOP BOOOPP BOOP BEEEEP ALGORITHYM HACKING INTO THE MAINFRAME")
		speak("Hello, my name is " + bot_name)
		return bot_name
		# choice = random.choice(boot_options)
		# return choice
		# return True bot_name #in the first half of this lesson we retunred True, not bot_name
		# random.choice(boot_options)



def brain():
	bot_name = boot()
	if boot:
		# action = random.choice(hugbot_actions)
		running = True
		while running ==True:
			action = raw_input("What should "+bot_name+" do?")
			if action == 'hug':
				hug()
				# running = True  ###### I can actually leave this out!
			elif action =='wave':
				wave()
				# running = True
			elif action =='pet the dog':
				pet = raw_input("what did you want me to pet?!")
				pet_thing(pet)

			elif action =='quit':
				running = False
			else:
				speak(action)
				# perform_action(action)
				# running = Truew
	else:
		speak("system failure :( ")





brain()

