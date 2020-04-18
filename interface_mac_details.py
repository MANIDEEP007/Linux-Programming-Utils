'''Module to Print the Interface Information in the Linux System'''
from __future__ import print_function
import os

def get_interfaces():
    '''Stores the Interfaces names as a list - Get the interfaces names
    alone using grep regularexpression and split it using new line character
    to store it as a list and filter unwanted new line strings
    '''
    interfaces = filter(lambda int_name: len(int_name) != 0, os.popen(" \
    ifconfig | grep -o -E \"^[[:alnum:]]{1,}\"").read().split("\n"))
    return interfaces

def mac_addresses(interfaces=None):
    '''
    Stores the Mac Address and interface Tuples in a list
    '''
    #If interfaces are not passes, get it by calling get_interfaces function
    if interfaces is None:
        interfaces = get_interfaces()
    interface_mac_list = []
    #Loop over the interface Names, get mac address & store as list of tuples
    for each_interface in interfaces:
        mac_addr = ""
        mac_addr = os.popen("ifconfig "+ each_interface +"| grep \
        -o \"HWaddr.*\" | cut -d' ' -f 2").read().strip()
        if mac_addr == '':
            mac_addr = 'NA'
        interface_mac_list.append((each_interface, mac_addr))
    return interface_mac_list

#Driver program to test the functions
MAC_INTERFACE_LIST = mac_addresses()
#Decoration
print('*'*31, "Interface and Mac Address List", '*'*31, sep='\n')
#Print Interface name and corresponding MAC Address if available
for each_tup in MAC_INTERFACE_LIST:
    print("%10s - %10s"%(each_tup[0], each_tup[1]))
