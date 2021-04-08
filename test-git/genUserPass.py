import pybase64
from libDecoder import *


def main():
	while True:
		print("== Please input the information ==")
		username = input("Input Username: ")
		password = input("Input Password: ")
		confirmPassword = input("Input Confirm Password: ")
		if password != confirmPassword:
			print("\nError Password not match!\n")
		else:
			encodedWord = encodeWord_base64(username, password)
			break

	print();
	print("Done!")
	print("-----------------------------------------------")
	print("Please copy the data below to login.xlsx\n")
	print("Your key is: " + str(encodedWord, 'utf-8'))
	print("\n-----------------------------------------------")

	print("Press any key to Exit")
	input()


#-------Running Zone----------
main()