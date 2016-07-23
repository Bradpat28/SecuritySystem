def checkUser(userName, password):
	if len(userName) < 6:
		print "Invalid UserName"
		return -1
	return 1