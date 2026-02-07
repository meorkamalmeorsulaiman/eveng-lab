# eveng-lab

This is the repository for my eveng lab. Lab options are available in `lab-topology` directory. It's allow listing and starting up nodes in a lab with eveng community. 

## Requirement

The code run onpython and few modules:
- request
- json
- os 
- ast

Environment variables that must be set:
- Username for accessing the API: `EVENG_USER`
- Username password for accessing the API: `EVENG_PASSWORD`
- EVE-NG Server IP Address: `EVENG_SERVER`

All the lab details is populated in the `metadata/lab-list.txt` as an python dictionary. Thus must be populate based on the environment. Below is the example:
```
{0: "0-Sandbox", 1: "1-Base-Template", 2: "2-IGP-N-SR", 3: "3-IBGP", 4: "4-L3VPN"}
```

## Running the code

Example of code to check the nodes available in a lab by running the script - `02-get-lab-nodes.py`
```
===============================================
Logging in...
===============================================
Please choose the lab nodes you want to list
===============================================
0 0-Sandbox
1 1-Base-Template
2 2-IGP-N-SR
3 3-IBGP
4 4-L3VPN
===============================================
Enter the lab number: 0
===============================================
Id: 1 - R1 - csr1000vng - telnet://192.168.101.253:32769
Id: 3 - R3 - csr1000vng - telnet://192.168.101.253:32771
Id: 4 - R4 - csr1000vng - telnet://192.168.101.253:32772
Id: 5 - R5 - csr1000vng - telnet://192.168.101.253:32773
Id: 6 - R6 - csr1000vng - telnet://192.168.101.253:32774
Id: 7 - R7 - csr1000vng - telnet://192.168.101.253:32775
Id: 9 - R9 - csr1000vng - telnet://192.168.101.253:32777
Id: 10 - R10 - csr1000vng - telnet://192.168.101.253:32778
Id: 11 - R11 - csr1000vng - telnet://192.168.101.253:32779
Id: 12 - R12 - csr1000vng - telnet://192.168.101.253:32780
Id: 13 - R13 - csr1000vng - telnet://192.168.101.253:32781
Id: 14 - R14 - csr1000vng - telnet://192.168.101.253:32782
Id: 2 - R2 - xrv - telnet://192.168.101.253:32770
Id: 8 - R8 - xrv - telnet://192.168.101.253:32776
===============================================
Logging out...
===============================================
```

Another example where starting an individual node in a lab by running the `03-start-lab.py`
```
==============
Logging in...
===========================================================================================
Do you want to start whole nodes in the lab or individual node? whole (A) or individual (B)
===========================================================================================
whole (A) or individual (B): b
===============================================
Please select which lab you want to start
===============================================
0 0-Sandbox
1 1-Base-Template
2 2-IGP-N-SR
3 3-IBGP
4 4-L3VPN
===============================================
Enter the lab number: 0
===============================================
Id: 1 - R1 - csr1000vng - telnet://192.168.101.253:32769
Id: 3 - R3 - csr1000vng - telnet://192.168.101.253:32771
Id: 4 - R4 - csr1000vng - telnet://192.168.101.253:32772
Id: 5 - R5 - csr1000vng - telnet://192.168.101.253:32773
Id: 6 - R6 - csr1000vng - telnet://192.168.101.253:32774
Id: 7 - R7 - csr1000vng - telnet://192.168.101.253:32775
Id: 9 - R9 - csr1000vng - telnet://192.168.101.253:32777
Id: 10 - R10 - csr1000vng - telnet://192.168.101.253:32778
Id: 11 - R11 - csr1000vng - telnet://192.168.101.253:32779
Id: 12 - R12 - csr1000vng - telnet://192.168.101.253:32780
Id: 13 - R13 - csr1000vng - telnet://192.168.101.253:32781
Id: 14 - R14 - csr1000vng - telnet://192.168.101.253:32782
Id: 2 - R2 - xrv - telnet://192.168.101.253:32770
Id: 8 - R8 - xrv - telnet://192.168.101.253:32776
==================================================
Please select the node Id that you want to start: 1
==================================================
{'code': 200, 'status': 'success', 'message': 'Node started (80049).'}
==================================================
Do you want to start another node? yes(Y) or no (N): y
==================================================
Id: 1 - R1 - csr1000vng - telnet://192.168.101.253:32769
Id: 3 - R3 - csr1000vng - telnet://192.168.101.253:32771
Id: 4 - R4 - csr1000vng - telnet://192.168.101.253:32772
Id: 5 - R5 - csr1000vng - telnet://192.168.101.253:32773
Id: 6 - R6 - csr1000vng - telnet://192.168.101.253:32774
Id: 7 - R7 - csr1000vng - telnet://192.168.101.253:32775
Id: 9 - R9 - csr1000vng - telnet://192.168.101.253:32777
Id: 10 - R10 - csr1000vng - telnet://192.168.101.253:32778
Id: 11 - R11 - csr1000vng - telnet://192.168.101.253:32779
Id: 12 - R12 - csr1000vng - telnet://192.168.101.253:32780
Id: 13 - R13 - csr1000vng - telnet://192.168.101.253:32781
Id: 14 - R14 - csr1000vng - telnet://192.168.101.253:32782
Id: 2 - R2 - xrv - telnet://192.168.101.253:32770
Id: 8 - R8 - xrv - telnet://192.168.101.253:32776
==================================================
Please select the node Id that you want to start: 2
==================================================
{'code': 200, 'status': 'success', 'message': 'Node started (80049).'}
==================================================
Do you want to start another node? yes(Y) or no (N): n
===============================================
Logging out...
===============================================
```