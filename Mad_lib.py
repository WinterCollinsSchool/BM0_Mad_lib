import random

verb = (input('Please enter a verb (action word): '))
noun = (input('Please enter a noun (person, or animal): '))
adjective = (input('Please enter a adjective (Descriptor.): '))

story_nun=random.randint(1,2)

if story_nun == 1:
	print(f"The {adjective} {noun} jumped over the {verb} dog.")
else:
	print(f"The {adjective} {noun} is {verb}.")

