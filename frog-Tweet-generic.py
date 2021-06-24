#!/usr/bin/python

import os
import sys
import argparse
from twython import Twython
import subprocess


#Twitter App Tokens and Keys
CONSUMER_KEY = 'YourTwitterConsumerKey'
CONSUMER_SECRET = 'YourTwitterConsumerSecret'
ACCESS_KEY = 'YourTwitterAccessKey'
ACCESS_SECRET = 'YourTwitterAccessSecret'

# API connection string
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# Photo path
photo = open('/home/pi/frogPics/webcam.jpg','rb')

# Get tank temperature from subprocess Popen and store to temp
t = subprocess.Popen(["/home/pi/tempy.py"], stdout=subprocess.PIPE)
temp, err = t.communicate()
#print temp

# Argparse conditions
parser = argparse.ArgumentParser(description='AquaPiTweet')
parser.add_argument('--sleep',action='store_true',default=False)
parser.add_argument('--awake',action='store_true',default=False)
args = parser.parse_args()

if args.sleep:
        api.update_status_with_media(status='We are sleepy now! Visit us tomorrow on cam @ http://yourwebsite.com Current ' + temp, media=photo)
elif args.awake:
        api.update_status_with_media(status='We are awake! Come visit us on cam at http://yourwebsite.com Current ' + temp, media=photo)
else:
        print "argument not provided, exiting without status update "
