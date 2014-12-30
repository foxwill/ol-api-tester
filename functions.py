"""Different calls available to the OneLogin API"""

import requests
import methods


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
		methods.accountAPI(api_key)
	elif choice == 2:
		methods.userAPI(api_key)
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