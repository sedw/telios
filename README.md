# tarc
Telnet and run commands

## 1. Download a router image from cisco.com
- Cloud Services Router 1000V (csr1000v-universalk9.03.11.00.S.154-1.S-std-2.iso)

## 2. Start the router on VirtualBox

## 3. Allow telnet connection to router

e.g.
```
conf t
username sanfran privilege 15 password cisco
line vty 0 15
 login local
 tranport input telnet
int Gi 1
 ip address 192.168.33.100
 no shut
 end
```

## 4. Create a password file

e.g.
```
echo sanfran:cisco > password 
```

## 5. Telnet and run commands

e.g.
```
echo show ver | ./tarc.py 192.168.33.100 password
```

e.g.
```
cat << EOS | ./tarc.py 192.168.33.100 password
show ver
show int status
show run
EOS
```

