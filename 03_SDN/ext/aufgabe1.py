#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.packet.ethernet import ethernet, ETHER_BROADCAST
from pox.lib.packet.ipv4 import ipv4
from pox.lib.packet.arp import arp
from pprint import pprint 

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
    
    def __init__(self):
        log.info("KIT SDN Demo Controller started!")
        self.counter = 0
            
    def _handle_PacketIn (self, event):
        pkt = MyPacket(event)
        self.counter += 1
        log.info("PACKET_IN received ... (%d)", self.counter)
        pkt.flood()

def _handle_ConnectionUp (event):
  event.connection.addListeners(MyController())

def launch ():
  core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
  log.info("KIT SDN Demo Controller launched! (task: silent arp)")
