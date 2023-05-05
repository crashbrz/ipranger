![License](https://img.shields.io/badge/license-sushiware-red)
![Issues open](https://img.shields.io/github/issues/crashbrz/ipranger)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/crashbrz/ipranger)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/crashbrz/ipranger)
![GitHub last commit](https://img.shields.io/github/last-commit/crashbrz/ipranger)

# IP Ranger 
The IP Ranger tool allows users to input an IP address and CIDR notation and generate a list of IP addresses based on the provided information.
The tool takes the network address and subnet mask, calculates the range of IP addresses within the subnet, and generates a list of all possible IP addresses within that range.
This tool is helpful for pentesters, network administrators, and engineers who need to create a list of IP addresses quickly.

Usage example:
```
┌──(crash㉿Anubis)-[~]
└─$ python3 ipranger.py 10.3.3.0/24 

 ```
- The above command will display all the IP addresses for the input range.

```
┌──(crash㉿Anubis)-[~]
└─$ python3 ipranger.py 10.3.3.0/24 iplist_for_10_network.txt 

 ```
- The above command will display and save all the IP addresses to the file iplist_for_10_network.txt

### Usage/Help ###
Run ipranger.py without parameters. Also, you can contact me (@crashbrz) on Twitter<br>

### Installation ###
pip install pysnmp<br>
Clone the repository in the desired location.<br>

### License ###
IP Ranger is licensed under the SushiWare license. Check [docs/license.txt](docs/license.txt) for more information.
 
### Python Version ###
Tested on:<br>
Python 3.10.9
