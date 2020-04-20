'''Module to Print the IP's of Interface in the Linux System'''
from __future__ import print_function
import os
#IP Extraction Logic from IfConfig
IPV4_CMD = " | grep -E -o \"inet addr:[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.\
[[:digit:]]{1,3}\.[[:digit:]]{1,3}\" | cut -d':' -f 2"
IPV6_CMD = " | grep -E -o \"inet6 addr:\ [aAbBcCdDeEfF[:digit:]:/]*\" | \
cut -d' ' -f 3"
#End of IP Extraction Logic from IfConfig

def get_interfaces():
    '''Stores the Interfaces names as a list - Get the interfaces names
    alone using grep regularexpression and split it using new line character
    to store it as a list and filter unwanted new line strings
    '''
    try:
        interfaces = filter(lambda int_name: len(int_name) != 0, os.popen(" \
    ifconfig | grep -o -E \"^[[:alnum:]]{1,}\"").read().split("\n"))
    #Handle error in the command execution
    except:
        print("Error occured in the command execution")
        return "NULL"
    #Command executed properly, return Interfaces list
    else:
        return interfaces

def addr_extraction(interfaces=None):
    '''Extract the Interface and IP's as a list'''
    if interfaces is None:
        interfaces = get_interfaces()
    if interfaces == "NULL":
        return "No Interfaces extracted. So No IPv4 / IPV6 etxrtacted"
    interface_ip_list = []
    #Prepare List of Interface, IPV4, IPv6 Tuples
    for each_interface in interfaces:
        ipv4_addr, ipv6_addr = None, None
        try:
            ipv4_addr = os.popen("ifconfig " + each_interface + IPV4_CMD).\
            read().strip()
            if ipv4_addr is None or ipv4_addr == '':
                ipv4_addr = 'NA'
            ipv6_addr = os.popen("ifconfig " + each_interface + IPV6_CMD).\
            read().strip()
            if ipv6_addr is None or ipv6_addr == '':
                ipv6_addr = 'NA'
        except:
            print("Some Error in extraction of IP Addresses")
        interface_ip_list.append((each_interface, ipv4_addr, ipv6_addr))
    return interface_ip_list

#Driver Program to test the modules
RESULT = addr_extraction()
if type(RESULT).__name__ == 'str':
    print(RESULT)
else:
    #Decoration Stuff
    print('*'*90, ' '*20 + "Interface along with its IP Information", '*'*90, sep='\n')
    print("%20s  %20s  %40s"%("Name of Interface", "IPV4 Address", "IPV6 Address"))
    #Print the result
    for each_tup in RESULT:
        print("%20s  %20s  %40s"%(each_tup[0], each_tup[1], each_tup[2]))
