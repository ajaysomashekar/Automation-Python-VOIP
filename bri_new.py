#!/usr/bin/python2.7

import subprocess
import os
import sys
import time
import telnetlib
#  *****  Login to Remote machine and register UAC with the Testing device & run UAS in the remote machine  ******

a1 = subprocess.Popen('cp /root/testing/automation/config/result.txt .', shell=True)
outputa1, err = a1.communicate()
var = 1
asterisk = "Asterisk"
count = 1
# ***** Setting Device IP address***********

while var == 1:

#  *****  UAC call scenario execution using sipp *****

			call = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/bri_call.xml 192.168.10.89 -i 192.168.10.66 -s 8634 -ap 8634 -r 1 -m 1'
			p = subprocess.Popen(call, shell=True)
			output4, err = p.communicate()
		count = count + 1
		result_data = open('result.txt', 'a')
		result_data.write('    %s \n' % (count))
		time.sleep(2)
