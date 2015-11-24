import random

sChoice='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789012345678901234567890123456789'
for i in range(1, 100):
	s=''
	for j in range(0, 7): 
		s+=random.choice(sChoice)
	print(s)