#!/bin/sh
echo "+-----------------------------------+"
echo "| controller: MULTI SWITCH (task 2)"
echo "| default logging: disabled"
if [ -z $1 ]; then 
	task="aufgabe2"
else 
	echo "| use task: $1"
	task=$1 
fi
cmd="python  $sdn_lab_dir/pox.py openflow.of_01 --port=16001 log --no-default openflow.discovery $task"
echo "+-----------------------------------+"
echo $cmd
eval $cmd
