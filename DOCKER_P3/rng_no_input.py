from random import randint

def func(min_number, max_number):
  if (max_number < min_number): 
    print('Invalid input - shutting down...')
  else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number)

func(1,2)
func(4,2)