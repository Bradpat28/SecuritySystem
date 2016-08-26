#This is a file full of helper function used throughout the program
import textHelperFunc
import time
import getpass
import os


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

def createAccount():
	print "Creating Account..."
	new_username = raw_input("Enter a Username: ")
	new_password = raw_input("Enter a Password: ")
	if checkUser(new_username, new_password) > 0:
		print "Account Creation Successful"
	else:
		print "Unable to Create Account"
		exit()

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

def checkFilesystem():
	path = os.getcwd() + "/.securesys/filesystem.txt"
	return not (os.stat(path).st_size == 0)


















