import helperFuncs

input_username = "breadle"
input_password = "password"

if helperFuncs.checkUser(input_username, input_username) > 0:
	print "Successful"