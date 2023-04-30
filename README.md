# Utils

## ecscheck
For easier to tell whether a DNS server supports ECS protocol.
Before use it, dont forget install dnspython package with
**pip install dnspython**
then run 
**python3 ecscheck.py host/domain IP_of_DNS_SERVER Client_SUBNET_IP_IN_CIDR**

example:
python3 ecscheck.py cdn-niu-cdrs01.tanetcdn.edu.tw 8.8.8.8 59.124.220.95/24