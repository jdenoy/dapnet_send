#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys

dapnet_user = "nocall"
dapnet_pass = "nopass"
dapnet_txgroup = "f-all"
dapnet_emergency = "false"

def debug():
	if ((len(sys.argv)>3) and (str(sys.argv[3]) == "debug")):
		return True
	else:
		return False


if (len(sys.argv)<3):
	print ("dapnet_bulk_send.py - version 1.0 - by Johan Denoyer (f4wat@f4wat.xyz)")
	print ("Usage : ")
	print (sys.argv[0]+" destination_call_list_file \"message\" [debug]")
	print ("debug is optionnal (that's why it's between [])")
	exit(0)

destination_list = str(sys.argv[1])
message = str(sys.argv[2])

headers = {
    'Content-Type': 'application/json',
}

with open(destination_list, 'r') as f:
	destination = f.readline().rstrip('\n')
	while destination:
		data = '{ "text": "'+dapnet_user.upper()+': '+message+'", "callSignNames": ["'+destination+'"], "transmitterGroupNames": ["'+dapnet_txgroup+'"], "emergency": '+dapnet_emergency+' }'
		response = requests.post('http://www.hampager.de:8080/calls', headers=headers, data=data, auth=(dapnet_user, dapnet_pass))
		if (debug()):
			print ("DEBUG : "+str(response.text))
		destination = f.readline().rstrip('\n')
f.close()
exit(0)
