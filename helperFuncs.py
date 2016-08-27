#This is a file full of helper function used throughout the program
import textHelperFunc
import time
import getpass
import os
import csv


# return -1 if username is less than 6 chars
# return -2 if password is less than 6 chars 
# return -3 if special chars in username 
# return -4 if special chars in password 
# return 1  if successful 
def checkUser(username,password):
	if len(username) < 6 : 
		return -1
	if len(password) < 6 :
		return -2 
	chars = set("!@#$%^&*?,<>':;+=") 
	if any((c in chars) for c in username): 
		return -3 
	if any((c in chars) for c in password): 
		return -4 
	
	return 1

def createAccount(username, password):
	print "Creating Account..."
	if checkUser(username, password) > 0:
		with open('./.securesys/fileSystem.csv', 'w') as csvfile:
			fieldnames = ['first_name', 'last_name']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
			writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
			writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
		print "Account Creation Successful"
	else:
		print "Unable to Create Account"
		exit()

def loginMain():
	input_username = raw_input("Username: ")
	input_password = getpass.getpass("Password: ")
	csvFile = open('./.secureSys/fileSystem.csv')
	reader = csv.DictReader(csvFile)
	for row in reader:
		if row["Username"] == input_username:
			if row["Password"] == input_password:
				print "Login Successful"
				return 1
			print "Invalid Password"
			return -1
	print "User not Found"
	return -2

def mainMenu():
	print
	print "---------Main Menu---------"
	print "1 - Send a Text"
	print "2 - Send an Email"
	print "3 - Send a Text and Email"
	print "0 - No Notifications"
	textOrEmail = raw_input("Enter option: ")
	simMovementInput = raw_input("Simulate Movement? (y/n) ")
	if simMovementInput == 'y':
		if simMovement(textOrEmail) == 1:
			print "Success"
		else:
			print "Failure"

def simMovement(notification):
	if int(notification) == 0:
		return 1
	EmailUserName = raw_input("Enter the sending email: ")
	EmailPassword = getpass.getpass("Enter the sending password: ")
	if int(notification) == 2:
		EmailSendTo = raw_input("Enter the email to send to: ")
		message = "Subject: Movement Detected at " + time.strftime("%H:%M:%S") + "\nThere was movement detected on the security cam."
		print "Sending Email..."
		return textHelperFunc.sendEmail(EmailUserName, EmailPassword, EmailSendTo, message)
	
	TextNumber = raw_input("Enter the phone number to send to: ")
	print "0 - AT@T"
	print "1 - Boost Mobile"
	print "2 - Comcast"
	print "3 - MetroPCS"
	print "4 - Nextel"
	print "5 - Sprint"
	print "6 - T Mobile"
	print "7 - Verizon"
	UserCarrier = raw_input("Enter the number of your carrier: ")
	if int(notification) == 1:
		print "Sending Text..."
		message = "Subject: Movement Detected at " + time.strftime("%H:%M:%S") + "\nThere was movement detected on the security cam."
		return textHelperFunc.sendText(EmailUserName, EmailPassword, TextNumber, UserCarrier, message)
	
	EmailSendTo = raw_input("Enter the email to send to: ")
	print "Sending Email..."
	message = "Subject: Movement Detected at " + time.strftime("%H:%M:%S") + "\nThere was movement detected on the security cam."
	retE = textHelperFunc.sendEmail(EmailUserName, EmailPassword, EmailSendTo, message)
	if retE != 1:
		print "There was an error sending the Email CODE :(" + retE + ")"
	print "Sending Text..."
	retT = textHelperFunc.sendText(EmailUserName, EmailPassword, TextNumber, UserCarrier, message)
	if retT != 1:
		print "There was an error sending the Text CODE: (" + retT + ")"
	if retE != 1 or retT != 1:
		return -4
	return 1


#
# Not currently used, using a bash script instead to initialize the System
#
def createFilesystem(): 
	print "Creating FileSystem..."
	path = os.getcwd() + "/.securesys"
	if not os.path.exists(path):
		os.makedirs(path)
		print "Created File System Directory..."
	os.chdir(path)
	if not os.path.exists("filesystem.txt"):
		print "File does not exist"
		newfile = open("filesystem.txt", 'w')
	else:
		newfile = open("filesystem.txt", 'r+')
	print "Opened File System File - 'filesystem.txt'..."
	os.chdir("..")
	return newfile
#
# Not currently used, using a bash script instead to initialize the System
#
def checkFilesystem():
	print "--Checking FileSystem.......................",
	try:
		path = os.getcwd() + "/.securesys/fileSystem.csv"
		return not (os.stat(path).st_size == 0)
	except OSError:
		return False

def performInitChecks():
	print "Performing Init Checks..."
	if not checkFilesystem():
		print "Failed"
		print "Failed Init Checks"
		return False
	print "Passed"
	print "Init Checks Complete"
	return True














