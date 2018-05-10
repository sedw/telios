#!/usr/bin/env python
# coding=utf-8

# Telnet and run commands 

import sys
import os
import telnetlib


################################################################################
# Telnet client setting
################################################################################

hostname = sys.argv[1]

passwordfile = os.path.expanduser(sys.argv[2])
with open(passwordfile) as file:
    account = file.readline()
    accounts = account.rsplit(":")
username = accounts[0].rstrip()
password = accounts[1].rstrip()

TCPPORT = 23
TIMEOUT = 5


################################################################################
# Cisco IOS commands
################################################################################

USER_PROMPT = 'Username:'
PASSWORD_PROMPT = 'Password:'
EXEC_PROMPT = '#'
NOPAGER = 'terminal length 0'

commands = sys.stdin

EXIT = 'exit'


################################################################################
# Telnet and run commands
################################################################################

# Start Telnet
tn = telnetlib.Telnet(hostname, TCPPORT, TIMEOUT)

# Login
tn.read_until(USER_PROMPT)
tn.write(username + '\n')
tn.read_until(PASSWORD_PROMPT)
tn.write(password + '\n')
tn.read_until(EXEC_PROMPT)

# Do no display '-- more --'
tn.write(NOPAGER + '\n')
tn.read_until(EXEC_PROMPT)

# If this is deleted, "#" is not displayed at the beginning of the immediately
# following command. Is there any other good way?
tn.write('\n')

# Run commands
for command in commands:
    tn.write(command + '\n')
tn.write(EXIT + '\n')

# Display result
print tn.read_all()

