
import smtplib
import socket

#returns 1 if successful
#returns -1 if socket gaierror (Not connected to the internet)
#returns -2 if password is incorrect
def sendEmail(secEmail, secPass, userEmail, message):
	try:
		smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
		smtpObj.ehlo()
		smtpObj.starttls()
		smtpObj.login(secEmail, secPass)
		smtpObj.sendmail(secEmail, userEmail, message)
		smtpObj.quit()

	except socket.gaierror:
		smtpObj.quit()
		return -1
	except smtplib.SMTPAuthenticationError:
		smtpObj.quit()
		return -2
	return 1

#returns 1 if successful
#returns -1 if socket gaierror (Not connected to the internet)
#returns -2 if password is incorrect
#returns -3 if carrier is not recognized
def sendText(secEmail, secPass, userNumber, userCarrier, message):
	try:
		smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
		smtpObj.ehlo()
		smtpObj.starttls()
		smtpObj.login(secEmail, secPass)
		carrier = getCarrier(userCarrier)
		if carrier[0] != '@':
			return -3
		userNumber += carrier
		smtpObj.sendmail(secEmail, userNumber, message)
		smtpObj.quit()

	except socket.gaierror:
		smtpObj.quit()
		return -1
	except smtplib.SMTPAuthenticationError:
		smtpObj.quit()
		return -2
	return 1

#Helper function to return the carrier.
#returns the specified carrier else "Error"	
def getCarrier(userCarrier):
	carriers = {
		0 : "@txt.att.net",
		1 : "@myboostmobile.com",
		2 : "@comcastpcs.textmsg.com",
		3 : "@mymetropcs.com",
		4 : "@messaging.nextel.com",
		5 : "@messaging.sprintpcs.com",
		6 : "@tmomail.net",
		7 : "@vtext.com",
	}
	return carriers.get(int(userCarrier), "Error")