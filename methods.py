"""Different calls available to the OneLogin API"""

import requests
import functions


baseURL = 'https://app.onelogin.com'
password = 'x'



def accountAPI(api_key):
	""" Accounts API - not implemented"""
	print "Returning to Menu\n"
	functions.printMenu(api_key)


def userAPI(api_key):
	"""User API for actions involving user Accounts
	Creating user's will be added in a future version"""
	#setup the session info for talking to the API
	s = requests.Session()
	s.auth = (api_key, 'x')
	s.headers['Content-Type'] = 'text/xml'
	#several paths available for userAPI
	v3path = '/api/v3/users'
	v2path = '/api/v2/users'
	v1path = '/api/v1/users'
	#print the options available
	print "*************User API options "
	print "1. Show User (Single User)"
	print "2. List Users (All)"
	#print "3. Create User - Not Active"
	print "4. Update User"
	#print "5. Set Password -- Not Active"
	print "6. Delete User"
	print "7. Return to Menu"
	#check if user entry is valid
	userChoice = 0
	while userChoice == 0 and userChoice <= 7:
		userChoice = raw_input('Selection: \n')
		if not userChoice in '1234567':
			print "Invalid Selection"
			eventsAPI(api_key)	
		else:
			if int(userChoice) == 1:
				#option 1 does a basic user lookup
				userID = raw_input("Please provide UserID:  \n")
				target = baseURL + v2path + '/' + userID + '.xml'
				r = requests.get(target, auth=(api_key, password))
				print r.text
				functions.buildCurl(api_key,baseURL,v2path,userID)
				userAPI(api_key)
			elif int(userChoice) == 2:
				#option 2 provides a list of all users
				target = baseURL + v2path + '.xml'
				r = requests.get(target, auth=(api_key, password))
				print r.text
				functions.buildCurl(api_key,baseURL,v2path)
				userAPI(api_key)
			elif int(userChoice) == 3:
				#not implimented completely
				"""target = baseURL + v1path + '.xml'
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
				payload = "<user><email>+ email + '</email><firstname>' +\
				 fName + '</firstname><lastname>' + lName + '</lastname><username>' + userName + '</username>' + '<phone>' + phone + \
				 '</phone>' + '</user>'
				r = requests.post(target, auth=(api_key, password), data=payload)
				print r.text"""
				userAPI(api_key)
			elif int(userChoice) == 4:
				#option 4 lets you update attributes on a user
				userID = raw_input('Enter a userID to update:')
				print 'Choose a field to update (limit 1)\n'
				print '1. FirstName'
				print '2. LastName'
				print '3. UserName'
				print '4. Phone'
				print '5. Email'
				print '6. Custom Attribute'
				print '7. Return to Menu'
				updateChoice = 0
				while updateChoice == 0 and updateChoice <= 7:
					updateChoice = raw_input('Enter a selection:  \n')
					if not userChoice in '1234567':
						print "Invalid Selection"
						userAPI(api_key)	
					else:
						if int(updateChoice) == 1:
							firstName = raw_input('Enter a value for FirstName: ')
							payload = """<user><firstname>""" + firstName + """</firstname></user>"""
							r = s.put(baseURL + v3path + '/' + userID + '.xml', data=payload, auth=(api_key, password))
							functions.buildCurl(api_key,payload,baseURL,v3path,userID)
							userAPI(api_key)
						elif int(updateChoice) == 2:
							lastName = raw_input('Enter a value for LastName: ')
							payload = """<user><lastname>""" + lastName + """</lastname></user>"""
							r = s.put(baseURL + v3path + '/' + userID + '.xml', data=payload, auth=(api_key, password))
							functions.buildCurl(api_key,payload,baseURL,v3path,userID)
							userAPI(api_key)
						elif int(updateChoice) == 3:
							userName = raw_input('Enter a value for UserName: ')
							payload = """<user><username>""" + userName + """</username></user>"""
							r = s.put(baseURL + v3path + '/' + userID + '.xml', data=payload, auth=(api_key, password))
							functions.buildCurl(api_key,payload,baseURL,v3path,userID)
							userAPI(api_key)
						elif int(updateChoice) == 4:
							phone = raw_input('Enter a value for Phone: ')
							payload = """<user><phone>""" + phone + """</phone></user>"""
							r = s.put(baseURL + v3path + '/' + userID + '.xml', data=payload, auth=(api_key, password))
							functions.buildCurl(api_key,payload,baseURL,v3path,userID)
							userAPI(api_key)
						elif int(updateChoice) == 5:
							email = raw_input('Enter a value for email: ')
							payload = """<user><email>""" + email + """</email></user>"""
							r = s.put(baseURL + v3path + '/' + userID + '.xml', data=payload, auth=(api_key, password))
							functions.buildCurl(api_key,payload,baseURL,v3path,userID)
							userAPI(api_key)
						elif int(updateChoice) == 6:
							attrName = raw_input('Enter the custom attribute shortname: ')
							attrValue = raw_input('Enter the value to write to this attribute: ')
							payload = """<user><custom_attribute_""" + attrName + """>""" + attrValue + \
							"""</custom_attribute_""" + attrName + """></user>"""
							r = s.put(baseURL + v3path + '/' + userID + '.xml', data=payload, auth=(api_key, password))
							functions.buildCurl(api_key,payload,baseURL,v3path,userID)
							userAPI(api_key)
						elif int(updateChoice) == 7:
							userAPI(api_key)
				else:
					print "Invalid Selection"
					groupsAPI(api_key)

			elif int(userChoice) == 6:
				#option 6 deletes the user from the subscription
				userID = raw_input("Please provide UserID: ")
				target = baseURL + v1path + '/' + userID + '.xml'
				r = s.delete(target, auth=(api_key, password))
				if r.status_code == 200:
					print '-=-=-=-=User Deleted=-=-=-=- \n'
					functions.buildCurl(api_key,baseURL,v1path,userID)
				userAPI(api_key)
			elif int(userChoice) == 7:
				print "Returning to Menu\n"
				return functions.printMenu(api_key)
	else:
		print "Invalid Selection"
		userAPI(api_key)


def rolesAPI(api_key):
	s = requests.Session()
	s.auth = (api_key, 'x')
	s.headers['Content-Type'] = 'text/xml'
	path = '/api/v1/roles'
	print '*************Roles API Options'
	print '1. Show Role'
	print '2. List Roles'
	print '3. Return to Menu'
	userChoice = 0
	while userChoice == 0 and userChoice <= 3:
		userChoice = raw_input('Make a selection:  \n')
		if not userChoice in '123':
			print "Invalid Selection"
			eventsAPI(api_key)	
		else:
			if int(userChoice) == 1:
				userID = raw_input("Please provide UserID:  \n")
				target = baseURL + path + '/' + userID + '.xml'
				r = s.get(target, auth=(api_key, password))
				print r.text
				rolesAPI(api_key)
			elif int(userChoice) == 2:
				target = baseURL + path + '.xml'
				r = s.get(target, auth=(api_key, password))
				print r.text
				rolesAPI(api_key)
			elif int(userChoice) == 3:
				print "Returning to Menu\n"
				functions.printMenu(api_key)
	else:
		print "Invalid Selection"
		rolesAPI(api_key)



def groupsAPI(api_key):
	s = requests.Session()
	s.auth = (api_key, 'x')
	s.headers['Content-Type'] = 'text/xml'
	path = '/api/v1/groups'
	print '*************Groups API options'
	print """1. Show User's Group"""
	print '2. List All Groups'
	print '3. Return to Menu'
	userChoice = 0
	while userChoice == 0 and userChoice <= 3:
		userChoice = raw_input('Make a selection:  \n')
		if not userChoice in '123':
			print "Invalid Selection"
			eventsAPI(api_key)	
		else:
			if int(userChoice) == 1:
				groupID = raw_input("Please provide a GroupID:  \n")
				target = baseURL + path + '/' + groupID + '.xml'
				r = s.get(target, auth=(api_key, password))
				print r.text
				groupsAPI(api_key)
			elif int(userChoice) == 2:
				target = baseURL + path + '.xml'
				r = s.get(target, auth=(api_key, password))
				print r.text
				groupsAPI(api_key)
			elif int(userChoice) == 3:
				print "Returning to Menu\n"
				functions.printMenu(api_key)
	else:
		print "Invalid Selection"
		groupsAPI(api_key)


def eventsAPI(api_key):
	s = requests.Session()
	s.auth = (api_key, 'x')
	s.headers['Content-Type'] = 'text/xml'
	path = '/api/v1/events'
	print '*************Events API options'
	print '1. Show Event'
	print '2. List Events'
	#print '3. Create Event'
	print '4. Return to Menu'
	userChoice = 0
	while userChoice == 0 and userChoice <= 4:
		userChoice = raw_input('Make a selection:  \n')
		if not userChoice in '1234':
			print "Invalid Selection"
			eventsAPI(api_key)	
		else:
			if int(userChoice) == 1:
				eventID = raw_input("Please provide an EventID:  \n")
				target = baseURL + path + '/' + eventID + '.xml'
				r = s.get(target, auth=(api_key, password))
				print r.text
				print target
				print r.status_code
				eventsAPI(api_key)
			elif int(userChoice) == 2:
				target = baseURL + path + '/'
				r = s.get(target, auth=(api_key, password))
				print r.text
				print target
				print r.status_code
				eventsAPI(api_key)
			elif int(userChoice) == 3:
				eventsAPI(api_key)
			elif int(userChoice) == 4:
				print "Returning to Menu\n"
				functions.printMenu(api_key)
	else:
		print "Invalid Selection"
		eventsAPI(api_key)

def launchAPI(api_key):
	print '*************Launch API'
	print 'The launch API allows you to add a shortcut to the user desktop'
	print 'to allow for seamless login.  '
	print 'The app-id can be located by logging in and clicking on '
	print 'Apps -> Company Apps -> (locate the app in question and click it)'
	print 'the app-id is in the URL. example: https://aps.onelogin.com/apps/389111/edit'
	print 'the app-id would be 389111'
	print 'Enter 0 for the appID to exit this menu\n'
	appID = raw_input('Enter the App-ID: ')
	if appID in 'abcedefghijklmnopqrstuvwxyz':
			print "Invalid Selection"
			launchAPI(api_key)	
	else:
		if int(appID) == 0:
			print "Returning to Menu\n"
			functions.printMenu(api_key)
		else:	
			print 'Your link for the app with ID ' + appID + ' is: \n'
			print 'https://app.onelogin.com/launch/' + appID + '\n\n'
	launchAPI(api_key)

def delegateAPI(api_key):
	print "Returning to Menu\n"
	functions.printMenu(api_key)

def linkAPI(api_key):
	print "Returning to Menu\n"
	functions.printMenu(api_key)
