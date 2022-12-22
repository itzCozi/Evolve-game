# Randomly genorates a number between 0 and 2 then applys math and returns traits about the 'Love baby' based on the final number
# TODO: add intuition gene and add fitness gene and maybe a health check option and maybe add a menu where u can slect what to do with the 'Love baby'
import random

# random number gen
def random_number():
    return random.randint(0,2)
def random_number_2():
    return random.randint(0,2)
def random_number_3():
    return random.randint(0,1)
def random_number_4():
    return random.randint(0,3)

male_chromosomeY = random_number()
male_chromosomeX = random_number_2()
female_chromosomeX = random_number_3()
female_chromosomeY = random_number_4()
chromosomelst = [male_chromosomeY,male_chromosomeX,female_chromosomeX,female_chromosomeY]
love_baby_gender = []
main_subject = ""

def make_love_baby():
	main_subject = ""
	love_babyX1 = (random.choice(chromosomelst))
	love_babyY1 = (random.choice(chromosomelst))
	love_babyX2 = (random.choice(chromosomelst))
	love_babyY2 = (random.choice(chromosomelst))
	love_babyR = (random.choice(chromosomelst)) # makes sure there is always one more chromosome to determine gender
	completed_love_baby = love_babyX1, love_babyY1, love_babyX2, love_babyY2, love_babyR

	print("One love baby made.")
	print(completed_love_baby)
	completed_love_baby = main_subject
	# Gender defining the child with math!
	gender = (love_babyX1 + love_babyX2 - love_babyY1 + love_babyY2 + love_babyR)
	print(gender)

	if gender < 0:
		main_subject = "Dead"
		print("The baby died.")

	if gender > 5:
		main_subject = "Beyond human"
		print('the baby is beyond human')

	if gender < 2.5:
		love_baby_gender = 'Male'
		print("The baby was/is Male.")

	if gender > 2.5:
		love_baby_gender = 'Female'
		print("The baby was/is Female.")


make_love_baby()

