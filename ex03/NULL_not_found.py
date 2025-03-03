
def NULL_not_found(object: any) -> int:
	
	if (type(object) == type(None)):
		print(f"Nothing: {object} {type(object)}")
	elif (type(object) == type(float("NaN"))):
		print(f"Cheese: {object} {type(object)}")
	elif (type(object) == type(0)):
		print(f"Zero: {object} {type(object)}")
	elif (type(object) == type("")):
		if (len(object) > 0):
			print("Type not Found")
			return 1
		print(f"Empty: {object}{type(object)}")
	elif (type(object) == type(False)):
		print(f"Fake: {object} {type(object)}")
	else :
		print("Type not Found")
		return 1
	return 0
