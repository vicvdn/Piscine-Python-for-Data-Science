import sys

def what_is(argv) -> int:
	if (len(argv) > 2):
		print("AssertionError: more than one argument is provided")
		return 1
	if (len(argv) < 2):
		return 1
	try: 
		number = int(argv[1])
	except ValueError:
		print("AssertionError: argument is not an integer")
		return 1

	if (number % 2 == 0) :
		print("I'm Even.")
	else :
		print("I'm Odd.")
	return 0

what_is(sys.argv)