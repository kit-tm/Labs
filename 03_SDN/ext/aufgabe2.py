#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.packet.ethernet import ethernet, ETHER_BROADCAST
from pox.lib.packet.ipv4 import ipv4
from pox.lib.packet.arp import arp
from pprint import pprint 
from pox.lib.addresses import IPAddr, EthAddr

from helper import MyPacket, MyFlow

log = core.getLogger()

class MyController():
    """
        Hier koennen Sie ihren eigenen Controller implementieren.
        Die _handle_PacketIn()-Funktion wird immer dann aufgerufen, wenn
        ein Paket ohne Match an den Controller weitergereicht wird.
        Die __init__ Funktion wird einmal aufgerufen wenn der 
        Controller erzeugt wird (Konstruktor).
    """  

    def __init__(self, dpid, mac):
        self.dpid = dpid # datapath id of this switch
        self.mac = mac # the mac addr of this switch
            
    def _handle_PacketIn (self, event):
        pkt = MyPacket(event)
        # todo
      
def _handle_LinkEvent(event):
    print "link event -------->"
    for l in core.openflow_discovery.adjacency:
        print l.dpid1, l.dpid2, l.port1, l.port2

def _handle_ConnectionUp (event):
  mac = EthAddr("%012x" % (event.dpid & 0xffFFffFFffFF,))
  print "new switch with mac address %s and dpid %s connected" % (mac, event.dpid)
  event.connection.addListeners(MyController(event.dpid, mac))

def launch ():
  core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
  core.openflow_discovery.addListenerByName("LinkEvent", _handle_LinkEvent)
  log.info("KIT SDN Demo Controller launched! (task: multi switch)")
