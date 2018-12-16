#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys

dapnet_user = "nocall"
dapnet_pass = "nopass"
pos = 0

if (len(sys.argv)<3):
	print ("dapnet_rubric_send.py - version 1.0 - by Johan Denoyer (f4wat@f4wat.xyz)")
	print ("Usage : ")
	print (sys.argv[0]+" destination_rubric \"message\"")
	exit(0)

destination = str(sys.argv[1])
message = str(sys.argv[2])
headers = {
    'Content-Type': 'application/json',
}

data = '{ "rubricName": "'+destination+'", "text": "'+message+'", "number": '+str(pos)+'}'

response = requests.post('http://www.hampager.de:8080/news', headers=headers, data=data, auth=(dapnet_user, dapnet_pass))
exit(0)
