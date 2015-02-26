"""Different calls available to the OneLogin API"""

import requests
import methods


baseURL = 'https://app.onelogin.com'
password = 'x'

def testConnection(api_key):
	r = requests.get(baseURL + '/api/v2/users.xml', auth=(api_key, password))
	if r.status_code == 200:
		print 'SUCCESS!  API Token is good!\n'
	else:
		print 'ERROR! Connection Failed with status '+ str(r.status_code)
		exit()


def printMenu(api_key):
	"""Print the main menu"""
	print "*************************************"
	print "*************************************"
	print "Choose from the following:"
	print "1. Accounts - Reseller Account Only!!"
	print "2. Users"
	print "3. Roles"
	print "4. Groups"
	print "5. Events"
	print "6. Launch"
	print "7. Delegate Authentication"
	print "8. Secure Invite Link"
	print "9. Exit"
	choice = 0
	while (choice == 0 and choice <= 9):
		choice = raw_input("Choice: ")
		if not choice in '123456789':
			print "Invalid Selection"
			printMenu(api_key)	
		else:
			if int(choice) == 1:
				#print "Account API"
				methods.accountAPI(api_key)
			elif int(choice) == 2:
				methods.userAPI(api_key)
			elif int(choice) == 3:
				#print "Roles API"
				methods.rolesAPI(api_key)
			elif int(choice) == 4:
				#print "Groups API"
				methods.groupsAPI(api_key)
			elif int(choice) == 5:
				#print "Events API"
				methods.eventsAPI(api_key)
			elif int(choice) == 6:
				#print "Launch API"
				methods.launchAPI(api_key)
			elif int(choice) == 7:
				#print "Delegate Authentication API"
				methods.delegateAPI(api_key)
			elif int(choice) == 8:
				#print "Secure Invite Link API"
				methods.linkAPI(api_key)
			elif int(choice) == 9:
				exit()
	else:
		print "Invalid Selection"
		printMenu(api_key)

def buildCurl(api_key,baseURL,path,userID='null',payload='null'):
	"""
	write curl output for easier testing 
	"""
	if userID == 'null' and payload == 'null':
		print "curl -u " + api_key + ":x " + '"' + baseURL + path + '.xml1"'
	elif userID != 'null':
		if payload != 'null':
			print "curl -u " + api_key + ":x " + '"' + baseURL + path + '/' + userID + '.xml2"'
			print payload
		else:
			print "curl -u " + api_key + ":x " + ' "' + baseURL + path + '/' + userID + '.xml' \
	+ '" -X DELETE'
	else:
		print "curl -u " + api_key + ":x " + ' "' + baseURL + path + '/' + userID + '.xml' \
	+ '" -d "' + payload + '" -X PUT -h "content-type: text/xml"'
	