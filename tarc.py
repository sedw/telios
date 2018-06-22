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

accounts = os.environ['TARC_PASSWORD'].split(":")
username = accounts[0].rstrip()
password = accounts[1].rstrip()

TCPPORT = 23
TIMEOUT = 5


################################################################################
# Cisco IOS commands
################################################################################

USER_PROMPT = b'Username:'
PASSWORD_PROMPT = b'Password:'
EXEC_PROMPT = b"#"
NOPAGER = b'terminal length 0'

commands = sys.stdin

EXIT = b'exit'


################################################################################
# Telnet and run commands
################################################################################

# Start Telnet
tn = telnetlib.Telnet(hostname, TCPPORT, TIMEOUT)

# Login
tn.read_until(USER_PROMPT)
tn.write(username.encode('ascii') + b'\n')
tn.read_until(PASSWORD_PROMPT)
tn.write(password.encode('ascii') + b'\n')
tn.read_until(EXEC_PROMPT)

# Do no display '-- more --'
tn.write(NOPAGER + b'\n')
tn.read_until(EXEC_PROMPT)

# If this is deleted, "#" is not displayed at the beginning of the immediately
# following command. Is there any other good way?
tn.write(b'\n')

# Run commands
for command in commands:
    tn.write(command.encode('ascii') + b'\n')
tn.write(EXIT + b'\n')

# Display result
print(tn.read_all().decode('ascii'))

