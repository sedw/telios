# telios

Cisco IOS 機器に telnet 接続し、標準入力された文字列を流し込むスクリプトです

## 1. Cisco IOS 機器の設定

例)
- ユーザ名: sanfran
- パスワード: cisco
- IP アドレス: 192.168.33.100/24
- telnet ログイン可

```
conf t
username sanfran privilege 15 password cisco
line vty 0 15
 login local
 transport input telnet
int Gi 1
 ip address 192.168.33.100 255.255.255.0
 no shut
 end
```

## 2. 本スクリプト実行環境の環境変数に telnet ユーザ名とパスワードを設定

```
export TARC_USERNAME=sanfran
export TARC_PASSWORD=cisco
```

## 3. Cisco IOS 機器に telnet し、コマンドを実行する

show ver を実行する

```
echo show ver | ./telios.py 192.168.33.100
```

3 つのコマンドを連続で実行する

```
cat <<EOF | ./telios.py 192.168.33.100
show ver
show int status
show run
EOF
```

