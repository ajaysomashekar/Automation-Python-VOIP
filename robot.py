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
output1, err = a1.communicate()

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

#    ******************* ping device IP to check whether device is up or not **********************

hostname = '$ip1'
response = os.system("ping -c 4 " + hostname)
hostname = device_ip
hostname2 = local_machine_ip

if response == 0:
       	print hostname, 'is up!'
	time.sleep(10)

#       ***************       Registering user static extension 3002 and password 3002 using SIPP ***********

	reg = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uac_3002.xml $ip1 -s 3002 -ap 3002 -i $ip2 -r 1 -m 1'
	
	b = subprocess.Popen(reg, shell=True)
	output2, err = b.communicate()

#       ***************  Run UAS with rtp_echo using SIPP   *****************

	uasrun = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/uas_ulaw.xml -i $ip2 -m 1 -rtp_echo'
	c = subprocess.Popen(uasrun, shell=True)


#  *****  UAC call scenario execution using sipp *****

	call = '/root/testing/sipp-3.4-beta2/sipp -sf /root/testing/automation/xmlscenarios/robot_call.xml $ip1 -i $ip2 -r 1 -m 1 -s 3001 -ap 3001 -mp 6009 '
	p = subprocess.Popen(call, shell=True)
	output3, err = p.communicate()

	
# ***** Converting captured pcap file to wav format *************
        time.sleep(4)
        
 	q = subprocess.Popen('/root/testing/automation/scripts/pcaptowav6008.sh /root/testing/automation/destination_pcap/destination.pcap', shell=True)
        output4, err = q.communicate()


#  ********  Comparing captured wav file with the Original file using PESQ tool to evaluate voice quality  ***********


        r = subprocess.Popen('/root/testing/PESQ/P862_annex_A_2005_CD/source/PESQ +8000 /root/testing/automation/sounds/sourcealaw.wav /root/testing/automation/sounds/capture3D.wav', shell=True)
        output5, err = r.communicate()

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
                                          min_pesq = 2.0
                                          if ( pesq_mos_value >= min_pesq ) :
#                                                 print "%f second line" % l
                                                  result_data.write('        %s           PASS          %s\n' % (test_call_id, pesq_score))
                                          else:
                                                  result_data.write('        %s           FAIL          %s\n' % (test_call_id, pesq_score))
        g = subprocess.Popen('rm pesq_results.txt payloads sound.raw', shell=True)
        output6, err = g.communicate()
        test_call_id = test_call_id + 1


#       ***************  wait till execution completes (UAS with rtp_echo using SIPP)   *****************
        output11, err = c.communicate()
