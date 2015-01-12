#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014-2015 Robert Bauer (robert.bauer@kit.edu)
# 
# A small helper class providing some basic wrapper functions
# for simple openflow control handling with the POX-Controller.
# See aufgabe0.py for an simple example of how to use this file.
# 
# Copyright (c) 2015,
# Karlsruhe Institute of Technology, Institute of Telematics
# Zirkel 2, 76131 Karlsruhe
# Germany 
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# IMPORTANT: This file uses the POX-Controller (https://github.com/noxrepo/pox)
# which is published under the Apache License, Version 2.0. No modifications
# to the POX-Controller were made, except for the additional files in the
# pox/ext folder.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.packet.ethernet import ethernet, ETHER_BROADCAST
from pox.lib.packet.ipv4 import ipv4
from pox.lib.packet.arp import arp
from pox.lib.addresses import IPAddr, IPAddr6, EthAddr

class MyPacket():
    
    def __init__(self, event):
        self.event = event;
        self.dpid = event.connection.dpid;
        self.inport = event.port;
          
    def send_to_port(self, port):
        msg = of.ofp_packet_out()
        msg.actions.append(of.ofp_action_output(port = port))
        msg.data = self.event.ofp
        msg.in_port = self.event.port
        self.event.connection.send(msg)

    def flood(self):
        self.send_to_port(of.OFPP_FLOOD)  
                
    def get_inport(self):
        return self.event.port
    
    def is_arp(self):
        packet = self.event.parsed
        return isinstance(packet.next, arp)
        
    def get_arp_ip_source(self):
        """
            Gibt die IP-Adresse des Systems zurueck, von dem der ARP-Request gestartet wurde.
            Gibt None zurueck, falls es sich nicht um ein ARP-Request Paket handelt.
        """
        packet = self.event.parsed
        if not isinstance(packet.next, arp): return None
        return packet.next.protosrc        

    def get_arp_ip_target(self):
        """
            Gibt die aufzuloesende IP-Adresse eines ARP-Request Paketes zurueck.
            Gibt None zurueck, falls es sich nicht um ein ARP-Request Paket handelt.
        """
        packet = self.event.parsed
        if not isinstance(packet.next, arp): return None
        return packet.next.protodst
    
    def answer_arp(self, mac):
        """
            Erstellt fuer ein eingegangenes ARP-Request Paket ein Antwortpaket, dass
            fuer die angefragte IP-Adresse mac als Antwort zurueckgibt.
        """
        packet = self.event.parsed
        if not isinstance(packet.next, arp): return
        a = packet.next
        if a.opcode == arp.REQUEST:
            r = arp()
            r.hwtype = a.hwtype
            r.prototype = a.prototype
            r.hwlen = a.hwlen
            r.protolen = a.protolen
            r.opcode = arp.REPLY
            r.hwdst = a.hwsrc
            r.protodst = a.protosrc
            r.protosrc = a.protodst
            r.hwsrc = mac
            e = ethernet(type=packet.type, src=mac, dst=a.hwsrc)
            e.set_payload(r)
            # log.debug("%i %i answering ARP for %s" % (dpid, inport,str(r.protosrc)))
            msg = of.ofp_packet_out()
            msg.data = e.pack()
            msg.actions.append(of.ofp_action_output(port = of.OFPP_IN_PORT))
            msg.in_port = self.inport
            self.event.connection.send(msg)   
     
    def get_mac_src(self):
        packet = self.event.parsed
        if isinstance(packet, ethernet):
            return packet.src
        return None;

    def get_mac_dst(self):
        packet = self.event.parsed
        if isinstance(packet, ethernet):
            return packet.dst
        return None;
    
    def get_ip_src(self):
        packet = self.event.parsed
        if isinstance(packet.next, ipv4):
            return packet.next.srcip
        return None;
    
    def get_ip_dst(self):
        packet = self.event.parsed
        if isinstance(packet.next, ipv4):
            return packet.next.dstip
        return None;

class MyFlow():
    
    def __init__(self, event):
        self.event = event
        self.msg = of.ofp_flow_mod()        

    def program(self):
        self.event.connection.send(self.msg)
    
    def action_output(self, port):
        self.msg.actions.append(of.ofp_action_output(port = port))
        
    def action_drop(self):
        pass
    
    def set_idle_timeout(self, t):
        self.msg.idle_timeout = t

    def set_hard_timeout(self, t):
        self.msg.hard_timeout = t
           
    def match_mac_src(self, addr):
    	if isinstance(addr, basestring):
    		addr = EthAddr(addr)
        self.msg.match.dl_src = addr
        
    def match_mac_dst(self, addr):
    	if isinstance(addr, basestring):
    		addr = EthAddr(addr)
        self.msg.match.dl_dst = addr

    def match_ip_src(self, addr):
        self.msg.match.dl_type = ethernet.IP_TYPE #  required!
        self.msg.match.nw_src = addr
        
    def match_ip_dst(self, addr):
        self.msg.match.dl_type = ethernet.IP_TYPE #  required!
        self.msg.match.nw_dst = addr
        
    def match_inport(self, port):
        self.msg.match.in_port = int(port)
