#!/usr/bin/env python3
import requests
import json
import subprocess
import time
import pdb; pdb.set_trace()

r = requests.get(url='https://public-dns.info/nameserver/mx.json')
data = json.loads(r.content)

def query_dns(IP,NAME,CITY):
	print('###########################################################')
	print('Query to DNS %s with name %s from  %s' % (IP,NAME,CITY))
	p = subprocess.Popen("dig @%s um.edu.mx A" % IP ,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	#p = subprocess.Popen("dig @%s um.edu.mx A | sed -n '/QUESTION SECTION/,/Query time/p' | grep -v 'QUESTION SECTION' | grep -v 'Query time'" % IP, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True)
	(output, err) = p.communicate()
	p_status = p.wait()
	print("Command output : ")
	print(output.decode('utf-8').strip())
	#print(output.strip())

def load_dns_isp():
	for x in data:
	    IP=x['ip']
	    NAME=x['name']
	    CITY=x['city']
	    time.sleep(5)
	    query_dns(IP,NAME,CITY)

load_dns_isp()
