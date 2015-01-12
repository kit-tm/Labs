#!/usr/bin/python

import sys
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

"""
    SDN Szenario 1
    @author: Robert Bauer
"""

#!/usr/bin/python      
def SDNLabDemonet():
    

    print "*** start mininet for task #1"

    net = Mininet( topo=None, build=False)

    # create the nodes
    h1 = net.addHost( 'h1', ip='192.168.0.1/24' )
    h2 = net.addHost( 'h2', ip='192.168.0.2/24' )
    h3 = net.addHost( 'h3', ip='192.168.0.3/24' )
    h4 = net.addHost( 'h4', ip='192.168.0.4/24' )
    
    # create the switch
    s1 = net.addSwitch( 's1', listenPort=16001)

    # create the links
    net.addLink(h1, s1, )
    net.addLink(h2, s1, )   
    net.addLink(h3, s1, )   
    net.addLink(h4, s1, )
    
    # add controller
    controller = net.addController( 'c', controller=RemoteController, ip="127.0.0.1", port=16001)
    net.build()

    # connect controller
    s1.start( [controller] )
    
    # looks like the mac setter in the addHist function doesn't work, so we handle this here
    s1.setMAC("aa:aa:aa:aa:aa:aa")
    h1.setMAC("cc:cc:cc:cc:cc:01")
    h2.setMAC("cc:cc:cc:cc:cc:02")
    h3.setMAC("cc:cc:cc:cc:cc:03")
    h4.setMAC("cc:cc:cc:cc:cc:04")
     
    # start mininet CLI
    c = CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    SDNLabDemonet()