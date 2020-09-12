import random

def rand():
	total_no = int(input('showing total_no : '))
	lower_limit_no = int(input('lower_limit_no : '))
	upper_limit_no = int(input('upper_limit_no : '))

	for i in range(0,total_no): # generates 44 random integer values between 0 and 44.
	    n = random.randint(lower_limit_no,upper_limit_no) #integer values between 2 and 44.
	    print(n,end=' ')
rand()