#!/usr/bin/python2.7

import subprocess
import os
import sys
import time
import telnetlib
#  *****  Login to Remote machine and register UAC with the Testing device & run UAS in the remote machine  ******


test_call_id  = 1
var = 1

a1 = subprocess.Popen('cp /root/testing/automation/config/result.txt .', shell=True)
outputa1, err = a1.communicate()

lineconfig = 0
configfile = "/root/testing/automation/config/config.txt"
values = []
with open(configfile) as cf:
        for lineconfig, line in enumerate(cf):
                if lineconfig > 0:
                        values.append([val for val in line.strip().split()])
                        for pairs in values:
                                        device_ip,local_machine_ip = pairs[0],pairs[1]

# ***** Setting Device IP address***********

os.environ['ip1'] = device_ip
os.environ['ip2'] = local_machine_ip

while var == 1:
#    ******************* ping device IP to check whether device is up or not **********************

	hostname = '$ip1'
	response = os.system("ping -c 1 " + hostname)
	hostname = device_ip
	hostname2 = local_machine_ip

	if response == 0:
        	print hostname, 'is up!'

#       ***************       Registering user static extension 3001 and password 3001 using SIPP ***********
		com = "asterisk -rx'core show version'"
		root_login = 'su'
		tn= telnetlib.Telnet(device_ip)
		tn.read_until('login: ')
		tn.write('admin\r\n')
		tn.read_until('Password: ')
		tn.write('**x*rrrr\r\n')
		tn.read_until('$')
		time.sleep(2)
		tn.write(root_login+'\r\n' )
		tn.read_until('Password: ')
		tn.write('rrrrrr\r\n')
		tn.read_until('$')
		tn.write(com+'\r\n' )
		tn.read_until('\n')
		invalid = tn.read_until('Unable', 1)
		if invalid == "Unable":
			print "asterisk is not running"
			exit()
		else:
			tn.write(com+'\r\n' )
			tn.read_until('\n')
			asterisk = tn.read_until('Asterisk', 1)
		tn.read_until('$', 1)
		tn.write('exit\n')
		tn.read_until('$')
		tn.write('exit\n')

		if asterisk == "Asterisk":
			reg = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3001.xml $ip1 -s 3001 -ap 3001 -i $ip2 -r 1 -m 1'
	
			b = subprocess.Popen(reg, shell=True)
			output, err = b.communicate()

#       ***************  Run UAS with rtp_echo using SIPP   *****************

			uasrun = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uas_ulaw.xml -i $ip2 -m 1 -rtp_echo'
			c = subprocess.Popen(uasrun, shell=True)
#			output, err = c.communicate()

# ****** delay added for RTP FLOW after registering the user *******

			time.sleep(3)

#  *****  UAC call scenario execution using sipp *****

			call = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_hold.xml $ip1 -i $ip2 -r 1 -m 1 -s 3003 -ap 3003 -mp 6009'
			p = subprocess.Popen(call, shell=True)
			output4, err = p.communicate()
	
			time.sleep(6)
	

# ***** Converting captured pcap file to wav format *************

			q = subprocess.Popen('/root/testing/automation/scripts/pcaptowav.sh /root/testing/automation/destination_pcap/destination.pcap', shell=True)
			output1, err = q.communicate()

#  ********  Comparing captured wav file with the Original file using PESQ tool to evaluate voice quality  ***********


			r = subprocess.Popen('/root/testing/PESQ/P862_annex_A_2005_CD/source/PESQ +16000 /root/testing/automation/sounds/sourceulaw.wav /root/testing/automation/sounds/capture3D.wav', shell=True)
			output2, err = r.communicate()

# *************  Writing Result into result.txt file using PESQ MOS score **************************

			i = 0
			filename = "pesq_results.txt"
			mynumbers = []
			with open(filename) as f:
        			for i, line in enumerate(f):
                			if i > 0:
                        			mynumbers.append([n for n in line.strip().split()])
	                        		for pair in mynumbers:
        	                                	x,y,pesq_score = pair[0],pair[1],pair[2]
	                	      		print pesq_score
		                	        pesq_mos_value = float(pesq_score)
        		                	result_data = open('result.txt', 'a')
	                		        min_pesq = 3.5
        	                		if ( pesq_mos_value >= min_pesq ) :
	                	                	result_data.write('        %s           PASS          %s\n' % (test_call_id, pesq_score))
	        	                	else:
  		                      	               	result_data.write('        %s           FAIL          %s\n' % (test_call_id, pesq_score))


			g = subprocess.Popen('rm pesq_results.txt payloads sound.raw', shell=True)
			output10, err = g.communicate()
			test_call_id = test_call_id + 1
	        else:
			print "asterisk is crashed or not running"
			exit()
	else:
        	print "\n !!!!!!!!!!!!!!Testing Device down %s   !!!!!!!!!" % hostname
	       	exit()

	
