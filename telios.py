#!/usr/bin/env python
# coding=utf-8

import sys
import os
import telnetlib


################################################################################
# telnet クライアントの設定
################################################################################

TCPPORT = 23
TIMEOUT = 5

host = sys.argv[1]
user = os.environ['TELIOS_USERNAME']
password = os.environ['TELIOS_PASSWORD']


################################################################################
# Cisco IOS 用の設定
################################################################################

USER_PROMPT = b"Username:"
PASSWORD_PROMPT = b"Password:"
EXEC_PROMPT = b"#"
NOPAGER = b"terminal length 0"
EXIT = b"exit"

commands = sys.stdin


################################################################################
# telnet 接続とコマンド入力
################################################################################

# telnet 開始
tn = telnetlib.Telnet(host, TCPPORT, TIMEOUT)

# ログイン処理
tn.read_until(USER_PROMPT)
tn.write(user.encode('ascii') + b"\n")
tn.read_until(PASSWORD_PROMPT)
tn.write(password.encode('ascii') + b"\n")
tn.read_until(EXEC_PROMPT)

# '-- more --' を削除
tn.write(NOPAGER + b"\n")
tn.read_until(EXEC_PROMPT)

# 行頭に待ちプロンプトを表示させるための改行
tn.write(b"\n")

# コマンド入力
for command in commands:
    tn.write(command.encode('ascii') + b"\n")
tn.write(EXIT + b"\n")

# 結果表示
print(tn.read_all().decode('ascii'))

