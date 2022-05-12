# EVPN_proxy-nd_Hosts_Routers
How to get all Hosts and Routers shown under proxy-nd table. 

There is a distinction between host and routers when doing proxy-nd is explained in RFCs 9161 and the solution in 9047. Thanks to the distinction, we are able to identify Rtr or Host of specific IPv6 and Mac addresses. 

See a sample output from the CLI: 

![image](https://user-images.githubusercontent.com/94804863/159651921-b90465cd-f543-44f7-a783-1a448753197a.png)

Normally many addresses can be learned, and it is important to know how many routers and hosts learned and the vendor of the specific IP from different devices in once.  

For more detail regarding to RFC 9047:

https://www.ietf.org/rfc/rfc9047.pdf

In following topology, there are hosts and routers connected to PE (R1 and R2 nodes). There can be many PEs where members are connected.

![image](https://user-images.githubusercontent.com/94804863/159652948-82d54125-cce7-4c63-a780-f2b08c658fb5.png) 
