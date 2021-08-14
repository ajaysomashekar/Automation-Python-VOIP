#!/bin/bash

sshpass -p root123 ssh -t -t -o StrictHostKeyChecking=no root@192.168.0.201 ./test_basic_call_uas.py &
