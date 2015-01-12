#!/bin/sh
cmd="python  $sdn_lab_dir/pox.py openflow.of_01 --port=16001 aufgabe0"
echo "+---------------------+"
echo "| controller: SDN LAB |"
echo "+---------------------+"
echo $cmd
eval $cmd

