"""Different calls available to the OneLogin API"""

import requests


import re

baseURL = 'https://app.onelogin.com'
password = 'x'

def testConnection(api_key):
	r = requests.get(baseURL + '/api/v2/users.xml', auth=(api_key, password))
	if r.status_code == 200:
		print 'SUCCESS!  Credentials are good!\n'
	else:
		print 'ERROR! Connection Failed with status '+ str(r.status_code)


def printMenu(api_key):
	print "Choose from the following:"
	print "1. Accounts API"
	print "2. Users API"
	print "3. Roles API"
	print "4. Groups API"
	print "5. Events API"
	print "6. Launch API"
	print "7. Delegate Authentication API"
	print "8. Secure Invite Link API"
	print "9. Exit"

	choice = int(raw_input("Choice: "))

	if choice == 1:
		#print "Account API"
		accountAPI(api_key)
	elif choice == 2:
		userAPI(api_key)
	elif choice == 3:
		#print "Roles API"
		methods.rolesAPI(api_key)
	elif choice == 4:
		#print "Groups API"
		methods.groupsAPI(api_key)
	elif choice == 5:
		#print "Events API"
		methods.eventsAPI(api_key)
	elif choice == 6:
		#print "Launch API"
		methods.launchAPI(api_key)
	elif choice == 7:
		#print "Delegate Authentication API"
		methods.delegateAPI(api_key)
	elif choice == 8:
		#print "Secure Invite Link API"
		methods.linkAPI(api_key)
	elif choice == 9:
		exit()


def userAPI(api_key):
	path = '/api/v2/users'
	print "Select an Option: "
	print "1. Show User (Single User)"
	print "2. List Users (All)"
	print "3. Create User -- Not Active"
	print "4. Update User -- Not Active"
	print "5. Set Password -- Not Active"
	print "6. Delete User"
	print "7. Return to Menu"
	userChoice = int(raw_input('Selection: '))

	if userChoice == 1:
		userID = raw_input("Please provide UserID: ")
		target = baseURL + path + '/' + userID + '.xml'
		r = requests.get(target, auth=(api_key, password))
		print r.text
		userAPI(api_key)
	elif userChoice == 2:
		target = baseURL + path + '.xml'
		r = requests.get(target, auth=(api_key, password))
		print r.text
		userAPI(api_key)
	elif userChoice == 3:
		target = baseURL + path + '.xml'
		email_set = 0
		while email_set != 1:
			email = raw_input('Email: \n')
			if not re.match(r'[^@]+@[^@]+\.[^@]+',email):
				print "Invalid format, try again"
			else:
				email_set += 1

		fName = raw_input('First Name: \n')
		lName = raw_input('Last Name: \n')
		userName = raw_input('UserName: \n')
		phone = raw_input('Phone: \n')
		payload = '<user>\n' + '<email>' + email + '</email>' + '<firstname>' +\
		 fName + '</firstname>' + '<lastname>' + lName + '</lastname>' +\
		 '<username>' + userName + '</username>' + '<phone>' + phone + \
		 '</phone>' + '</user>'
		r = requests.post(target, auth=(api_key, password), data=payload)
		print r.text
		userAPI(api_key)
	elif userChoice == 6:
		userID = raw_input("Please provide UserID: ")
		target = baseURL + path + '/' + userID + '.xml'
		r = requests.delete(target, auth=(api_key, password))
		if r.status_code == 200:
			print '-=-=-=-=User Deleted=-=-=-=-'
		userAPI(api_key)
	elif userChoice == 7:
		return printMenu(api_key)



def accountAPI():
	"""test"""
	path = '/api/v1/accounts/'

def rolesAPI():
	"""test"""

def groupsAPI():
	"""test"""

def eventsAPI():
	"""test"""

def launchAPI():
	"""test"""

def delegateAPI():
	"""test"""

def linkAPI():
	"""test"""
