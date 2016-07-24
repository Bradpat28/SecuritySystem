import helperFuncs
import textHelperFunc

input_username = "username"
input_password = "password"

if helperFuncs.checkUser(input_username, input_password) > 0:
	print "Successful"

print "1 - Send a Text"
print "2 - Send an Email"
print "3 - Send a Text and Email"
print "0 - No Notifications"
textOrEmail = raw_input("Enter option: ")
simMovement = raw_input("Simulate Movement? (y/n) ")
if simMovement == 'y':
	if helperFuncs.simMovement(textOrEmail) == 1:
		print "Success"
	else:
		print "Failure"

