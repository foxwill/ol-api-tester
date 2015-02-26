"""Module to hold global settings used throughout OneLogin API"""

__author__ = "W. P. Fox - patric.fox[at]onelogin[dot]com"

global defaults
global default_filename

import os

if os.name == 'nt':
	default_filename = "config.ini"
else:
	default_filename = ".ocrc"

defaults = {'hostname':'api.onelogin.com','max_retries':'3'}