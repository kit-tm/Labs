#!/bin/bash
if [ "$(id -u)" != "0" ]; then
        echo "You must have root privileges to execute this script."
        exit 1
fi

echo ""
echo "Adding bandwidth delay of 100ms to eth0..."
echo ""
modprobe cls_fw
modprobe sch_netem
/sbin/tc qdisc add dev eth0 root netem delay 100ms limit -1 duplicate 0
