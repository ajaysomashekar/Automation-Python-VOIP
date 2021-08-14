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
		tn.write('rrrrrrrr\r\n')
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
			reg1 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3001.xml $ip1 -s 3001 -ap 3001 -i $ip2 -r 1 -m 1'
			b1 = subprocess.Popen(reg1, shell=True)
			output11, err = b1.communicate()

			reg2 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3002.xml $ip1 -s 3002 -ap 3002 -i $ip2 -r 1 -m 1'
			b2 = subprocess.Popen(reg2, shell=True)
			output12, err = b2.communicate()

			reg3 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3003.xml $ip1 -s 3003 -ap 3003 -i $ip2 -r 1 -m 1'
			b3 = subprocess.Popen(reg3, shell=True)
			output13, err = b3.communicate()

			reg4 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3004.xml $ip1 -s 3004 -ap 3004 -i $ip2 -r 1 -m 1'
			b4 = subprocess.Popen(reg4, shell=True)
			output14, err = b4.communicate()

			reg5 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3005.xml $ip1 -s 3005 -ap 3005 -i $ip2 -r 1 -m 1'
			b5 = subprocess.Popen(reg5, shell=True)
			output15, err = b5.communicate()

			reg6 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3006.xml $ip1 -s 3006 -ap 3006 -i $ip2 -r 1 -m 1'
			b6 = subprocess.Popen(reg6, shell=True)
			output16, err = b6.communicate()

			reg7 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3007.xml $ip1 -s 3007 -ap 3007 -i $ip2 -r 1 -m 1'
			b7 = subprocess.Popen(reg7, shell=True)
			output17, err = b7.communicate()

			reg8 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3008.xml $ip1 -s 3008 -ap 3008 -i $ip2 -r 1 -m 1'
			b8 = subprocess.Popen(reg8, shell=True)
			output18, err = b8.communicate()

			reg9 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3009.xml $ip1 -s 3009 -ap 3009 -i $ip2 -r 1 -m 1'
			b9 = subprocess.Popen(reg9, shell=True)
			output19, err = b9.communicate()

			reg10 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3010.xml $ip1 -s 3010 -ap 3010 -i $ip2 -r 1 -m 1'
			b10 = subprocess.Popen(reg10, shell=True)
			output20, err = b10.communicate()

			reg11 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3011.xml $ip1 -s 3011 -ap 3011 -i $ip2 -r 1 -m 1'
			b11 = subprocess.Popen(reg11, shell=True)
			output21, err = b11.communicate()

			reg12 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3012.xml $ip1 -s 3012 -ap 3012 -i $ip2 -r 1 -m 1'
			b12 = subprocess.Popen(reg12, shell=True)
			output22, err = b12.communicate()

#       ***************  Run UAS with rtp_echo using SIPP   *****************

			uasrun = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uas_ulaw.xml -i $ip2 -m 10 -rtp_echo'
			c = subprocess.Popen(uasrun, shell=True)
#			output, err = c.communicate()

# ****** delay added for RTP FLOW after registering the user *******

			time.sleep(3)

#  *****  UAC call scenario execution using sipp *****

			call1 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_ulaw_3017_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3017 -ap 3017 -mp 6100'
			p1 = subprocess.Popen(call1, shell=True)

			call2 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_ulaw_3018_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3018 -ap 3018 -mp 6101'
			p2 = subprocess.Popen(call2, shell=True)

			call3 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_ulaw_3019_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3019 -ap 3019 -mp 6152'
			p3 = subprocess.Popen(call3, shell=True)

			call4 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_ulaw_3020_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3020 -ap 3020 -mp 6153'
			p4 = subprocess.Popen(call4, shell=True)

			call5 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_ulaw_3021_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3021 -ap 3021 -mp 6251'
			p5 = subprocess.Popen(call5, shell=True)

			call6 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_ulaw_3022_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3022 -ap 3022 -mp 6355'
			p6 = subprocess.Popen(call6, shell=True)

			call7 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_ulaw_3023_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3023 -ap 3023 -mp 6455'
			p7 = subprocess.Popen(call7, shell=True)

			call8 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_ulaw_3024_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3024 -ap 3024 -mp 6555'
			p8 = subprocess.Popen(call8, shell=True)

			call9 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_ulaw_3025_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3025 -ap 3025 -mp 6655'
			p9 = subprocess.Popen(call9, shell=True)

			call10 = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_ulaw_3026_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3026 -ap 3026 -mp 6755'
			p10 = subprocess.Popen(call10, shell=True)

			output20, err = p1.communicate()
	
			time.sleep(8)
	

# ***** Converting captured pcap file to wav format *************

#			q1 = subprocess.Popen('/root/testing/automation/scripts/ptw6009/pcaptowav6009.sh /root/testing/automation/destination_pcap/destination3001.pcap', shell=True)
#			output1, err = q1.communicate()
#			time.sleep(2)
#			q2 = subprocess.Popen('/root/testing/automation/scripts/ptw6010/pcaptowav6010.sh /root/testing/automation/destination_pcap/destination3002.pcap', shell=True)
#			output1, err = q2.communicate()

#  ********  Comparing captured wav file with the Original file using PESQ tool to evaluate voice quality  ***********


#			r1 = subprocess.Popen('/root/testing/PESQ/P862_annex_A_2005_CD/source/PESQ +16000 /root/testing/automation/sounds/sourceulaw.wav /root/testing/automation/sounds/capture3D3001.wav', shell=True)
#			output2, err = r1.communicate()
			time.sleep(2)
#			r2 = subprocess.Popen('/root/testing/PESQ/P862_annex_A_2005_CD/source/PESQ +16000 /root/testing/automation/sounds/sourceulaw3002.wav /root/testing/automation/sounds/capture3D3002.wav', shell=True)
#			output2, err = r2.communicate()

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
#               	                		print "%f second line" % l
	                	                	result_data.write('        %s           PASS          %s\n' % (test_call_id, pesq_score))
	        	                	else:
  		                      	               	result_data.write('        %s           FAIL          %s\n' % (test_call_id, pesq_score))


			g = subprocess.Popen('rm pesq_results.txt sound.raw payloads', shell=True)
			output10, err = g.communicate()
			test_call_id = test_call_id + 1
	        else:
			print "asterisk is crashed or not running"
			exit()
	else:
        	print "\n !!!!!!!!!!!!!!Testing Device down %s   !!!!!!!!!" % hostname
	       	exit()

	
