import time
import random
from time import sleep



def start_motivation(time, train_type):
	print( "Hello! \nWelcome to the trainig. You chose the {} minutes {} training. \
Remember, be strong and never give up! When it hurts - it grows! \nSo let's start!".format(time, train_type))


def warmup(time):
	warmup_4min = ['wrist rolling', 'arms rolling', 'hips rolling', 'knees rolling', 'head rolling']
	print('\nWarmup starts, it will take you {} minutes to finish:\n'.format(time))
	#sleep(1)
	for a in range(len(warmup_4min)):
		print(warmup_4min[a])
		#sleep(1)


def cardio(time):
	print('\nCardio part starts, it will take you {} minutes to finish:\n'.format(time))
	cardio_exc = {'jumping jacks':1, 'knees up':1, 'boxing run':1, 'jumping wide-narrow':1}
	exc_time = time

	while exc_time > 0:
		#print (exc_time)
		exc = random.choice(list(cardio_exc.keys()))
		exc_value = cardio_exc[exc]
		exc_time = exc_time - exc_value
		if exc_time <0:
			break
		print(exc)
		if exc_value == 1:
			print(exc_value, 'minute \n')
		else:
			print(exc_value, 'minutes \n')


def print_exc_value_plural_or_not(exc_value):
	if exc_value == 1:
		print(exc_value, 'minute \n')
	else:
		print(exc_value, 'minutes \n')


def excercises(time):	
	exc_time = time

	abss = {'30 sit ups':1, '50 Lying Floor Leg Raise':2, '50 Crunches':2 }
	legs = {'50 squats':1, '25 half squats with jump':1, '20 (side) leg extension':1}
	arms = {'30 standard pushups':1, '30 pushups narrow':1, '30 pushups wide':1, '30 diamond pushups':1}
	calf = {'Standing calf raise':1}
	backs = {'50 back raising lying':1}
	glutes = {'20 (side) leg raise from front support':1, '20 (side) Lunges':1 }

	if exc_time == 3:
		body_parts = [abss, legs, arms]
	elif exc_time == 10:
		body_parts = [abss, legs, arms, calf, backs, glutes, abss, legs, arms, abss]
	else:
		body_parts = [abss, backs]


	body_parts_number = 0	
	while exc_time > 0:
		#print (exc_time)
		
		exc = random.choice(list(body_parts[body_parts_number].keys()))
		exc_value = body_parts[body_parts_number][exc]
		exc_time = exc_time - exc_value
		if exc_time <0:
			break

		print(exc)
		print_exc_value_plural_or_not(exc_value)

		body_parts_number += 1


def other_excercises(time, train_type):
	if train_type == 'karate':
		karate_exc(time)
	else:
		universal_exc(time)


def karate_exc(time):
	print('\nKarate part starts, it will take you {} minutes to finish:\n'.format(time))

	kihon = {'50 seiken chudan tsuki':1, '40 maygeri':1, '30 gedan barai':1, '30 uchi uke':1, '30 soto uke':1, '30 jodan uke':1}
	kata = {'taikyoku kata sono ichi':2, 'taikyoku kata sono ni':2, 'pinan kata sono ichi':2, 'pinan kata sono ni':2, 'seipai kata':2}

	exc_time = time

	if exc_time == 2:
		karate_parts = [kihon, kihon]
	else:
		karate_parts = [kata, kihon, kihon, kihon, kata, kihon, kihon, kihon, ]

	karate_parts_number = 0	
	while exc_time > 0:
		#print (exc_time)
		
		exc = random.choice(list(karate_parts[karate_parts_number].keys()))
		exc_value = karate_parts[karate_parts_number][exc]
		exc_time = exc_time - exc_value
		if exc_time <0:
			break

		print(exc)
		print_exc_value_plural_or_not(exc_value)

		karate_parts_number += 1


def universal_exc(time):
	print('\nUniversal part starts, it will take you {} minutes to finish:\n'.format(time))
	excercises(time)


def end_training():
	print(10*'#','\nCongratulations! You menaged to finish the trainig! I hope you enjoyed it, so see you soon!')


def training_time_scheme(time):

	if time == 15:
		warmup_time = 4
		cardio_time = 5
		excercises_time = 3
		other_time = 2
		
	elif time == 30:
		warmup_time = 4
		cardio_time = 6
		excercises_time = 10
		other_time = 10
		
	else:
		print('There is no training for this duration of time')
	
	return [warmup_time, cardio_time, excercises_time, other_time]


def training(time, train_type):
	start_motivation(time, train_type)
	#sleep(1)

	train = training_time_scheme(time)
	[warmup_time, cardio_time, excercises_time, other_time] = train

	warmup(warmup_time)
	#sleep(1)
	cardio(cardio_time)
	#sleep(1)
	print('\nStandard excercises part starts, it will take you {} minutes to finish:\n'.format(time))
	excercises(excercises_time)
	#sleep(1)
	other_excercises(other_time, train_type)
	
	end_training()



training(30, 'karate')
training(15, 'jakiś_trening')
