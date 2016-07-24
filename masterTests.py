import unittest
import helperFuncs


class TestUserAuthenicationMethods(unittest.TestCase):
	def test_username_char_count(self):
		badUser = "bad"
		goodUser = "bradley"
		lineUser = "6chars"
		randPass = "Password"
		self.assertEquals(helperFuncs.checkUser(badUser, randPass), -1)
		self.assertEquals(helperFuncs.checkUser(goodUser, randPass), 1)
		self.assertEquals(helperFuncs.checkUser(lineUser, randPass), 1)
	def test_password_char_count(self):
		badPass = "bad"
		goodPass = "Password"
		linePass = "6chars"
		randUser = "bradley"
		self.assertEquals(helperFuncs.checkUser(randUser, badPass), -2)
		self.assertEquals(helperFuncs.checkUser(randUser, goodPass), 1)
		self.assertEquals(helperFuncs.checkUser(randUser, linePass), 1)
	def test_user_invalid_char(self):
		badUser = "asggf"
		badChars = "!@#$%^&*?,<>':;+="
		randPass = "Password"
		for c in badChars:
			badUser += c
			self.assertEquals(helperFuncs.checkUser(badUser, randPass), -3)
			badUser = badUser[:-1]
	def test_pass_invalid_char(self):
		badPass = "asggf"
		badChars = "!@#$%^&*?,<>':;+="
		randUser = "Username"
		for c in badChars:
			badPass += c
			self.assertEquals(helperFuncs.checkUser(randUser, badPass), -4)
			badPass = badPass[:-1]

if __name__ =='__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestUserAuthenicationMethods)
	unittest.TextTestRunner(verbosity=1).run(suite)
