import helperFuncs
import textHelperFunc

filesystem = helperFuncs.createFilesystem()
if helperFuncs.checkFilesystem():
	if "y" == raw_input("Create Account? (y/n) "):
		createAccount()
else:
	helperFuncs.createAccount()

input_username = raw_input("Username: ")
input_password = raw_input("Password: ")


	

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












