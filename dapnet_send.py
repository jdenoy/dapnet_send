#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys

dapnet_user = "nocall"
dapnet_pass = "nopass"
dapnet_txgroup = "all"
dapnet_emergency = "false"

if (len(sys.argv)<3):
	print ("dapnet_send.py - version 1.0 - by Johan Denoyer (f4wat@f4wat.xyz)")
	print ("Usage : ")
	print (sys.argv[0]+" destination_call \"message\"")
	exit(0)

destination = str(sys.argv[1])
message = str(sys.argv[2])
headers = {
    'Content-Type': 'application/json',
}

data = '{ "text": "'+destination+': '+message+'", "callSignNames": ["'+destination+'"], "transmitterGroupNames": ["'+dapnet_txgroup+'"], "emergency": '+dapnet_emergency+' }'

response = requests.post('http://www.hampager.de:8080/calls', headers=headers, data=data, auth=(dapnet_user, dapnet_pass))
exit(0)
