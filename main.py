import helperFuncs
import textHelperFunc
import getpass


if not helperFuncs.performInitChecks():
	exit()
print "Starting..."
print 


print "----------WELCOME----------"
print "1 - Create Account"
print "2 - Login"
option = int(raw_input("Enter an option: "))
if option == 1:
	helperFuncs.createAccount()
elif option == 2:
	if helperFuncs.loginMain() == 1:
		helperFuncs.mainMenu()
else: 
	exit()












