# return -1 if username is less than 6 chars
# return -2 if password is less than 6 chars 
# return -3 if special chars in username 
# return -4 if special chars in password 
# return 1  if successful 


def checkuser(username,password):
	if len(username) < 6 : 
		return -1
	if len(password) < 6 :
		return -2 
	chars = set("!@#$%^&*?,<>':;+=") 
	if any((c in chars) for c in username): 
		return -3 
	if any((c in chars) for c in password): 
		return -4 
	else:
		return 1
