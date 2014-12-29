"""OneLogin API Tester"""

import sys
import requests
import methods

"""
API Key:
7dc7fff7dfbc29055d98aafe0b990346004c1054
"""

api_key = sys.argv[1]
password = 'x'
baseURL = 'app.onelogin.com'

##If not called with the right params, exit

if (len(sys.argv)<=1) or (len(sys.argv)>2) or ((len(sys.argv[1])) < 40 or (len(sys.argv[1]) >= 41)):
	print ('Usage: %s APIKEY' % sys.argv[0])
	print ('Example: %s 7dc7fff7dfbaaa055d98aafe0b990346004c1054' % sys.argv[0])
	if len(sys.argv[1]) < 40:
		print "API key is too short"
	else:
		print "API key is too long"
	exit(0)

	
methods.testConnection(api_key)
methods.printMenu(api_key)