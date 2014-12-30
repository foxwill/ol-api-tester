"""Different calls available to the OneLogin API"""

import requests
import functions


baseURL = 'https://app.onelogin.com'
password = 'x'


def userAPI(api_key):
	v2path = '/api/v2/users'
	v1path = '/api/v1/users'
	print "Select an Option: "
	print "1. Show User (Single User)"
	print "2. List Users (All)"
	print "3. Create User - Not Active"
	print "4. Update User"
	print "5. Set Password -- Not Active"
	print "6. Delete User"
	print "7. Return to Menu"
	userChoice = int(raw_input('Selection: '))

	if userChoice == 1:
		userID = raw_input("Please provide UserID: ")
		target = baseURL + v2path + '/' + userID + '.xml'
		r = requests.get(target, auth=(api_key, password))
		print r.text
		userAPI(api_key)
	elif userChoice == 2:
		target = baseURL + v2path + '.xml'
		r = requests.get(target, auth=(api_key, password))
		print r.text
		userAPI(api_key)
	elif userChoice == 3:
		target = baseURL + v1path + '.xml'
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
	elif userChoice == 4:
		target = baseURL + v1path + '.xml'
		userID = raw_input('Enter a userID to update:')
		print 'Choose a field to update (limit 1)'
		print '1. FirstName'
		print '2. LastName'
		print '3. UserName'
		print '4. Phone'
		print '5. Email'
		print '6. Return to Menu'

		updateChoice = raw_input('Enter a selection: ')
		if updateChoice == '1':
			firstName = raw_input('Enter a value for FirstName')
			if firstName:
				payload = '<user><firstname>' + firstName + '</firstname></user>'
				r = requests.put(target, data=payload, auth=(api_key, password))
				print r.status_code
		elif updateChoice == 2:
			lastName = raw_input('Enter a value for LastName')
		elif updateChoice == 3:
			userName = raw_input('Enter a value for UserName')
		elif updateChoice == 4:
			phone = raw_input('Enter a value for Phone')
		elif updateChoice == 5:
			email = raw_input('Enter a value for email')
		elif updateChoice == 7:
			userAPI(api_key)



	elif userChoice == 6:
		userID = raw_input("Please provide UserID: ")
		target = baseURL + v1path + '/' + userID + '.xml'
		r = requests.delete(target, auth=(api_key, password))
		if r.status_code == 200:
			print '-=-=-=-=User Deleted=-=-=-=-'
		userAPI(api_key)
	elif userChoice == 7:
		return functions.printMenu(api_key)



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
