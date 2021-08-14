#!/bin/bash

sshpass -p root123 ssh -o StrictHostKeyChecking=no root@192.168.0.201 "killall -9 sipp"
