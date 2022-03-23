from pprint import pprint
from ttp import ttp
import json
import time
import urllib.request as urllib2
import json
import codecs
import re
import os
from termcolor import colored
import sys
from netmiko import ConnectHandler

IPs = [10.10.10.1, 10.10.10.2] # IPs of the devices where proxy-nd learned. There can be many PEs where members are connected. 

for ip in IPs: 

    ssh = {
        'device_type': 'alcatel_sros',
        'ip': ip,
        'username': 'admin',
        'password': 'admin',
        'port': '22'
    }

    print ('Connection successful')

    net_connect = ConnectHandler(**ssh)
    data_to_parse = net_connect.send_command('show service id 4000 proxy-nd detail')
    #print (output)

    def proxy_nd(data_to_parse):
        ttp_template = template_proxy_nd_detail

        parser = ttp(data=data_to_parse, template=ttp_template)
        parser.parse()

        # print result in JSON format
        results = parser.result(format='json')[0]
        #print(results)

        #converting str to json. 
        result = json.loads(results)
        
        return(result)

    parsed_proxy_nd = proxy_nd(data_to_parse)

    #print(proxy_nd(data_to_parse))

    #print(parsed_proxy_nd[0])

    router_count = 0
    host_count = 0

    for proxy in parsed_proxy_nd[0]:
        if proxy == "PROXY_ND": # Which means we will check each entry. 
            #print(parsed_proxy_nd[0]["PROXY_ND"])
            for entry in parsed_proxy_nd[0]["PROXY_ND"]:
                #print(entry)
                if entry["if_router_host"] == "Rtr":
                    print(f"The type of the device which has IPv6 : {entry['IPv6_Address']}, Mac : {entry['Mac_Address']} and Type : {entry['Type']} is {entry['if_router_host']}")
                    router_count += 1
                elif entry["if_router_host"] == "Host":
                    print(f"The type of the device which has IPv6 : {entry['IPv6_Address']}, Mac : {entry['Mac_Address']} and Type : {entry['Type']} is {entry['if_router_host']}")
                    host_count += 1
        elif proxy == "TOTAL_ENTRY": # Which means we will get all numbers. 
            print(f"The Number Of Proxy-ND Entries : {parsed_proxy_nd[0]['TOTAL_ENTRY']['Number_Of_Entries']}")

    print(f"Number of Routers is {router_count}")
    print(f"Number of Hosts is {host_count}")
