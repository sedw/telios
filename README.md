# telios

Cisco IOS 機器に telnet 接続し、標準入力された文字列を流し込むスクリプトです

## 1. telnet サーバの設定

例) Cisco IOS の場合

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

## 2. ユーザ名とパスワードを環境変数にセット

例) ユーザ名:sanfran パスワード:cisco

```
export TARC_USER=sanfran
export TARC_PASSWORD=cisco
```

## 3. telnet サーバに接続し、コマンドを実行する

telnet サーバ上で show ver を実行

```
echo show ver | ./telios.py 192.168.33.100
```

telnet サーバ上で 3 つのコマンドを連続で実行する

```
cat <<EOF | ./telios.py 192.168.33.100
show ver
show int status
show run
EOF
```

