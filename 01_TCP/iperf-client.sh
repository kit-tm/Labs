#! /bin/sh
echo ""
echo "starting iperf client (running for some seconds) ..."
echo ""
iperf -c localhost -p 1980 --tcp-info=statistics.txt --tcp-info-time=100 $1 $2 $3
