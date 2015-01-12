#!/usr/bin/python

import sys
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

"""
    SDN Szenario 2
    @author: Robert Bauer
"""

def int2dpid( dpid ):
    dpid = hex( dpid )[ 2: ]
    dpid = '0' * ( 16 - len( dpid ) ) + dpid
    return dpid

#!/usr/bin/python      
def SDNLabDemonet():
    

    print "*** start mininet for task #2"

    net = Mininet( topo=None, build=False)

    # create the nodes
    h1 = net.addHost( 'h1', ip='10.0.0.1/8' )
    h2 = net.addHost( 'h2', ip='10.0.0.2/8' )
    h3 = net.addHost( 'h3', ip='192.168.0.1/24' )
    h4 = net.addHost( 'h4', ip='192.168.0.2/24' )
    
    # create the switch
    s1 = net.addSwitch( 's1',  dpid=int2dpid(500), listenPort=16001)
    s2 = net.addSwitch( 's2',  dpid=int2dpid(700), listenPort=16001)
    
    # create the links
    net.addLink(h1, s1, )
    net.addLink(h2, s1, )   
    net.addLink(s1, s2, )
    net.addLink(h3, s2, )   
    net.addLink(h4, s2, )
    
    # add controller
    controller = net.addController( 'c', controller=RemoteController, ip="127.0.0.1", port=16001)
    net.build()

    # looks like the mac setter in the addHist function doesn't work, so we handle this here
    s1.setMAC("aa:aa:aa:aa:aa:01")
    s2.setMAC("aa:aa:aa:aa:aa:02")
    h1.setMAC("cc:cc:cc:cc:cc:01")
    h2.setMAC("cc:cc:cc:cc:cc:02")
    h3.setMAC("cc:cc:cc:cc:cc:03")
    h4.setMAC("cc:cc:cc:cc:cc:04")
 
    # update routing tables
    h1.cmd("route add -net 192.168.0.0/24 h1-eth0")
    h2.cmd("route add -net 192.168.0.0/24 h2-eth0")
    h3.cmd("route add -net 10.0.0.0/8 h3-eth0")
    h4.cmd("route add -net 10.0.0.0/8 h4-eth0")
    
    # connect controller
    s1.start( [controller] )
    s2.start( [controller] )
     
    # start mininet CLI
    c = CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    SDNLabDemonet()
